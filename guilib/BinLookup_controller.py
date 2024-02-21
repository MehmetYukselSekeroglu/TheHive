from guilib.BinLookupScreen import Ui_BIN_LOOKUP_WIDGET
from PyQt5.QtWidgets import *


from guilib.html_text_generator.html_draft import gen_error_text,gen_info_text

from hivelibrary.bin_lookup import lookup_bin



class BinLookupWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.BinLookup = Ui_BIN_LOOKUP_WIDGET()
        self.BinLookup.setupUi(self)
        self.setWindowTitle(f"Bin Lookup")
        self.BinLookup.pushButton_start.clicked.connect(self.startLookup)
        self.BinLookup.pushButton_clear.clicked.connect(self.clearResults)
        self.BinLookup.textBrowser_logConsole.setText("<B>LOG CONSOLE:</B>")
    
    def startLookup(self):
        
        targetBin = self.BinLookup.lineEdit_bin_input.text()

        if len(targetBin) < 6 or not targetBin[:6].isnumeric():
            self.BinLookup.textBrowser_logConsole.append(gen_error_text("❌ Invalid BIN, example: 123123"))
            return  
        
        self.BinLookup.textBrowser_logConsole.append(gen_info_text("Sending api"))
        lookup_data = lookup_bin(target_bin=targetBin)

        if lookup_data[0] == False:
            self.BinLookup.textBrowser_logConsole.append(gen_error_text(lookup_data[1]))        
            return
        
        self.BinLookup.textBrowser_logConsole.append(gen_info_text("Proccess success"))
        self.BinLookup.textBrowser_logConsole.append(str(">"*15) + str("<"*15))
        self.BinLookup.textBrowser_logConsole.append(lookup_data[1])
        self.BinLookup.textBrowser_logConsole.append(str(">"*15) + str("<"*15))

    
    def clearResults(self):
        self.BinLookup.textBrowser_logConsole.setText("<B>LOG CONSOLE:</B>")
        self.BinLookup.lineEdit_bin_input.clear()
        
        
        