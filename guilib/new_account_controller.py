from hivelibrary import database_tools
from guilib.newAccountScreen import Ui_ConfigureAccounts

from PyQt5.QtWidgets import *

import sqlite3
import sys




class NewAccountScreen(QWidget):
    def __init__(self, db_connections, db_cursor, targetWindow,MainConfig):
        super().__init__()
        
    # setup the ui
        self.newAccountPage = Ui_ConfigureAccounts()
        self.newAccountPage.setupUi(self)
        
        # set dabase connections and cursor
        self.db_connections = db_connections
        self.db_cursor = db_cursor
        self.DBS_CONF =  [self.db_connections, self.db_cursor]
        # set return window
        self.targetMainWindow = targetWindow(*self.DBS_CONF,MainConfig)
        
        # set window title
        self.setWindowTitle("Configure Local Accounts")
        
        self.newAccountPage.pushButton_confirmAccount.clicked.connect(self.configureNewAccounts)
        self.newAccountPage.pushButton_exit_app.clicked.connect(self.exitProtocol)
        
        
        
    def configureNewAccounts(self):
        
        input_new_username = self.newAccountPage.lineEdit_getNewUsername.text()
        input_new_password = self.newAccountPage.lineEdit_getNewPassword.text()
        input_new_password_confirm = self.newAccountPage.lineEdit_getNewPasswordVerify.text()
        
        if len(input_new_username) < 3 or len(input_new_password) < 8 or len(input_new_password_confirm) < 8:
            err_msg="Status: username min len 3, password min len 8 chars"
            self.newAccountPage.label_status_info.setText(err_msg)
            return
        
        if input_new_password != input_new_password_confirm:
            err_msg="Status: passwords not match"
            self.newAccountPage.label_status_info.setText(err_msg)
            return
    
        config_status = database_tools.generate_admin_accounts(username=input_new_username, password=input_new_password,db=self.db_connections,db_cursor=self.db_cursor)
        
        if config_status["success"] != True:
            err_msg=f"Status: {config_status['data']} "
            self.newAccountPage.label_status_info.setText(err_msg)
            return
        
        self.hide()
        self.targetMainWindow.show()
        
        
        
    def exitProtocol(self):
        sys.exit(1)
        
        