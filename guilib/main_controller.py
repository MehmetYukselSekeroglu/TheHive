from PyQt5.QtWidgets import *

from guilib.TheHive_mainWindow import Ui_TheHve_MainWindow
from guilib.coomingSoom_controller import CoomingSoonPage
from guilib.ibanParser_controller import ibanParserPage
from guilib.changePassword_controller import PasswordChangePage
from guilib.soundConverter_controller import soundConverterPage


from hivelibrary import env

import sqlite3


class TheHive_mainPage(QMainWindow):
    def __init__(self, db_cnn:sqlite3.Connection, db_cursor:sqlite3.Cursor):
        super().__init__()
        
        self.mainScreen = Ui_TheHve_MainWindow()
        self.mainScreen.setupUi(self)
        
        
        self.setWindowTitle("TheHive Remastred")
        
        self.db_cnn = db_cnn
        self.db_cursor = db_cursor
        self.DBS_CONF = [self.db_cnn, self.db_cursor]
        
        
        
        self.mainScreen.actioniban_Parser.triggered.connect(self.menuAction_ibanParser)
        self.mainScreen.actionChange_Login_Password.triggered.connect(self.menuAction_loginPasswordChange)
        self.mainScreen.actionSound_Converter.triggered.connect(self.menuAction_soundConverter)
        
    
    def menuAction_soundConverter(self):
        self.soundConverterScreen = soundConverterPage(output_dir=env.DEFAULT_ROOT_DIR_NAME, temp_dir=env.DEFAULT_TEMP_DIR)
        self.soundConverterScreen.show()
        
        
    def menuAction_loginPasswordChange(self):
        self.passwordChangeScreen = PasswordChangePage(*self.DBS_CONF)
        self.passwordChangeScreen.show()
        
    def menuAction_ibanParser(self):
        self.ibanScreen = ibanParserPage()
        self.ibanScreen.show()
        
        
    def coomingSoonTheFuture(self):
        msg = """Bu özellik şuanda bu sürümde mevcut değildir. Güncellemekleri kontrol ediniz veya resmi github hesabını kontrol ediniz.<br>
<br>
<br>
<B>GitHub:</B> https://github.com/MehmetYukselSekeroglu/TheHive <br>
<B>e-mail:</B> PrimeSecurity@gmail.com <br>
"""
        self.informationPage = CoomingSoonPage(outputMessage=msg)
        self.informationPage.show()