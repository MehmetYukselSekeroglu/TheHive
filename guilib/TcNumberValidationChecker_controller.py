from PyQt5.QtWidgets import *
from guilib.TcNumberValidationCheckerScreen import Ui_TcValidatorScreen
from hivelibrary.identify.tc_number_tools import gecerlilik_kontrol






class TcValidatorCheckerWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.TcValidator = Ui_TcValidatorScreen()
        self.TcValidator.setupUi(self)
        self.setWindowTitle("Tc Validity Checker")
        
        
        self.TcValidator.pushButton_runValidationChecker.clicked.connect(self.__runValidtorChecker)
        
    
    def __runValidtorChecker(self):
        self.__clearLogConsole()
        
        getInput = self.TcValidator.lineEdit_tcInput.text()
        tcStatus = gecerlilik_kontrol(getInput)
        
        if len(getInput) != 11:
            return self.TcValidator.textBrowser_logConsole.append("<B>HATA: </B>Lütfen 11 haneli hedef tc numarası giriniz.")
        
        if not getInput.isnumeric():
            return self.TcValidator.textBrowser_logConsole.append("<B>HATA: </B>Tc numarası sadece rakamlardan oluşmalıdır.")
        
        
        self.TcValidator.textBrowser_logConsole.append(tcStatus["data"])
        
    def __clearLogConsole(self):
        self.TcValidator.textBrowser_logConsole.setHtml("<B>LOG AND RESULTS: </B><br>")