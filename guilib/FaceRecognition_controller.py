from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtGui

from guilib.FaceRecognitionScreen import Ui_FaceRecognitionWidget
from guilib.html_text_generator.html_draft import gen_error_text,gen_info_text

from hivelibrary.env import DEFAULT_LOGO_PATH


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
    def __init__(self):
        super().__init__()
        
        self.FaceRecognitionPage = Ui_FaceRecognitionWidget()
        self.FaceRecognitionPage.setupUi(self)
        
        self.setWindowTitle("Face Recognition For Database")
        
        self.LabelSupportedResulation = (320, 320)
        
        self.showDefaultImage(targetLabel=self.FaceRecognitionPage.label_soruceImageShower)
        self.showDefaultImage(targetLabel=self.FaceRecognitionPage.label_detectedImageShower)
        
        
        
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