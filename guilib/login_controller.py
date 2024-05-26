
from guilib.loginScreen import Ui_AuthenticationScreen

from hivelibrary import database_tools
from hivelibrary import console_tools

from PyQt5.QtWidgets import *
import sys


class LoginScreen(QWidget):
    def __init__(self, sqlite_cnn, sqlite_curosr, targetWindow, MainConfig):
        super().__init__()
        # Console Log
        console_tools.InformationPrinter("Starting login screen")
        
        # set external varaibles
        self.db_connections = sqlite_cnn
        self.db_cursor = sqlite_curosr
        self.DBS_CONF = [ self.db_connections, self.db_cursor ]
        
        # set current widget ui
        self.loginScreen = Ui_AuthenticationScreen()
        self.loginScreen.setupUi(self)
        
        # set return window
        self.targetMainWindow = targetWindow(*self.DBS_CONF,MainConfig)
        
        # set login credientals
        self.MAX_LOGIN_TRY = 3
        self.CURRENT_TRY = 0
        
        # set window title
        self.setWindowTitle(f"Local Authentication")
        
        # set button targets
        self.loginScreen.pushButton_initralAuth_authenticateButton.clicked.connect(self.tryAuthenticate)
        self.loginScreen.pushButton_initralAuth_exitButton.clicked.connect(self.exitProtocol)
    
    def tryAuthenticate(self):
        # add count in current trying
        self.CURRENT_TRY += 1
        
        # get username & password 
        input_username = self.loginScreen.lineEdit_initralAuth_username.text()
        input_password = self.loginScreen.lineEdit_initralAuth_password.text()
        
        # check trying count
        if self.CURRENT_TRY > self.MAX_LOGIN_TRY:
            console_tools.WarnPrinter("Maximum trial limit exceeded, exiting the program")
            self.exitProtocol()
        
        # send username password to hive api
        authenticateStatus = database_tools.is_authenticated(username=input_username,password=input_password,db_cursor=self.db_cursor)

        # TheHive api ye gönderilen verilerin sonuçları kontrol edilir 
        if authenticateStatus["success"] != True:
            console_tools.ErrorPrinter("Wrong password or username")
            err_text = f"Status: Failed, {str(self.MAX_LOGIN_TRY - self.CURRENT_TRY)} credit left."
            self.loginScreen.label_4_authenticate_status.setText(err_text)
            self.loginScreen.lineEdit_initralAuth_username.clear()
            self.loginScreen.lineEdit_initralAuth_password.clear()
            return

        else:
            console_tools.InformationPrinter("Authentication successfully")
            self.hide()
            self.targetMainWindow.show()
    
    # for exit button and broken authenticate protocol
    def exitProtocol(self):
        sys.exit(1)