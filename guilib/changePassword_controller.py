from guilib.changePassworScreen import Ui_changePassword
from  hivelibrary import database_tools

from PyQt5.QtWidgets import *
import sqlite3

class PasswordChangePage(QWidget):
    def __init__(self, db_connections:sqlite3.Connection, db_cursor:sqlite3.Cursor):
        super().__init__()
        
        self.passwordChangeWidget = Ui_changePassword()
        self.passwordChangeWidget.setupUi(self)
        
        
        self.db_connections = db_connections
        self.db_cursor = db_cursor
        
        self.setWindowTitle(f"Password Change")
        
        
        self.passwordChangeWidget.pushButton_cancelChangeProccess.clicked.connect(self.cancelProcess)
        self.passwordChangeWidget.pushButton_runChange.clicked.connect(self.changePassword)
        
        
    def changePassword(self):
        old_password_input = self.passwordChangeWidget.lineEdit_oldPassword_input.text()
        new_password_input = self.passwordChangeWidget.lineEdit_newPassword_input.text()
        new_password_confirm_input = self.passwordChangeWidget.lineEdit_newPasswordConfirm_input.text()
        user_username = self.passwordChangeWidget.lineEdit_username_input.text()
        
        
        if len(old_password_input) < 1 or len(new_password_input) < 1 or len(new_password_confirm_input) <1 or len(user_username) <1:
            err_text = f"Status: Failed, no password or username input"
            self.passwordChangeWidget.label_changeStatusBar.setText(err_text)
            self.clearAll_input()
            return 
        
        check_is_authenticated = database_tools.is_authenticated(username=user_username,password=old_password_input,db_cursor=self.db_cursor)
        
        
        if check_is_authenticated["success"] != True:
            err_text = f"Status: Invalid old password or username"
            self.passwordChangeWidget.label_changeStatusBar.setText(err_text)
            self.clearAll_input()
            return
        
        if new_password_input != new_password_confirm_input:
            err_text = f"Status: New passwords do not match!"
            self.passwordChangeWidget.label_changeStatusBar.setText(err_text)
            self.clearAll_input()
            return
        
        
        results = database_tools.change_admin_password(username=user_username,new_password=new_password_input,db=self.db_connections,db_cursor=self.db_cursor)
        if results["success"] != True:
            err_text = f"Status: database error, try after!"
            self.passwordChangeWidget.label_changeStatusBar.setText(err_text)
            self.clearAll_input()
            return  
        
        err_text = f"Status: password successfuly changed!"
        self.passwordChangeWidget.label_changeStatusBar.setText(err_text)
        self.clearAll_input()
        
        
    def clearAll_input(self):
        self.passwordChangeWidget.lineEdit_oldPassword_input.clear()
        self.passwordChangeWidget.lineEdit_newPassword_input.clear()
        self.passwordChangeWidget.lineEdit_newPasswordConfirm_input.clear()
        return
    
    def cancelProcess(self):
        self.hide()