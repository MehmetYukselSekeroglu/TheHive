from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtGui
import os
from guilib.FaceDetectionScreen import Ui_FaceDetectionOnly
from guilib.html_text_generator import html_draft
from hivelibrary.env import DEFAULT_LOGO_PATH


class faceDetectionBackendThread(QThread):
    
    statusSignal = pyqtSignal(dict)
    
    """
    dict type for statusSignal:
    
    {
        "end": bool,
        "success": bool or None,
        "text": "proccess x is running now" ,
        
        # if proccess succesfuly complated and face detected in image
        "face_data": return for face data,
        "cv2_image": for showing screen,
    }
    
    """
    
    
    
    def __init__(self, targetFilePath:str):
        super().__init__()
        
        self.targetFilePath = targetFilePath
    
    
    def __runningStatusReturner(self, text:str):
        dict_is = {"end": False,"success":None,"text":text,}
        self.statusSignal.emit(dict_is)
        
    def __finalyStatusReturner(self, text:str, success_status=True,face_data=None, cv2_image=None ):
        dict_is = {
            "end":True,
            "success":success_status,
            "text":text,
            "face_data":face_data,
            "cv2_image": cv2_image
        }
        self.statusSignal.emit(dict_is)
    
    
    
    def run(self):
        self.__runningStatusReturner(text=html_draft.gen_info_text("Gereksinim içe aktarması başlatıldı"))
        import cv2
        import insightface
        from hivelibrary.ImageTools.opencv_tools import landmarks_rectangle, landmarks_rectangle_2d

        faceAnalayserUI = insightface.app.FaceAnalysis()
        faceAnalayserUI.prepare(ctx_id=-1)
        
        self.__runningStatusReturner(text=html_draft.gen_info_text("Yüz tespit sistemi CPU üzerinden çalışacak şekilde ayarlandı"))
        self.__runningStatusReturner(text=html_draft.gen_info_text("Resim openCV ile okunuyor"))
        
        original_image_data = cv2.imread(self.targetFilePath)

        self.__runningStatusReturner(text=html_draft.gen_info_text("Resim analizi başlatıldı"))
        analysedImage = faceAnalayserUI.get(original_image_data)
        
        if len(analysedImage) < 1:
            
            self.__finalyStatusReturner(text=html_draft.gen_error_text("Resimde herhangi bir yüz bulunamadı.")
                ,success_status=False,face_data=None,cv2_image=None)
            return
        
        
        self.__runningStatusReturner(text=html_draft.gen_info_text(f"Resim içinde {len(analysedImage)} yüz bulundu işleniyor"))
        
        currentFace = 0
        for single_face_data in analysedImage:
            self.__runningStatusReturner(html_draft.gen_info_text(f"İşlenen yüz numarası: {currentFace}"))
            kareList = single_face_data["bbox"]
            noktaList = single_face_data["landmark_2d_106"]
            original_image_data = landmarks_rectangle(original_image_data,kareList)
            original_image_data = landmarks_rectangle_2d(original_image_data,noktaList)
            currentFace+=1
        
        
        self.__finalyStatusReturner(text=html_draft.gen_info_text("İşlem başarıyla tamamlandı"),
            success_status=True,face_data=analysedImage,cv2_image=original_image_data)
        






class FaceDetectionWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        
        self.detectModelDefaultResulation = (640,640)
        
        self.FaceDetectionPage = Ui_FaceDetectionOnly()
        self.FaceDetectionPage.setupUi(self)
        self.setWindowTitle("Face Detection")
        
        
        self.selectedTargetImageFile = None
        self.showDefaultImage()                            
        self.FaceDetectionPage.pushButton_selectImage.clicked.connect(self.selectTargetImage)
        self.FaceDetectionPage.pushButton_runDetection.clicked.connect(self.startDetectionProccess)
        self.FaceDetectionPage.pushButton_clearLogConsole.clicked.connect(self.clearLogConsole)
        
    
    
    def showDefaultImage(self):
        import cv2
        
        image_data = cv2.imread(DEFAULT_LOGO_PATH)
        image_data = cv2.resize(image_data, self.detectModelDefaultResulation)
        image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
        img_height, img_width = self.detectModelDefaultResulation
        image_data = QtGui.QImage(image_data, img_width, img_height,QtGui.QImage.Format.Format_RGB888)
        self.FaceDetectionPage.label_showImage.setPixmap(QtGui.QPixmap(image_data))
 
    def selectTargetImage(self):
        fileSelector = QFileDialog()
        fileSelector.setNameFilter("Image Files (*.jpg *.png *.jpeg *.webm)")
        
        if fileSelector.exec_():
            self.selectedTargetImageFile = fileSelector.selectedFiles()[0]

        if self.selectedTargetImageFile == None:
            self.FaceDetectionPage.textBrowser_logConsole.append(html_draft.gen_error_text("Ivalid file selections, proccess stopped"))
            self.selectedTargetImageFile = None
            return

        if not os.path.exists(self.selectedTargetImageFile) or not os.path.isfile(self.selectedTargetImageFile):
            self.FaceDetectionPage.textBrowser_logConsole.append(html_draft.gen_error_text("Ivalid file selections, proccess stopped"))
            self.selectedTargetImageFile = None
            return
        
        
        self.FaceDetectionPage.textBrowser_logConsole.append(html_draft.gen_info_text(f"Target file: {self.selectedTargetImageFile}"))
        self.addImageInWindow_usingFilePath(target_image=self.selectedTargetImageFile)
    
    def startDetectionProccess(self):
        if self.selectedTargetImageFile == None:
            self.FaceDetectionPage.textBrowser_logConsole.append(html_draft.gen_error_text("İşlemi başlatmak için lütfen hedef resim seçiniz."))
            self.selectedTargetImageFile = None
            return
        
        self.backEndWorkerThread = faceDetectionBackendThread(targetFilePath=self.selectedTargetImageFile)
        self.backEndWorkerThread.statusSignal.connect(self.threadSignalHandler)
        self.backEndWorkerThread.start()
    
    def clearLogConsole(self):
        self.FaceDetectionPage.textBrowser_logConsole.setText("<B>LOG CONSOLE:</B>")
        self.FaceDetectionPage.textBrowser_allDataFromDetections.setText("<B>SON TESPİTE AİT TÜM VERİLER:</B>")
        self.showDefaultImage()
        
        
    def threadSignalHandler(self, signalDict):
        if signalDict["end"] == True and signalDict["success"] != True:
            self.FaceDetectionPage.textBrowser_logConsole.append(str(signalDict["text"]))
            return
        
        if signalDict["end"] == False and signalDict["success"] == None:
            self.FaceDetectionPage.textBrowser_logConsole.append(str(signalDict["text"]))
            return
        
        if signalDict["end"] == True and signalDict["success"] == True:
            import cv2
            image_data = signalDict["cv2_image"]
            image_data = cv2.resize(image_data, self.detectModelDefaultResulation)
            image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
            img_height, img_width = self.detectModelDefaultResulation
            image_data = QtGui.QImage(image_data, img_width, img_height,QtGui.QImage.Format.Format_RGB888)
            self.FaceDetectionPage.label_showImage.setPixmap(QtGui.QPixmap.fromImage(image_data))
            self.FaceDetectionPage.textBrowser_logConsole.append(str(signalDict["text"]))
            self.FaceDetectionPage.textBrowser_logConsole.append(html_draft.gen_info_text("Tespite ait tam veri yan sekmededir."))
            self.FaceDetectionPage.textBrowser_allDataFromDetections.append(str(signalDict["face_data"]))
            return
    
    def addImageInWindow_usingFilePath(self,target_image):
        import cv2
        image_data = cv2.imread(target_image)
        image_data = cv2.resize(image_data, self.detectModelDefaultResulation)
        image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
        img_height, img_width = self.detectModelDefaultResulation
        image_data = QtGui.QImage(image_data, img_width, img_height,QtGui.QImage.Format.Format_RGB888)
        self.FaceDetectionPage.label_showImage.setPixmap(QtGui.QPixmap.fromImage(image_data))
        
        
        
        
        """
        # Reference code:
        
        self.selectInputFile = cv2.imread(self.selectInputFile)
        self.analays_target = self.selectInputFile
        self.selectInputFile = cv2.resize(self.selectInputFile,(624,624))
        
        self.selectInputFile = cv2.cvtColor(self.selectInputFile,cv2.COLOR_BGR2RGB)
        yukseklik , genislik = self.selectInputFile.shape[0], self.selectInputFile.shape[1]
        self.selectInputFile = QtGui.QImage(self.selectInputFile, genislik,yukseklik,QtGui.QImage.Format.Format_RGB888)
        self.detectPage.label_imageShow.setPixmap(QtGui.QPixmap.fromImage(self.selectInputFile))
        """
