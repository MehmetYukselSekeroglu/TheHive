
from guilib.loginScreen import Ui_AuthenticationScreen

from hivelibrary import database_tools

from PyQt5.QtWidgets import *
import sqlite3
import sys


class LoginScreen(QWidget):
    def __init__(self, sqlite_cnn:sqlite3.Connection, sqlite_curosr:sqlite3.Cursor, targetWindow):
        super().__init__()
        # set external varaibles
        self.db_connections = sqlite_cnn
        self.db_cursor = sqlite_curosr
        self.DBS_CONF = [ self.db_connections, self.db_cursor ]
        
        # set current widget ui
        self.loginScreen = Ui_AuthenticationScreen()
        self.loginScreen.setupUi(self)
        
        # set return window
        self.targetMainWindow = targetWindow()
        
        # set login credientals
        self.MAX_LOGIN_TRY = 3
        self.CURRENT_TRY = 0
        
        # set window title
        self.setWindowTitle(f"Local Authentication")
        
        # set button targets
        self.loginScreen.pushButton_initralAuth_authenticateButton.clicked.connect(self.tryAuthenticate)
        self.loginScreen.pushButton_initralAuth_exitButton.clicked.connect(self.exitProtocol)
    
    def tryAuthenticate(self):
        self.CURRENT_TRY += 1
        
        input_username = self.loginScreen.lineEdit_initralAuth_username.text()
        input_password = self.loginScreen.lineEdit_initralAuth_password.text()
        
        if self.CURRENT_TRY >= self.MAX_LOGIN_TRY:
            self.exitProtocol()
        
            
        authenticateStatus = database_tools.is_authenticated(username=input_username,password=input_password,db_cursor=self.db_cursor)

        if authenticateStatus["success"] != True:
            err_text = f"Status: Failed, {str(self.MAX_LOGIN_TRY - self.CURRENT_TRY)} credit left."
            self.loginScreen.label_4_authenticate_status.setText(err_text)
            self.loginScreen.lineEdit_initralAuth_username.clear()
            self.loginScreen.lineEdit_initralAuth_password.clear()
            return

        else:
            self.hide()
            self.targetMainWindow.show()
    
    # for exit button and broken authenticate protocol
    def exitProtocol(self):
        sys.exit(1)