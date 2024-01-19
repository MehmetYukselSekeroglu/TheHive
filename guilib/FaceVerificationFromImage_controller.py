from guilib.FaceVerificationScreen_from_image import Ui_FaceVerificationWidget
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtGui

from hivelibrary.env import DEFAULT_LOGO_PATH
from guilib.html_text_generator.html_draft import *

import os


class FaceVerificationBackendThread(QThread):
    statusSignal = pyqtSignal(dict)
    
    def __init__(self, sourceImagePath:str, targetImagePath:str):
        super().__init__()

        self.detectModelDefaultResulation = (640,640)
        self.labelDefaultResulation =(320,320)
        self.sourceImagePath = sourceImagePath
        self.targetImagePath = targetImagePath

    def __runningStatusReturner(self, text:str):
        data_dict = { "end":False, "success":None, "text":text, "verification":None, "img_1":None, "img_2":None, "result":None }
        self.statusSignal.emit(data_dict)
    
    def __finalyStatusReturner(self, text:str, success_status=True,image_1=None, image_2=None, verification=None, result=None ):
        data_dict = { "end":True, "success":success_status, "text":text, "verification":verification, "img_1":image_1, "img_2":image_2, "result":result }
        self.statusSignal.emit(data_dict)
        
    def run(self):
        self.__runningStatusReturner(text=gen_info_text("Arkaplan thread'ı başlatıldı, gereksinimler içe aktarılıyor"))
        import cv2
        import insightface
        import numpy as np
        from hivelibrary.ImageTools.opencv_tools import landmarks_rectangle, landmarks_rectangle_2d
        
        faceAnalayserUI = insightface.app.FaceAnalysis()
        faceAnalayserUI.prepare(ctx_id=-1,det_thresh=0.5)
        
        self.__runningStatusReturner(text=gen_info_text("Yüz tespit sistemi CPU üzerinden çalışacak şekilde ayarlandı"))
        self.__runningStatusReturner(text=gen_info_text("Resimler openCV ile okunuyor"))


        originalSourceImageData = cv2.imread(self.sourceImagePath)
        originalTargetImageData = cv2.imread(self.targetImagePath)
        
        self.__runningStatusReturner(text=gen_info_text("Kaynak resim analizi başlatıldı"))
        analysedSourceImage = faceAnalayserUI.get(originalSourceImageData)
        
        if len(analysedSourceImage) > 1:
            self.__finalyStatusReturner(text=gen_error_text("Kaynak resimde 1 den fazla yüz kabul edilemez"),
success_status=False,)
            return

        self.__runningStatusReturner(text=gen_info_text("Hedef resim analizi başlatıldı"))
        analysedTargetImage = faceAnalayserUI.get(originalTargetImageData)
        
        if len(analysedSourceImage) == 0:
            self.__finalyStatusReturner(text=gen_error_text("Kaynak resimde herhangi bir yüz bulunamadı"),success_status=False,)
            return            

        if len(analysedTargetImage) == 0:
            self.__finalyStatusReturner(text=gen_error_text("Hedef resimde herhangi bir yüz bulunamadı"),success_status=False,)
            return          
        
        if len(analysedTargetImage) > 1:
            self.__finalyStatusReturner(text=gen_error_text("Bu sürümde hedef resim 1 den fazla yüzü desteklemez"),success_status=False,)
            return

        
        self.__runningStatusReturner(text=gen_info_text("Tespit işlemi tamamlandı, veriler analiz ediliyor"))

        face_embedding_sourceFile = analysedSourceImage[0]["embedding"]
        face_embedding_targetFile = analysedTargetImage[0]["embedding"]
        

        self.__runningStatusReturner(text=gen_info_text("Benzerlik oranı hesaplanıyor"))


        dot_product_size = np.dot(face_embedding_sourceFile, face_embedding_targetFile)
        norm_sound1 = np.linalg.norm(face_embedding_sourceFile)
        norm_sound2 = np.linalg.norm(face_embedding_targetFile)

        # kosinus benzerliğini hesaplama 
        GetSimilarity = dot_product_size / (norm_sound1 * norm_sound2)
        GetSimilarity = GetSimilarity * 100
        GetSimilarity = int(GetSimilarity)
        
        self.__runningStatusReturner(text=gen_info_text("Resimler hazırlanıyor"))


        originalSourceImageData = cv2.cvtColor(originalSourceImageData,cv2.COLOR_BGR2RGB)
        originalTargetImageData = cv2.cvtColor(originalTargetImageData,cv2.COLOR_BGR2RGB)
        
        
        originalSourceImageData = landmarks_rectangle(originalSourceImageData,data_list=analysedSourceImage[0]["bbox"])
        originalSourceImageData = landmarks_rectangle_2d(originalSourceImageData, data_list=analysedSourceImage[0]["landmark_2d_106"])
        
        originalTargetImageData = landmarks_rectangle(originalTargetImageData,data_list=analysedTargetImage[0]["bbox"])
        originalTargetImageData = landmarks_rectangle_2d(originalTargetImageData, data_list=analysedTargetImage[0]["landmark_2d_106"])
        
        if GetSimilarity < 0:
            GetSimilarity = 0
        
        final_text = f"""<B>{"-"*20}</B><br>
Benzerlik Oranı: %{GetSimilarity}<br>
<B>{"-"*20}</B><br>"""
        self.__finalyStatusReturner(text=final_text,success_status=True,image_1=originalSourceImageData, image_2=originalTargetImageData
            ,verification=GetSimilarity,)
        
        
class FaceVerificationScreen_from_image(QWidget):
    def __init__(self):
        super().__init__()
        
        self.detectModelDefaultResulation = (640,640)
        self.labelDefaultResulation =(320,320)
        
        self.FaceVerificationFromImage = Ui_FaceVerificationWidget()
        self.FaceVerificationFromImage.setupUi(self)
        
        self.setWindowTitle("Face Verification")
        self.showDefaultImage(targetLabel=self.FaceVerificationFromImage.label_sourceImage)
        self.showDefaultImage(targetLabel=self.FaceVerificationFromImage.label_targetImage)
        
        
        self.selectedSourceImage = None
        self.selectedTargetImage = None

        self.FaceVerificationFromImage.pushButton_removeSourceImage.clicked.connect(self.removeSourceImage)
        self.FaceVerificationFromImage.pushButton_removeTargetImage.clicked.connect(self.removeTargetImage)
        self.FaceVerificationFromImage.pushButton_selectSourceImage.clicked.connect(self.selectSourceImage)
        self.FaceVerificationFromImage.pushButton_selectTargetImage.clicked.connect(self.selectTargetImage)
        self.FaceVerificationFromImage.pushButton_startVerification.clicked.connect(self.startVerification)





    def threadSignalHandler(self, data_dict):
        if data_dict["end"] == True and data_dict["success"] == False:
            self.FaceVerificationFromImage.textBrowser_logConsole.append(str(data_dict["text"]))            
            return
        
        if data_dict["end"] == False and data_dict["success"] == None:
            self.FaceVerificationFromImage.textBrowser_logConsole.append(str(data_dict["text"]))            
            return
        
        if data_dict["end"] == True and data_dict["success"] == True:
            
            import cv2
            self.FaceVerificationFromImage.textBrowser_logConsole.append(str(data_dict["text"]))      
            siimilarity_rate = data_dict["verification"]

            self.FaceVerificationFromImage.progressBar_similarityBar.setValue(siimilarity_rate)
            
            img_height, img_width = self.labelDefaultResulation
            image_data_1 = data_dict["img_1"]
            image_data_1 = cv2.resize(image_data_1,self.labelDefaultResulation)
            image_data_1 = QtGui.QImage(image_data_1, img_width, img_height,QtGui.QImage.Format.Format_RGB888)
            self.FaceVerificationFromImage.label_sourceImage.setPixmap(QtGui.QPixmap.fromImage(image_data_1))
        
            image_data_2 = data_dict["img_2"]
            image_data_2 = cv2.resize(image_data_2,self.labelDefaultResulation)
            image_data_2 = QtGui.QImage(image_data_2, img_width, img_height,QtGui.QImage.Format.Format_RGB888)
            self.FaceVerificationFromImage.label_targetImage.setPixmap(QtGui.QPixmap.fromImage(image_data_2))
        
        """
        image_data = cv2.resize(image_data, self.labelDefaultResulation)
        image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
        img_height, img_width = self.labelDefaultResulation
        image_data = QtGui.QImage(image_data, img_width, img_height,QtGui.QImage.Format.Format_RGB888)
        target_label.setPixmap(QtGui.QPixmap.fromImage(image_data))
        """
            
    def selectSourceImage(self):
        fileSelector = QFileDialog()
        fileSelector.setNameFilter("Image Files (*.jpg *.png *.jpeg *.webm)")
        
        if fileSelector.exec_():
            self.selectedSourceImage = fileSelector.selectedFiles()[0]

        if self.selectedSourceImage == None:
            self.FaceVerificationFromImage.textBrowser_logConsole.append(gen_error_text("Ivalid file selections, proccess stopped"))
            self.selectedSourceImage = None
            return

        if not os.path.exists(self.selectedSourceImage) or not os.path.isfile(self.selectedSourceImage):
            self.FaceVerificationFromImage.textBrowser_logConsole.append(gen_error_text("Ivalid file selections, proccess stopped"))
            self.selectedSourceImage = None
            return
        
        
        self.FaceVerificationFromImage.textBrowser_logConsole.append(gen_info_text(f"Target file: {self.selectedSourceImage}"))
        self.addImageInWindow_usingFilePath(target_image=self.selectedSourceImage,target_label=self.FaceVerificationFromImage.label_sourceImage)
    
    def selectTargetImage(self):
        fileSelector = QFileDialog()
        fileSelector.setNameFilter("Image Files (*.jpg *.png *.jpeg *.webm)")
        
        if fileSelector.exec_():
            self.selectedTargetImage = fileSelector.selectedFiles()[0]

        if self.selectedTargetImage == None:
            self.FaceVerificationFromImage.textBrowser_logConsole.append(gen_error_text("Ivalid file selections, proccess stopped"))
            self.selectedTargetImage = None
            return

        if not os.path.exists(self.selectedTargetImage) or not os.path.isfile(self.selectedTargetImage):
            self.FaceVerificationFromImage.textBrowser_logConsole.append(gen_error_text("Ivalid file selections, proccess stopped"))
            self.selectedTargetImage = None
            return
        
        self.FaceVerificationFromImage.textBrowser_logConsole.append(gen_info_text(f"Target file: {self.selectedTargetImage}"))
        self.addImageInWindow_usingFilePath(target_image=self.selectedTargetImage,target_label=self.FaceVerificationFromImage.label_targetImage)
    
    def startVerification(self):
        if self.selectedTargetImage == None or self.selectedSourceImage == None:
            self.FaceVerificationFromImage.textBrowser_logConsole.append(
                gen_error_text("Kaynak resim veya hedef resim seçilmedi, işlem iptal edildi"))
            return
        
        self.backEndWorkerThread = FaceVerificationBackendThread(
            sourceImagePath=self.selectedSourceImage, targetImagePath=self.selectedTargetImage
        )
        self.backEndWorkerThread.statusSignal.connect(self.threadSignalHandler)
        self.backEndWorkerThread.start()
    
    
    def removeSourceImage(self):
        if self.selectedSourceImage != None:
            self.selectedSourceImage = None
            self.showDefaultImage(targetLabel=self.FaceVerificationFromImage.label_sourceImage)
            self.FaceVerificationFromImage.textBrowser_logConsole.append(gen_info_text("Kaynak resim kaldırıldı"))
            return
        self.FaceVerificationFromImage.textBrowser_logConsole.append(gen_error_text("Kaynak resim zaten seçili değil"))

    def removeTargetImage(self):
        if self.selectedTargetImage != None:
            self.selectedTargetImage = None
            self.showDefaultImage(targetLabel=self.FaceVerificationFromImage.label_targetImage)
            self.FaceVerificationFromImage.textBrowser_logConsole.append(gen_info_text("Hedef resim kaldırıldı"))
            return
        
        self.FaceVerificationFromImage.textBrowser_logConsole.append(gen_error_text("Hedef resim zaten seçili değil"))

    def showDefaultImage(self, targetLabel):
        import cv2
        
        image_data = cv2.imread(DEFAULT_LOGO_PATH)
        image_data = cv2.resize(image_data, self.labelDefaultResulation)
        image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
        img_height, img_width = self.labelDefaultResulation
        image_data = QtGui.QImage(image_data, img_width, img_height,QtGui.QImage.Format.Format_RGB888)
        targetLabel.setPixmap(QtGui.QPixmap(image_data))

    def addImageInWindow_usingFilePath(self,target_image,target_label):
        import cv2
        image_data = cv2.imread(target_image)
        image_data = cv2.resize(image_data, self.labelDefaultResulation)
        image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
        img_height, img_width = self.labelDefaultResulation
        image_data = QtGui.QImage(image_data, img_width, img_height,QtGui.QImage.Format.Format_RGB888)
        target_label.setPixmap(QtGui.QPixmap.fromImage(image_data))
        

