from PyQt5.QtWidgets import *
from guilib.PhoneNumberParserScreen import Ui_phoneNumberParser
from guilib.html_text_generator.html_draft import *

from hivelibrary.identify.phoneNumper_tools import check_number_only_TR


class PhoneNumberParserWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.phoneNumberParser = Ui_phoneNumberParser()
        self.phoneNumberParser.setupUi(self)
        
        
        self.setWindowTitle("Phone Number Parser")
        
        
        self.phoneNumberParser.pushButton_startProccess.clicked.connect(self.runParser)
        self.phoneNumberParser.pushButton_saveResults.clicked.connect(self.saveResult)
    
    
    def runParser(self):
        self.clearLogConsole()
        
        
        
    
    
    def saveResult(self):
        self.phoneNumberParser.textBrowser_logConsole.append(gen_error_text(f"Bu özellik şuanda aktif değildir"))
        
        
    def clearLogConsole(self):
        self.phoneNumberParser.textBrowser_logConsole.setText("<B>LOG AND RESULTS: </B>")