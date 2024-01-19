from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtGui

from guilib.FaceRecognitionScreen import Ui_FaceRecognitionWidget
from guilib.html_text_generator.html_draft import gen_error_text,gen_info_text
from guilib.external_thread_modules.FaceRecognitionDirectoryTransfer import directoryAdderThread

from hivelibrary.console_tools import InformationPrinter
from hivelibrary.env import DEFAULT_LOGO_PATH,DB_FACE_RECOGNITION_TABLE,DEFAULT_TEMP_DIR
from hivelibrary.face_recognition_database_tools import recognitionDbTools
from hivelibrary.file_operations import generic_tools


import os
import sqlite3

class faceRecognitionBackendThread(QThread):
    
    statusSignal = pyqtSignal(dict)
    """Dict types
    success -> bool
    text    -> status text
    cv2_image -> raw image
    face_name -> name from db
    add date -> date from db UTC
    similarity -> similartiy rate
    
    
    """
    
    
    def __init__(self, targetFaceImagePath:str, faceAnalayserUI:object, db_curosr:sqlite3.Cursor,):
        super().__init__()
        
        self.databaseCursor = db_curosr
        self.targetImagePath = targetFaceImagePath
        self.faceAnalayserUI = faceAnalayserUI
        self.threadStopSignal = False
        self.minSimilarity = 30
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
        
        self.__runningStatusReturner(text="Veritabanı kontrol ediliyor")
        rsults = self.databaseCursor.execute(f"SELECT COUNT(*) FROM {DB_FACE_RECOGNITION_TABLE}").fetchall()[0][0]
        
        if int(rsults) < 1:
            self.__finalyStatusReturner(text=gen_error_text("Veritabanı boş, arama yapmak için önce veritabanına ekleme yapınız"),
                success_status=False,)
            return 
        
        if len(analysedSourceImage) > 1:
            self.__finalyStatusReturner(text=gen_error_text("Kaynak resimde 1 den fazla yüz kabul edilemez"),
                success_status=False,)
            return

        if len(analysedSourceImage) == 0:
            self.__finalyStatusReturner(text=gen_error_text("Kaynak resimde herhangi bir yüz bulunamadı"),
                success_status=False,)
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
            self.__finalyStatusReturner(text=gen_error_text(f"%{self.minSimilarity} veya daha yüksek bir oranda eşleşme bulunamadı sistemde"),
                success_status=False,)
            return
        
        #self.__runningStatusReturner(text=f"%30 ve üzeri eşleşme veren id ler ve oranları {str(self.similartiyStorageDcit)}")
        
        self.__runningStatusReturner(text="arama tamamlandı sonuçlar işleniyor")
        
        if len(self.similartiyStorageDcit) < 1:
            self.__finalyStatusReturner(text=gen_error_text("Veritabanında kişiye benzer birisi bulunamadı."),
                success_status=False,cv2_image=None,face_name="Failed To detec")
            return
        
        enBenzerID = max(list(self.similartiyStorageDcit.values()))
        enYuksekBenzerlik = enBenzerID
        
        for key, value in self.similartiyStorageDcit.items():
            if value == enYuksekBenzerlik:
                enBenzerID = key
        
        STATIC_SQL_COMMAND = f"SELECT * FROM {DB_FACE_RECOGNITION_TABLE} WHERE id=?"
        STATIC_DATA_TUPLE = (enBenzerID,)
        
        results = self.databaseCursor.execute(STATIC_SQL_COMMAND,STATIC_DATA_TUPLE).fetchall()[0]
        
        detectedFaceSimilartiyRate = self.similartiyStorageDcit[enBenzerID]
        detectedFaceDatabaseID= enBenzerID
        detectedFacePictur = results[1]
        detectedFacePictureHash = results[2]
        #detectedFace2Dlandmakrs = numpy.frombuffer(results[4],dtype=numpy.float32)
        #detectedFaceFaceBox = numpy.frombuffer(results[5],dtype=numpy.float32)
        detectedFaceName = results[6]
        detectedFaceAddDate = results[8]

        return_text = f"""<B>Bulunan Eşleşme Bilgileri: </B><br>
<B>Kişinin kayıtlı adı:</B> {detectedFaceName}<br>
<B>Benzerlik oranı: </B> %{enYuksekBenzerlik}<br>
<B>Veritabanı ID: </B>{detectedFaceDatabaseID}<br>
<B>Resim sha1 hash'i: </B> {detectedFacePictureHash}<br>
<B>Veritabanına eklenme tarihi UTC: </B> {detectedFaceAddDate}<br>
<B>{"-"*20}<B/><br>"""


        self.__finalyStatusReturner(text=return_text,success_status=True,cv2_image=detectedFacePictur,face_name=detectedFaceName,similartiy=detectedFaceSimilartiyRate)

class FaceRecognitionWidget(QWidget):
    def __init__(self, db_cnn:sqlite3.Connection, db_curosr:sqlite3.Cursor):
        super().__init__()
        
        self.FaceRecognitionPage = Ui_FaceRecognitionWidget()
        self.FaceRecognitionPage.setupUi(self)

        self.setWindowTitle("Face Recognition From Image")
        
        self.LabelSupportedResulation = (320, 320)
        
        self.showDefaultImage(targetLabel=self.FaceRecognitionPage.label_soruceImageShower)
        self.showDefaultImage(targetLabel=self.FaceRecognitionPage.label_detectedImageShower)
        self.showDefaultImage(targetLabel=self.FaceRecognitionPage.label_selected_image_show)
        
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
        
        self.DatabaseSearchThread = QThread()
        self.MultiAdderThread = QThread()
        
        self.MultiAdderActive = False
        
        self.databaseConnections = db_cnn
        self.databaseCursor = db_curosr
        self.selectedDirectory = None
        self.targettDir_is_selected = True
        
        InformationPrinter(f"importing insightFace")
        import insightface

        InformationPrinter(f"initing face detection system")
        self.FaceAnalysisUI = insightface.app.FaceAnalysis() 
        self.FaceAnalysisUI.prepare(ctx_id=-1,det_thresh=0.5)
        InformationPrinter("Face detection system succesfully init")
        
        InformationPrinter("initing FaceRecognitionDatabaseTools")
        self.faceRecDbTools = recognitionDbTools(db_cnn=self.databaseConnections,db_curosr=self.databaseCursor)        
        InformationPrinter("FaceRecognitionDatabaseTools successfuly init")
        
    def threadSignalHandler(self,thread_dict):
        if thread_dict["success"] == None and thread_dict["end"] == False:
            self.FaceRecognitionPage.textBrowser_logConsole.append(gen_info_text(str(thread_dict["text"])))
            return
        
        if thread_dict["success"] != True and thread_dict["end"] == True:
            self.FaceRecognitionPage.textBrowser_logConsole.append(gen_error_text(str(thread_dict["text"])))
            return
        
        if thread_dict["success"] == True and thread_dict["end"] == True:
            self.FaceRecognitionPage.textBrowser_logConsole.append(str(thread_dict["text"]))
            self.FaceRecognitionPage.progressBar_benzerlikBari.setValue(thread_dict["similartiy"])
            self.show_cv2_image_target_label(image_data=thread_dict["cv2_image"],targetLabel=self.FaceRecognitionPage.label_detectedImageShower)
        
    def sendKillSignalThread(self):
        if not self.DatabaseSearchThread.isRunning():
            err_msg = "<B>ERROR: </B>No running jobs!"
            self.FaceRecognitionPage.textBrowser_logConsole.append(err_msg)
            return
        
        
        info_msg = "<B>INFO: </B>Sending kill signal..."
        self.FaceRecognitionPage.textBrowser_logConsole.append(info_msg)
        self.DatabaseSearchThread.stop()
    
    def startDatabaseSearch(self):
        
        if self.selectedSourceImage == None :
            self.FaceRecognitionPage.textBrowser_logConsole.append(
                gen_error_text("Kaynak resim seçilmedi, işlem iptal edildi"))
            return
        
        self.FaceRecognitionPage.textBrowser_logConsole.append(gen_info_text("Veritabanı araması başlaılıyor"))
        
        self.DatabaseSearchThread = faceRecognitionBackendThread(
            targetFaceImagePath=self.selectedSourceImage,faceAnalayserUI=self.FaceAnalysisUI,db_curosr=self.databaseCursor
        )
        self.DatabaseSearchThread.statusSignal.connect(self.threadSignalHandler)
        self.DatabaseSearchThread.start()

        
        """
        # Thread reference code
        self.backEndWorkerThread = FaceVerificationBackendThread(
            sourceImagePath=self.selectedSourceImage, targetImagePath=self.selectedTargetImage
        )
        self.backEndWorkerThread.statusSignal.connect(self.threadSignalHandler)
        self.backEndWorkerThread.start()
        
        """
        
        
        
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
    
    
    def detectAndDraw(self, cv2_image, target_label):
        pass
    
    def tekilResimEkleme_start(self):
        getNameInput = self.FaceRecognitionPage.lineEdit_singleEklemeKisiAdi.text()
        if len(getNameInput) < 1:
            self.FaceRecognitionPage.textBrowser_singleFaceAddTab_logConsole.append(gen_error_text("En az 1 karakterlik kişi bilgisi gerekir, işlem iptal edildi"))
            return
        
        import cv2
        cv2_image = cv2.imread(self.sistemeEklenecekImageSelected)
        binaryImage = generic_tools.binaryData(self.sistemeEklenecekImageSelected)
        
        self.FaceRecognitionPage.textBrowser_singleFaceAddTab_logConsole.append(gen_info_text("Seçilen veri işleniyor"))
        eklemeDurumu = self.faceRecDbTools.insertImageFromDB(
            cv2_image_data=cv2_image,
            image_binary_data=binaryImage,
            face_name=getNameInput,
            insightface_face_analyser_ojb=self.FaceAnalysisUI
        )
        
        if eklemeDurumu["success"] != True:
            self.FaceRecognitionPage.textBrowser_singleFaceAddTab_logConsole.append(gen_error_text(f"Ekleme işlemi başarısız oldu sebep: {eklemeDurumu['data']}"))
            return
        
        self.FaceRecognitionPage.textBrowser_singleFaceAddTab_logConsole.append(
            gen_info_text(str(eklemeDurumu["data"]))
        )
        
        self.FaceRecognitionPage.textBrowser_singleFaceAddTab_logConsole.append(
            gen_info_text("Süreç başarıyla tamamlandı")
        )
        
    
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
            err_msg = "Error: Invalid file selections"
            self.FaceRecognitionPage.textBrowser_showTargetDir.setText(err_msg)
            return
        
        if len(os.listdir(folder_dialog)) == 0:
            err_msg = "Error: Selected directory empty"
            self.FaceRecognitionPage.textBrowser_showTargetDir.setText(err_msg)
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
            err_msg = "<B>ERROR: </B>No running jobs!"
            self.FaceRecognitionPage.textBrowser_cokluEkleme_logConsole.append(err_msg)
            return
        
        
        info_msg = "<B>INFO: </B>Sending kill signal..."
        self.FaceRecognitionPage.textBrowser_cokluEkleme_logConsole.append(info_msg)
        self.MultiAdderThread.stop()
        self.MultiAdderActive = False
        
    def startMultiAdder(self):
        self.clearLogConsoleTab2()
        
        if self.MultiAdderActive == True:
            self.FaceRecognitionPage.textBrowser_cokluEkleme_logConsole.append(f"<B>ERROR: </B>Ekleme işlemi zaten aktif önce işlemi durdurmanız gerek!")
            return
        
        if self.targettDir_is_selected != True:
            self.FaceRecognitionPage.textBrowser_cokluEkleme_logConsole.append(f"<B>ERROR: </B>Hedef klasör seçilmedi!")
            return
        
        if not os.path.exists(str(self.selectedDirectory)):
            self.FaceRecognitionPage.textBrowser_cokluEkleme_logConsole.append(f"<B>ERROR: </B>Hedef klasör seçilmedi!")
            return    
        
        self.MultiAdderActive = True
        self.MultiAdderThread = directoryAdderThread(faceAnalayserUI=self.FaceAnalysisUI,targetDirectory=self.selectedDirectory,
            databaseConnections=self.databaseConnections,databaseCursor=self.databaseCursor)
        
        self.MultiAdderThread.statusSignal.connect(self.multiAdderThreadSignalHandler)
        
        self.MultiAdderThread.start()