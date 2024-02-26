from guilib.changePassworScreen import Ui_changePassword
from  hivelibrary import database_tools
from PyQt5.QtWidgets import *

class PasswordChangePage(QWidget):
    def __init__(self, db_connections, db_cursor):
        super().__init__()
        
        # temel sistemin kurulması
        self.passwordChangeWidget = Ui_changePassword()
        self.passwordChangeWidget.setupUi(self)
        self.setWindowTitle(f"Password Change")
        
        
        # Veritabanı objelerinin atanması
        self.db_connections = db_connections
        self.db_cursor = db_cursor
        
        
        # buton sinyallerinin slotlara bağlanması
        self.passwordChangeWidget.pushButton_cancelChangeProccess.clicked.connect(self.cancelProcess)
        self.passwordChangeWidget.pushButton_runChange.clicked.connect(self.changePassword)
        
        
    def changePassword(self):
        
        # Veri girişlerinin alınması
        old_password_input = self.passwordChangeWidget.lineEdit_oldPassword_input.text()
        new_password_input = self.passwordChangeWidget.lineEdit_newPassword_input.text()
        new_password_confirm_input = self.passwordChangeWidget.lineEdit_newPasswordConfirm_input.text()
        user_username = self.passwordChangeWidget.lineEdit_username_input.text()
        
        
        # girdilerin kontrol edilmesi uzunluk vs.
        if len(old_password_input) < 1 or len(new_password_input) < 1 or len(new_password_confirm_input) <1 or len(user_username) <1:
            err_text = f"Status: Failed, no password or username input"
            self.passwordChangeWidget.label_changeStatusBar.setText(err_text)
            self.clearAll_input()
            return 
        
        # girilen parola gerçekten kullanıcıya aitmi kontrol edilir 
        check_is_authenticated = database_tools.is_authenticated(username=user_username,password=old_password_input,db_cursor=self.db_cursor)
        
        
        # Yetki kontrol isteğinin sonucu kontrol edilir 
        if check_is_authenticated["success"] != True:
            err_text = f"Status: Invalid old password or username"
            self.passwordChangeWidget.label_changeStatusBar.setText(err_text)
            self.clearAll_input()
            return
        
        # Yeni parola ve doğrulama parolası eşleşiyormu kontrol edilir 
        if new_password_input != new_password_confirm_input:
            err_text = f"Status: New passwords do not match!"
            self.passwordChangeWidget.label_changeStatusBar.setText(err_text)
            self.clearAll_input()
            return
        
        # gereksinimler tammalandıysa sistem api sine değişim isteği gönderilir 
        results = database_tools.change_admin_password(username=user_username,new_password=new_password_input,db=self.db_connections,db_cursor=self.db_cursor)
        
        
        # api den gelen sonuç başarılımı kontrol edilir 
        if results["success"] != True:
            err_text = f"Status: database error, try after!"
            self.passwordChangeWidget.label_changeStatusBar.setText(err_text)
            self.clearAll_input()
            return  
        
        # işlem başarılı ise geri dönüş yapılır kullanıcıya 
        err_text = f"Status: password successfuly changed!"
        self.passwordChangeWidget.label_changeStatusBar.setText(err_text)
        self.clearAll_input()
        
        
        
    def clearAll_input(self):
        
        # Bütün verilerin temizlenmesi
        self.passwordChangeWidget.lineEdit_oldPassword_input.clear()
        self.passwordChangeWidget.lineEdit_newPassword_input.clear()
        self.passwordChangeWidget.lineEdit_newPasswordConfirm_input.clear()
        return
    
    
    def cancelProcess(self):
        
        # işlem iptal etmek istenirse
        self.hide()