from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtGui

from guilib.FaceRecognitionScreen import Ui_FaceRecognitionWidget
from guilib.html_text_generator.html_draft import gen_error_text,gen_info_text
from guilib.external_thread_modules.FaceRecognitionDirectoryTransfer import directoryAdderThread
from guilib.external_thread_modules.FaceRecognitionManuelDatabaseSearch import manuelDatabaseSearcherThread

from hivelibrary.console_tools import InformationPrinter
from hivelibrary.env import DEFAULT_LOGO_PATH,DB_FACE_RECOGNITION_TABLE,DEFAULT_TEMP_DIR,DEFAULT_ROOT_DIR_NAME
from hivelibrary.face_recognition_database_tools import recognitionDbTools,get_image_from_id
from hivelibrary.file_operations import generic_tools


import os
import sqlite3

class faceRecognitionBackendThread(QThread):
    
    statusSignal = pyqtSignal(dict)

    def __init__(self, targetFaceImagePath:str, faceAnalayserUI:object, db_curosr, minSimilarityRate:int):
        super().__init__()
        
        self.databaseCursor = db_curosr
        self.targetImagePath = targetFaceImagePath
        self.faceAnalayserUI = faceAnalayserUI
        self.threadStopSignal = False
        self.minSimilarity = minSimilarityRate
        self.similartiyStorageDcit = {}
        self.maxThread = 100
        
    def stop(self):
        self.threadStopSignal = True
        msg = {"end":True,"success":False,"text":f"<B>INFO: </B>Thread killed by user!",}
        self.statusSignal.emit(msg)
        return
    
    def __runningStatusReturner(self, text:str):
        data_dict = {"success":None, "end":False, "text":text}
        self.statusSignal.emit(data_dict)
        
            
    def __finalyStatusReturner(self,text:str,success_status:bool, cv2_image=None,face_name=None,add_date=None,similartiy=None,target_raw_data=None):
        data_dcit = {"success":success_status, "end":True, "text":text, "cv2_image":cv2_image, "face_name":face_name,"add_date":add_date, "similartiy":similartiy }
        self.statusSignal.emit(data_dcit)
    def run(self):
        
        import cv2
        import numpy
        from hivelibrary.ImageTools.opencv_tools import landmarks_rectangle,landmarks_rectangle_2d
        self.__runningStatusReturner(text="Gereksinimler başarıyla içe aktarıldı")
        raw_cv2_image = cv2.imread(self.targetImagePath)
        analysedSourceImage = self.faceAnalayserUI.get(raw_cv2_image)
        self.__runningStatusReturner(text=f"Seçilen en düşük benzerlik değeri: %{self.minSimilarity}")
        self.__runningStatusReturner(text="Veritabanı kontrol ediliyor")
        self.databaseCursor.execute(f"SELECT COUNT(*) FROM {DB_FACE_RECOGNITION_TABLE}")
        rsults = self.databaseCursor.fetchall()[0][0]
        if int(rsults) < 1:
            self.__finalyStatusReturner(text=gen_error_text("Veritabanı boş, arama yapmak için önce veritabanına ekleme yapınız"),success_status=False,)
            return 
        
        if len(analysedSourceImage) > 1:
            self.__finalyStatusReturner(text=gen_error_text("Kaynak resimde 1 den fazla yüz kabul edilemez"),success_status=False,)
            return

        if len(analysedSourceImage) == 0:
            self.__finalyStatusReturner(text=gen_error_text("Kaynak resimde herhangi bir yüz bulunamadı"),success_status=False,)
            return      
        
        sourceFaceEmbeddings = analysedSourceImage[0]["embedding"]
        STATIC_SQL_COMMAND = f"SELECT id,face_name,face_embedding_data FROM {DB_FACE_RECOGNITION_TABLE}"
        self.databaseCursor.execute(STATIC_SQL_COMMAND)
        self.__runningStatusReturner(text=f"Veritabanı boyutu: {rsults}")
        self.__runningStatusReturner(text="Arama için döngü başlatıldı")
        
        totalAnalysCount = 0
        while self.threadStopSignal != True:
            
            get_rows = self.databaseCursor.fetchmany(self.maxThread)
            if not get_rows:
                break
            
            for single_row in get_rows:
                row_id = single_row[0]
                face_name = single_row[1]
                targetEmbeds = numpy.frombuffer(single_row[2],dtype=numpy.float32)
                calculateSimilartiy = generic_tools.cosineSimilarityCalculator(sourceFaceEmbeddings,targetEmbeds)
                if calculateSimilartiy >= self.minSimilarity:
                    self.similartiyStorageDcit[row_id] = calculateSimilartiy
        
        if self.threadStopSignal == True:
            self.__finalyStatusReturner(text=gen_error_text(f"%{self.minSimilarity} veya daha yüksek bir oranda eşleşme bulunamadı sistemde"),success_status=False,)
            return
        
        self.__runningStatusReturner(text="arama tamamlandı sonuçlar işleniyor")
        if len(self.similartiyStorageDcit) < 1:
            self.__finalyStatusReturner(text=gen_error_text("Veritabanında kişiye benzer birisi bulunamadı."),success_status=False,face_name="Failed To detec",similartiy=0)
            return
        
        enBenzerID = max(list(self.similartiyStorageDcit.values()))
        enYuksekBenzerlik = enBenzerID
        
        for key, value in self.similartiyStorageDcit.items():
            if value == enYuksekBenzerlik:
                enBenzerID = key
        
        STATIC_SQL_COMMAND = f"SELECT * FROM {DB_FACE_RECOGNITION_TABLE} WHERE id=%s"
        STATIC_DATA_TUPLE = (enBenzerID,)
        
        self.databaseCursor.execute(STATIC_SQL_COMMAND,STATIC_DATA_TUPLE)
        results = self.databaseCursor.fetchall()[0]
        detectedFaceSimilartiyRate = self.similartiyStorageDcit[enBenzerID]
        detectedFaceDatabaseID= enBenzerID
        detectedFacePictur = results[1]
        detectedFacePictureHash = results[2]
        detectedFaceName = results[6]
        detectedFaceAddDate = results[7]

        return_text = f"""<B>Bulunan Eşleşme Bilgileri: </B><br>
<B>Kişinin kayıtlı adı:</B> {detectedFaceName}<br>
<B>Benzerlik oranı: </B> %{enYuksekBenzerlik}<br>
<B>Veritabanı ID: </B>{detectedFaceDatabaseID}<br>
<B>Resim sha1 hash'i: </B> {detectedFacePictureHash}<br>
<B>Veritabanına eklenme tarihi UTC: </B> {detectedFaceAddDate}<br>
<B>{"-"*20}<B/><br>"""


        self.__finalyStatusReturner(text=return_text,success_status=True,cv2_image=detectedFacePictur,face_name=detectedFaceName,similartiy=detectedFaceSimilartiyRate)

class FaceRecognitionWidget(QWidget):
    def __init__(self, db_cnn, db_curosr, mainConfig):
        super().__init__()
        self.mainConfig = mainConfig
        self.FaceRecognitionPage = Ui_FaceRecognitionWidget()
        self.FaceRecognitionPage.setupUi(self)
        self.setWindowTitle("Face Recognition From Image")
        self.LabelSupportedResulation = (320, 320)
        self.showDefaultImage(targetLabel=self.FaceRecognitionPage.label_soruceImageShower)
        self.showDefaultImage(targetLabel=self.FaceRecognitionPage.label_detectedImageShower)
        self.showDefaultImage(targetLabel=self.FaceRecognitionPage.label_selected_image_show)
        self.showDefaultImage(targetLabel=self.FaceRecognitionPage.label_dbManuelSearchImageShower)
        self.selectedSourceImage = None
        self.sistemeEklenecekImageSelected = None
        self.FaceRecognitionPage.pushButton_selectSourceImage.clicked.connect(self.selectSourceImage)
        self.FaceRecognitionPage.pushButton_removeSourceImage.clicked.connect(self.removeSourceImage)
        self.FaceRecognitionPage.pushButton_startDbSearch.clicked.connect(self.startDatabaseSearch)
        self.FaceRecognitionPage.pushButton_stopSearch.clicked.connect(self.sendKillSignalThread)
        self.FaceRecognitionPage.pushButton_tab2_resim_sec.clicked.connect(self.selectEklenecekResim)
        self.FaceRecognitionPage.pushButton_tab2_sistemeEkle.clicked.connect(self.tekilResimEkleme_start)
        self.FaceRecognitionPage.pushButton_selectDirectory.clicked.connect(self.selectTargetDirectory)
        self.FaceRecognitionPage.pushButton_startMultiAdder.clicked.connect(self.startMultiAdder)
        self.FaceRecognitionPage.pushButton_stopMultiAdder.clicked.connect(self.mulitAdderThreadKillSignal)
        self.FaceRecognitionPage.pushButton_starManueltSearch.clicked.connect(self.start_manuel_database_search)
        self.FaceRecognitionPage.pushButton_clearResultManuelSearch.clicked.connect(self.clear_all_manuel_search_output)
        self.FaceRecognitionPage.pushButton_stopActiveManuelSearch.clicked.connect(self.stopActivaManuelSearch)
        self.FaceRecognitionPage.pushButton_saveCurrentImage.clicked.connect(self.save_current_image)
        self.FaceRecognitionPage.comboBox_targetColumn.currentIndexChanged.connect(self.updateManuelSearchLineEdit)
        self.FaceRecognitionPage.tableWidget_resultTable.cellClicked.connect(self.table_widget_signal_handler)
        self.FaceRecognitionPage.tableWidget_resultTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.DatabaseSearchThread = QThread()
        self.MultiAdderThread = QThread()
        self.manuelSearchThread = QThread()
        self.minimumSimilaritySize = self.getMinSimilartiyCurrentValue()
        self.databaseConnections = db_cnn
        self.databaseCursor = db_curosr
        self.selectedDirectory = None
        self.targettDir_is_selected = False
        InformationPrinter(f"importing insightFace")
        import insightface
        InformationPrinter(f"initing face detection system")
        self.FaceAnalysisUI = insightface.app.FaceAnalysis() 
        self.FaceAnalysisUI.prepare(ctx_id=-1,det_thresh=0.5)
        InformationPrinter("Face detection system succesfully init")
        InformationPrinter("initing FaceRecognitionDatabaseTools")
        self.faceRecDbTools = recognitionDbTools(db_cnn=self.databaseConnections,db_curosr=self.databaseCursor)        
        InformationPrinter("FaceRecognitionDatabaseTools successfuly init")
        
    

    
    def getMinSimilartiyCurrentValue(self) -> int:
        currentIndex = self.FaceRecognitionPage.comboBox_minSimVal.currentIndex()
        
        if currentIndex == 0:
            return 10
        if currentIndex == 1:
            return 20
        if currentIndex == 2:
            return 30
        if currentIndex == 3:
            return 35
        if currentIndex == 4:
            return 40
        if currentIndex == 5:
            return 45
        if currentIndex == 6:
            return 50
        if currentIndex == 7:
            return 60
        if currentIndex == 8:
            return 70
        if currentIndex == 9:
            return 80
        if currentIndex == 10:
            return 90
        if currentIndex == 11:
            return 100
        
        
    
    def threadSignalHandler(self,thread_dict):
        if thread_dict["success"] == None and thread_dict["end"] == False:
            self.FaceRecognitionPage.textBrowser_logConsole.append(gen_info_text(str(thread_dict["text"])))
            return
        
        if thread_dict["success"] != True and thread_dict["end"] == True:
            self.FaceRecognitionPage.textBrowser_logConsole.append(str(thread_dict["text"]))
            self.FaceRecognitionPage.progressBar_benzerlikBari.setValue(0)
            self.showDefaultImage(targetLabel=self.FaceRecognitionPage.label_detectedImageShower)
            return
        
        if thread_dict["success"] == True and thread_dict["end"] == True:
            self.FaceRecognitionPage.textBrowser_logConsole.append(str(thread_dict["text"]))
            self.FaceRecognitionPage.progressBar_benzerlikBari.setValue(thread_dict["similartiy"])
            self.show_cv2_image_target_label(image_data=thread_dict["cv2_image"],targetLabel=self.FaceRecognitionPage.label_detectedImageShower)
    
    
            
    def sendKillSignalThread(self):
        if not self.DatabaseSearchThread.isRunning():
            self.FaceRecognitionPage.textBrowser_logConsole.append(gen_error_text("No running jobs!"))
            return
        
        self.FaceRecognitionPage.textBrowser_logConsole.append(gen_info_text("ending kill signal..."))
        self.DatabaseSearchThread.stop()
    
    
    
    def startDatabaseSearch(self):
        if self.DatabaseSearchThread.isRunning():
            self.FaceRecognitionPage.textBrowser_logConsole.append(gen_error_text("İşlem zaten aktif, yeniden başlatmak için bitmeli veya durdurulmalı"))
            return   
        
        if self.MultiAdderThread.isRunning():
            self.FaceRecognitionPage.textBrowser_logConsole.append(gen_error_text("Klasör ekleme işlemi aktif iken arama yapılamaz"))
            return
        
        if self.selectedSourceImage == None :
            self.FaceRecognitionPage.textBrowser_logConsole.append(gen_error_text("Kaynak resim seçilmedi, işlem iptal edildi"))
            return
        
        self.FaceRecognitionPage.textBrowser_logConsole.clear()
        self.minimumSimilaritySize = self.getMinSimilartiyCurrentValue()
        self.FaceRecognitionPage.textBrowser_logConsole.append(gen_info_text("Veritabanı araması başlaılıyor"))
        self.DatabaseSearchThread = faceRecognitionBackendThread(targetFaceImagePath=self.selectedSourceImage,faceAnalayserUI=self.FaceAnalysisUI,db_curosr=self.databaseCursor,minSimilarityRate=self.minimumSimilaritySize)
        self.DatabaseSearchThread.statusSignal.connect(self.threadSignalHandler)
        self.DatabaseSearchThread.start()

        
        
    def showDefaultImage(self, targetLabel):
        import cv2
        image_data = cv2.imread(DEFAULT_LOGO_PATH)
        image_data = cv2.resize(image_data, self.LabelSupportedResulation)
        image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
        img_height, img_width = self.LabelSupportedResulation
        image_data = QtGui.QImage(image_data, img_width, img_height,QtGui.QImage.Format.Format_RGB888)
        targetLabel.setPixmap(QtGui.QPixmap(image_data))
        
        
        
    def show_cv2_image_target_label(self,image_data,targetLabel):
        import cv2
        import random
        rand_save_name =str(DEFAULT_TEMP_DIR) +str(os.path.sep) + f"temp_save_{random.randint(1,9999)}.png"
        with open(rand_save_name, "wb+") as savefile:
            savefile.write(image_data)

        image_data = cv2.imread(rand_save_name)
        os.remove(rand_save_name)        
        image_data = cv2.resize(image_data, self.LabelSupportedResulation)
        image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
        img_height, img_width = self.LabelSupportedResulation
        image_data = QtGui.QImage(image_data, img_width, img_height,QtGui.QImage.Format.Format_RGB888)
        targetLabel.setPixmap(QtGui.QPixmap(image_data))
        
        
        
    def addImageInWindow_usingFilePath(self,target_image,target_label):
        import cv2
        image_data = cv2.imread(target_image)
        image_data = cv2.resize(image_data, self.LabelSupportedResulation)
        image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
        img_height, img_width = self.LabelSupportedResulation
        image_data = QtGui.QImage(image_data, img_width, img_height,QtGui.QImage.Format.Format_RGB888)
        target_label.setPixmap(QtGui.QPixmap.fromImage(image_data))
        
        
        
    def removeSourceImage(self):
        if self.selectedSourceImage != None:
            self.selectedSourceImage = None
            self.showDefaultImage(targetLabel=self.FaceRecognitionPage.label_soruceImageShower)
            self.FaceRecognitionPage.textBrowser_logConsole.append(gen_info_text("Kaynak resim kaldırıldı"))
            return
        self.FaceRecognitionPage.textBrowser_logConsole.append(gen_error_text("Kaynak resim zaten seçili değil"))
        
        
        
    def selectSourceImage(self):
        fileSelector = QFileDialog()
        fileSelector.setNameFilter("Image Files (*.jpg *.png *.jpeg *.webm)")
        if fileSelector.exec_():
            self.selectedSourceImage = fileSelector.selectedFiles()[0]

        if self.selectedSourceImage == None:
            self.FaceRecognitionPage.textBrowser_logConsole.append(gen_error_text("Ivalid file selections, proccess stopped"))
            self.selectedSourceImage = None
            return

        if not os.path.exists(self.selectedSourceImage) or not os.path.isfile(self.selectedSourceImage):
            self.FaceRecognitionPage.textBrowser_logConsole.append(gen_error_text("Ivalid file selections, proccess stopped"))
            self.selectedSourceImage = None
            return
        
        self.FaceRecognitionPage.textBrowser_logConsole.append(gen_info_text(f"Target file: {self.selectedSourceImage}"))
        self.addImageInWindow_usingFilePath(target_image=self.selectedSourceImage,target_label=self.FaceRecognitionPage.label_soruceImageShower)


    
    def tekilResimEkleme_start(self):
        getNameInput = self.FaceRecognitionPage.lineEdit_singleEklemeKisiAdi.text()
        if len(getNameInput) < 1:
            self.FaceRecognitionPage.textBrowser_singleFaceAddTab_logConsole.append(gen_error_text("En az 1 karakterlik kişi bilgisi gerekir, işlem iptal edildi"))
            return
        
        import cv2
        cv2_image = cv2.imread(self.sistemeEklenecekImageSelected)
        binaryImage = generic_tools.binaryData(self.sistemeEklenecekImageSelected)
        self.FaceRecognitionPage.textBrowser_singleFaceAddTab_logConsole.append(gen_info_text("Seçilen veri işleniyor"))
        eklemeDurumu = self.faceRecDbTools.insertImageFromDB(cv2_image_data=cv2_image,image_binary_data=binaryImage,face_name=getNameInput,insightface_face_analyser_ojb=self.FaceAnalysisUI)
        if eklemeDurumu["success"] != True:
            self.FaceRecognitionPage.textBrowser_singleFaceAddTab_logConsole.append(gen_error_text(f"Ekleme işlemi başarısız oldu sebep: {eklemeDurumu['data']}"))
            return
        
        self.FaceRecognitionPage.textBrowser_singleFaceAddTab_logConsole.append(gen_info_text(str(eklemeDurumu["data"])))
        self.FaceRecognitionPage.textBrowser_singleFaceAddTab_logConsole.append(gen_info_text("Süreç başarıyla tamamlandı"))
        
    
    
    def selectEklenecekResim(self):
        fileSelector = QFileDialog()
        fileSelector.setNameFilter("Image Files (*.jpg *.png *.jpeg *.webm)")
        if fileSelector.exec_():
            self.sistemeEklenecekImageSelected = fileSelector.selectedFiles()[0]

        if self.sistemeEklenecekImageSelected == None:
            self.FaceRecognitionPage.textBrowser_singleFaceAddTab_logConsole.append(gen_error_text("Ivalid file selections, proccess stopped"))
            self.sistemeEklenecekImageSelected = None
            return

        if not os.path.exists(self.sistemeEklenecekImageSelected) or not os.path.isfile(self.sistemeEklenecekImageSelected):
            self.FaceRecognitionPage.textBrowser_singleFaceAddTab_logConsole.append(gen_error_text("Ivalid file selections, proccess stopped"))
            self.sistemeEklenecekImageSelected = None
            return
        
        self.FaceRecognitionPage.textBrowser_singleFaceAddTab_logConsole.append(gen_info_text(f"Target file: {self.sistemeEklenecekImageSelected}"))
        self.addImageInWindow_usingFilePath(target_image=self.sistemeEklenecekImageSelected,target_label=self.FaceRecognitionPage.label_selected_image_show)
    
    
    
    def selectTargetDirectory(self):
        self.targettDir_is_selected = False
        folder_dialog = QFileDialog()
        folder_dialog = QFileDialog.getExistingDirectory(self,"Select Directory")
        if folder_dialog:
            if os.name == "nt":
                check_digit = str(folder_dialog[-2:])
                if not str(os.path.sep) in check_digit:
                    folder_dialog = str(folder_dialog) + str(os.path.sep)
            else:
                check_digit = str(folder_dialog[-1])
                if not str(os.path.sep) in check_digit:
                    folder_dialog = str(folder_dialog) + str(os.path.sep)

        if folder_dialog == None or not os.path.exists(folder_dialog) or not os.path.isdir(folder_dialog):
            self.FaceRecognitionPage.textBrowser_showTargetDir.setText(gen_error_text("Invalid file selections"))
            return
    
        if len(os.listdir(folder_dialog)) == 0:
            self.FaceRecognitionPage.textBrowser_showTargetDir.setText(gen_error_text("elected directory empty"))
            return          
        
        self.selectedDirectory = folder_dialog
        self.targettDir_is_selected = True
        self.FaceRecognitionPage.textBrowser_showTargetDir.setText(folder_dialog)
    
    
        
    def clearLogConsoleTab2(self):
        self.FaceRecognitionPage.textBrowser_cokluEkleme_logConsole.setText("<B>LOG AND RESULTS:</B>")
        
        
        
    def multiAdderThreadSignalHandler(self,data_dict):
        self.FaceRecognitionPage.textBrowser_cokluEkleme_logConsole.append(data_dict["text"])
    
    
    
    def mulitAdderThreadKillSignal(self):
        if not self.MultiAdderThread.isRunning():
            self.FaceRecognitionPage.textBrowser_cokluEkleme_logConsole.append(gen_error_text("No running jobs!"))
            return
        
        self.FaceRecognitionPage.textBrowser_cokluEkleme_logConsole.append(gen_info_text("Sending kill signal..."))
        self.MultiAdderThread.stop()
        
        
        
    def startMultiAdder(self):
        self.clearLogConsoleTab2()
        if self.MultiAdderThread.isRunning():
            self.FaceRecognitionPage.textBrowser_cokluEkleme_logConsole.append(f"<B>ERROR: </B>Ekleme işlemi zaten aktif önce işlemi durdurmanız gerek!")
            return
        
        if self.targettDir_is_selected != True:
            self.FaceRecognitionPage.textBrowser_cokluEkleme_logConsole.append(f"<B>ERROR: </B>Hedef klasör seçilmedi!")
            return
        
        if not os.path.exists(str(self.selectedDirectory)):
            self.FaceRecognitionPage.textBrowser_cokluEkleme_logConsole.append(f"<B>ERROR: </B>Hedef klasör seçilmedi!")
            return    
       
        self.MultiAdderThread = directoryAdderThread(faceAnalayserUI=self.FaceAnalysisUI,targetDirectory=self.selectedDirectory,
            databaseConnections=self.databaseConnections,databaseCursor=self.databaseCursor,mainConfig=self.mainConfig)
        self.MultiAdderThread.statusSignal.connect(self.multiAdderThreadSignalHandler)
        self.MultiAdderThread.start()
        
        
        


    # Veritabanı listeleme ve arama ekranı için olan kısım 
    
    def updateManuelSearchLineEdit(self):
        getCurrentIndex = self.FaceRecognitionPage.comboBox_targetColumn.currentIndex()
        self.FaceRecognitionPage.lineEdit_searchInput.setDisabled(getCurrentIndex==2)
        
    
    def stopActivaManuelSearch(self):
        if not self.manuelSearchThread.isRunning():
            self.FaceRecognitionPage.textBrowser_ManuelSearchLogConsole.append(gen_error_text("Durdurulacak aktif bir arama işlemi yoktur"))
            return
        
        self.manuelSearchThread.quit()
        self.manuelSearchThread.wait()
        self.FaceRecognitionPage.textBrowser_ManuelSearchLogConsole.append(gen_info_text("Aktif arama işlemi kullanıcı tarafından sonlandırıldı"))
    
    
    def clear_all_manuel_search_output(self):
        self.FaceRecognitionPage.textBrowser_ManuelSearchLogConsole.setText(f"<B>LOG CONSOLE:</B>")
        self.FaceRecognitionPage.tableWidget_resultTable.clearContents()
        self.FaceRecognitionPage.tableWidget_resultTable.setRowCount(0)
        self.showDefaultImage(self.FaceRecognitionPage.label_dbManuelSearchImageShower)
        
    
    def table_widget_signal_handler(self,row,column):
        if column == 1:
            db_id = self.FaceRecognitionPage.tableWidget_resultTable.item(row,0).text()
            image_data = get_image_from_id(self.databaseCursor,db_id=int(db_id))
            if image_data["success"] != True:
                self.FaceRecognitionPage.textBrowser_ManuelSearchLogConsole.append(gen_error_text(f"Resim ekrana getirilemedi: {image_data['data']}"))
                return
            self.show_cv2_image_target_label(image_data=image_data["data"],targetLabel=self.FaceRecognitionPage.label_dbManuelSearchImageShower)
            
            
            
    def manuel_database_search_thread_signal_handler(self,thread_dict):
        results = thread_dict
        
        if results["success"] == None and results["end"] == False:
            self.FaceRecognitionPage.textBrowser_ManuelSearchLogConsole.append(str(results["text"]))
            return
        
        if results["success"] == False and results["end"] == True:
            self.FaceRecognitionPage.textBrowser_ManuelSearchLogConsole.append(str(results["text"]))
            return
        
        if results["success"] == True and results["end"] == True:
            self.FaceRecognitionPage.textBrowser_ManuelSearchLogConsole.append(str(results["text"]))
            result_data = results["data"]
            self.FaceRecognitionPage.tableWidget_resultTable.setRowCount(len(result_data))
            currentLine = 0
            
            for single_row in result_data:
                database_id = single_row[0]
                face_image_text = "tıkla ve görüntüle"
                image_hash = single_row[2]
                face_name = single_row[6]
                add_date = single_row[7]
                add_date = str(add_date)
                
                
                self.FaceRecognitionPage.tableWidget_resultTable.setItem(currentLine,0,QTableWidgetItem(str(database_id)))
                self.FaceRecognitionPage.tableWidget_resultTable.setItem(currentLine,1,QTableWidgetItem(face_image_text))
                self.FaceRecognitionPage.tableWidget_resultTable.setItem(currentLine,2,QTableWidgetItem(image_hash))
                self.FaceRecognitionPage.tableWidget_resultTable.setItem(currentLine,3,QTableWidgetItem(face_name))
                self.FaceRecognitionPage.tableWidget_resultTable.setItem(currentLine,4,QTableWidgetItem(add_date))
                currentLine += 1
            
    
    
    def start_manuel_database_search(self):
        currentSearchType = self.FaceRecognitionPage.comboBox_targetColumn.currentIndex()
        currentSearchString = self.FaceRecognitionPage.lineEdit_searchInput.text()
        
        if len(currentSearchString) == 0 and currentSearchType != 2:
            self.FaceRecognitionPage.textBrowser_ManuelSearchLogConsole.append(gen_error_text("Geçerli bir arama terimi girilmedi, işlem iptal edildi"))
            return
        
        self.manuelSearchThread = manuelDatabaseSearcherThread(db_cnn=self.databaseConnections,db_curosr=self.databaseCursor,search_keywords=currentSearchString,selected_search=currentSearchType)
        self.manuelSearchThread.threadSignal.connect(self.manuel_database_search_thread_signal_handler)
        self.manuelSearchThread.start()
        
    def save_current_image(self):
        
        getCurrentLine = self.FaceRecognitionPage.tableWidget_resultTable.currentRow()
        getCurrentColumn = self.FaceRecognitionPage.tableWidget_resultTable.currentColumn()
        if getCurrentLine < 0 and getCurrentColumn != 1:
            self.FaceRecognitionPage.textBrowser_ManuelSearchLogConsole.append(gen_error_text("Kaydedilecek resmin üzerine tıklayınız önce."))
            return
        
        db_id = self.FaceRecognitionPage.tableWidget_resultTable.item(getCurrentLine,0).text()
        faceNmae = self.FaceRecognitionPage.tableWidget_resultTable.item(getCurrentLine,3).text()
        image_data = get_image_from_id(self.databaseCursor,db_id=int(db_id))
        
        if image_data["success"] != True:
            self.FaceRecognitionPage.textBrowser_ManuelSearchLogConsole.append(gen_error_text(f"Resim kaydedilemedi: {image_data['data']}"))
            return
        
        file_path = DEFAULT_ROOT_DIR_NAME + str(os.path.sep) + str(faceNmae)+".png"
        with open(file_path,"wb") as targetFile:
            targetFile.write(image_data["data"])
        
        self.FaceRecognitionPage.textBrowser_ManuelSearchLogConsole.append(gen_info_text(f"Resim başarıyla dışa aktarıldı, {file_path}"))
        
