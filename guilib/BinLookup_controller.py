from guilib.BinLookupScreen import Ui_BIN_LOOKUP_WIDGET
from PyQt5.QtWidgets import *
from guilib.html_text_generator.html_draft import gen_error_text,gen_info_text
from hivelibrary.bin_lookup import lookup_bin



class BinLookupWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        # temel sistem kuruldu
        self.BinLookup = Ui_BIN_LOOKUP_WIDGET()
        self.BinLookup.setupUi(self)
        self.setWindowTitle(f"Bin Lookup")
        
        # buton sinyalleri slotlara bağlandı
        self.BinLookup.pushButton_start.clicked.connect(self.startLookup)
        self.BinLookup.pushButton_clear.clicked.connect(self.clearResults)
        
        # ön tanımlı değerler atandı
        self.BinLookup.textBrowser_logConsole.setText("<B>LOG CONSOLE:</B>")
    
    def startLookup(self):
        # Girilen bin alındı
        targetBin = self.BinLookup.lineEdit_bin_input.text()
        
        # Girdinin doğruluğu kontrol edildi
        if len(targetBin) < 6 or not targetBin[:6].isnumeric():
            self.BinLookup.textBrowser_logConsole.append(gen_error_text("❌ Invalid BIN, example: 123123"))
            return  
        
        # kullanıcı feedback
        self.BinLookup.textBrowser_logConsole.append(gen_info_text("Sending api"))
        
        # sistem apisine verinin gönderilmesi
        lookup_data = lookup_bin(target_bin=targetBin)

        # işlem başarısının kontrolü
        if lookup_data[0] == False:
            self.BinLookup.textBrowser_logConsole.append(gen_error_text(lookup_data[1]))        
            return
        
        # işlem başarılı ise verinin ekrana verilmesi
        self.BinLookup.textBrowser_logConsole.append(gen_info_text("Proccess success"))
        self.BinLookup.textBrowser_logConsole.append(str(">"*15) + str("<"*15))
        self.BinLookup.textBrowser_logConsole.append(lookup_data[1])
        self.BinLookup.textBrowser_logConsole.append(str(">"*15) + str("<"*15))

    
    def clearResults(self):
        # Çıktıların temizlenmesi
        self.BinLookup.textBrowser_logConsole.setText("<B>LOG CONSOLE:</B>")
        self.BinLookup.lineEdit_bin_input.clear()
        
        
        