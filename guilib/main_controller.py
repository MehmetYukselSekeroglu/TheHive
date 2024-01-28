from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal


from guilib.TheHive_mainWindow import Ui_TheHve_MainWindow
from guilib.coomingSoom_controller import CoomingSoonPage
from guilib.ibanParser_controller import ibanParserPage
from guilib.changePassword_controller import PasswordChangePage
from guilib.soundConverter_controller import soundConverterPage
from guilib.voiceVerification_controller import voiceVerificationPage
from guilib.videoFrameExtractor_controller import VideoFrameExtractorPage
from guilib.FaceDetection_controller import FaceDetectionWidget
from guilib.FaceVerificationFromImage_controller import FaceVerificationScreen_from_image
from guilib.PhoneNumberParser_controller import PhoneNumberParserWidget
from guilib.TcNumberValidationChecker_controller import TcValidatorCheckerWidget
from guilib.TcNumberCalculator_controller import TcCalculatorWidget
from guilib.FaceRecognition_controller import FaceRecognitionWidget

from hivelibrary import env
from hivelibrary import os_information
import sqlite3
import time


WELCOME_SCREEN_TEXT = f"""Welcome to <B>TheHive Remastred</B><br><br>
TheHive is a fully equipped professional osint kit project with v2 version. Developed by {env.APPLICATION_VENDOR_VALUE}.
<br><br>
Contact information:<br>
GitHub Page: https://MehmetYukselSekeroglu/TheHive<br>
E-mail     : contact.primesec@gmail.com<br>
<br>
"""


class welcomeScreenSourceThread(QThread):
    returnSignal = pyqtSignal(str)

    
    def __init__(self, updateSecond=1):
        super().__init__()
        
        self.updateSecond = updateSecond
        self.activeOsUser = os_information.get_active_user()
        self.computerHostname = os_information.get_hostname()
        self.totalCpuCount = os_information.total_cpu_count()
        
    def run(self):
        while True:
            currentBattaryStatus = os_information.get_battery_percentage()
            memoryDict = os_information.get_memory_usage()
            totalRam = memoryDict["total"]
            usedRam = memoryDict["used"]
            yuzdelikRam = memoryDict["yüzde"]
            cpu_usage = os_information.get_cpu_usage()
            
            outputText =  f"""<B style="align:center;"> SYSTEM INFORMATION </B><br><br>
Os User     :    {self.activeOsUser}<br>
Hostname    :    {self.computerHostname}<br>
Cpu count   :    {self.totalCpuCount}<br>
<br>
Cpu     :    %{cpu_usage}<br>
Ram     :    {usedRam}/{totalRam} GB    %{yuzdelikRam}<br>
Battary :    {currentBattaryStatus}<br>
<br>
Update  :    {self.updateSecond} sec<br>
TheHive version: {env.APPLICATION_VERSION_VALUE}"""
          
            self.returnSignal.emit(outputText)
            time.sleep(self.updateSecond)


class TheHive_mainPage(QMainWindow):
    def __init__(self, db_cnn:sqlite3.Connection, db_cursor:sqlite3.Cursor):
        super().__init__()
        
        self.mainScreen = Ui_TheHve_MainWindow()
        self.mainScreen.setupUi(self)
        
        
        self.setWindowTitle("TheHive Remastred")
        
        self.db_cnn = db_cnn
        self.db_cursor = db_cursor
        self.DBS_CONF = [self.db_cnn, self.db_cursor]
        
        self.backEndWorkerThread = welcomeScreenSourceThread(updateSecond=1)
        self.backEndWorkerThread.returnSignal.connect(self.sourceThreadSignalHandler)
        self.backEndWorkerThread.start()
        
        self.mainScreen.actioniban_Parser.triggered.connect(self.menuAction_ibanParser)
        self.mainScreen.actionChange_Login_Password.triggered.connect(self.menuAction_loginPasswordChange)
        self.mainScreen.actionSound_Converter.triggered.connect(self.menuAction_soundConverter)
        self.mainScreen.actionVoice_verification.triggered.connect(self.menuAction_voiceVerification)
        self.mainScreen.actionVideo_frame_extractor.triggered.connect(self.menuAction_videoFrameExtactor)
        self.mainScreen.actionFace_Detection.triggered.connect(self.menuAction_FaceInsight_faceDetection)
        self.mainScreen.actionFace_Verification.triggered.connect(self.menuAction_FaceInsight_faceVerification)
        self.mainScreen.actionPhone_number_parser.triggered.connect(self.menuAction_phoneNumberParser)
        self.mainScreen.actionTC_Verification.triggered.connect(self.menuAction_TcValidator)
        self.mainScreen.actionTC_Calculator.triggered.connect(self.menuAction_TcCalculator)
        self.mainScreen.actionFace_Recognition.triggered.connect(self.menuAction_FaceInsight_FaceRecognition)
        
        self.mainScreen.textBrowser_WelcomeAndToolinfo.setText(WELCOME_SCREEN_TEXT)


    def menuAction_FaceInsight_FaceRecognition(self):
        self.FaceRecognition = FaceRecognitionWidget(db_cnn=self.db_cnn, db_curosr=self.db_cursor)
        self.FaceRecognition.show()

    def menuAction_TcCalculator(self):
        self.TcCalculator = TcCalculatorWidget()
        self.TcCalculator.show()

    def menuAction_TcValidator(self):
        self.TcValidator = TcValidatorCheckerWidget()
        self.TcValidator.show()

    def menuAction_phoneNumberParser(self):
        self.phoneNumberParser = PhoneNumberParserWidget()
        self.phoneNumberParser.show()

    def menuAction_FaceInsight_faceVerification(self):
        self.faceVerificationScreen = FaceVerificationScreen_from_image()
        self.faceVerificationScreen.show()

    def sourceThreadSignalHandler(self, data_strings):
        self.mainScreen.textBrowser_systemStatus.setText(data_strings)


    def menuAction_FaceInsight_faceDetection(self):
        self.FaceDetectionScreen = FaceDetectionWidget()
        self.FaceDetectionScreen.show()
    
    def menuAction_voiceVerification(self):
        self.voiceVerificationScreen = CoomingSoonPage(outputMessage="Kütüpahne güncellemesi nedeniyle doğruluk oranları tekrar hesaplanacaktır bu modul şuan kapalıdır")
        self.voiceVerificationScreen.show()
    
    def menuAction_soundConverter(self):
        self.soundConverterScreen = soundConverterPage(output_dir=env.DEFAULT_ROOT_DIR_NAME, temp_dir=env.DEFAULT_TEMP_DIR)
        self.soundConverterScreen.show()
        
        
    def menuAction_loginPasswordChange(self):
        self.passwordChangeScreen = PasswordChangePage(*self.DBS_CONF)
        self.passwordChangeScreen.show()
        
    def menuAction_ibanParser(self):
        self.ibanScreen = ibanParserPage()
        self.ibanScreen.show()
    
    def menuAction_videoFrameExtactor(self):
        self.videoFrameExtractorScreen = VideoFrameExtractorPage()
        self.videoFrameExtractorScreen.show()
    
        
    def coomingSoonTheFuture(self):
        msg = """Bu özellik şuanda bu sürümde mevcut değildir. Güncellemekleri kontrol ediniz veya resmi github hesabını kontrol ediniz.<br>
<br>
<br>
<B>GitHub:</B> https://github.com/MehmetYukselSekeroglu/TheHive <br>
<B>e-mail:</B> PrimeSecurity@gmail.com <br>
"""
        self.informationPage = CoomingSoonPage(outputMessage=msg)
        self.informationPage.show()