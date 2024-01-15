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
        
        getNumber = self.phoneNumberParser.lineEdit_phoneInput.text()
        
        if len(getNumber) < 4:
            self.phoneNumberParser.textBrowser_logConsole.append(gen_error_text(
                f"Geçersiz numara formatı, format: +12948938591"
            ))
            return     
        
        if getNumber[0] != "+":
            self.phoneNumberParser.textBrowser_logConsole.append(gen_error_text(
                f"Geçersiz numara formatı, format: +12948938591"
            ))
            return
        
        if getNumber[0:3] != "+90":         
            self.phoneNumberParser.textBrowser_logConsole.append(gen_error_text(
                f"Şuanda sadece türk numaraları desteklenmektedir."
            ))
            return
        
        data_is = check_number_only_TR(phone_numbber=getNumber)
        
        if data_is["success"] != True:
            self.phoneNumberParser.textBrowser_logConsole.append(gen_error_text(
                data_is["message"]
            ))
            return  
        
        currentOperator = data_is["operatör"]
        otherCodesForCurrentOperator = data_is["supported_codes"]
        googleDorkForNumber = data_is["dork"]
        
        text = f"""<B>Numara için sonuçlar: </B><br><br>
Geçerli operatör: {currentOperator}<br>
Operatöre ait diğer kodlar: {otherCodesForCurrentOperator}<br>
<br>
Google Dork: {googleDorkForNumber}<br><br>
{"-"*30}"""
        self.phoneNumberParser.textBrowser_logConsole.append(text)

    
    def saveResult(self):
        self.phoneNumberParser.textBrowser_logConsole.append(gen_error_text(f"Bu özellik şuanda aktif değildir"))
        
        
    def clearLogConsole(self):
        self.phoneNumberParser.textBrowser_logConsole.setText("<B>LOG AND RESULTS: </B>")