from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtGui

from guilib.FaceRecognitionScreen import Ui_FaceRecognitionWidget
from guilib.html_text_generator.html_draft import gen_error_text,gen_info_text

from hivelibrary.console_tools import InformationPrinter
from hivelibrary.env import DEFAULT_LOGO_PATH
from hivelibrary.face_recognition_database_tools import recognitionDbTools
from hivelibrary.file_operations import generic_tools
import os
import sqlite3

class faceRecognitionBackendThread(QThread):
    
    statusSignal = pyqtSignal(dict)
    
    
    def __init__(self):
        super().__init__()
        
    
    def __runningStatusReturner(self, text:str):
        pass
    
    def __finalyStatusReturner(self,text:str):
        pass
    
    def run(self):
        pass    
        
    



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
        
        
        self.FaceRecognitionPage.pushButton_tab2_resim_sec.clicked.connect(self.selectEklenecekResim)
        self.FaceRecognitionPage.pushButton_tab2_sistemeEkle.clicked.connect(self.tekilResimEkleme_start)
        
        self.databaseConnections = db_cnn
        self.databaseCursor = db_curosr

        
        InformationPrinter(f"importing insightFace")
        import insightface

        InformationPrinter(f"initing face detection system")
        self.FaceAnalysisUI = insightface.app.FaceAnalysis() 
        self.FaceAnalysisUI.prepare(ctx_id=-1,det_thresh=0.5)
        InformationPrinter("Face detection system succesfully init")
        
        InformationPrinter("initing FaceRecognitionDatabaseTools")
        self.faceRecDbTools = recognitionDbTools(db_cnn=self.databaseConnections,db_curosr=self.databaseCursor)        
        InformationPrinter("FaceRecognitionDatabaseTools successfuly init")
        
    def sendKillSignalThread(self):
        pass
    
    def startDatabaseSearch(self):
        pass
        
    def showDefaultImage(self, targetLabel):
        import cv2
        image_data = cv2.imread(DEFAULT_LOGO_PATH)
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
    