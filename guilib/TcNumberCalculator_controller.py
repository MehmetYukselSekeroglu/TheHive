from guilib.TcNumberCalculatorScreen import Ui_TcNumberCalculator
from guilib.html_text_generator.html_draft import gen_error_text, gen_info_text
from PyQt5.QtWidgets import *
from hivelibrary.identify.tc_number_tools import tc_uretici, gecerlilik_kontrol





class TcCalculatorWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.TcCalculatorPage = Ui_TcNumberCalculator()
        self.TcCalculatorPage.setupUi(self)
        self.setWindowTitle("Tc Calculator")
        
        self.TcCalculatorPage.pushButton_startCalculator.clicked.connect(self.startCalculating)    
        
    def startCalculating(self):
        self.clearLogConsole()
        getTc = self.TcCalculatorPage.lineEdit_tcNumberInput.text()
        getCount = self.TcCalculatorPage.spinBox_numberOfCalculating.value()
        
        if len(getTc) != 11:
            self.TcCalculatorPage.textBrowser_logConsole.append(str(gen_error_text("Tc numrası 11 haneli olmalıdır, işlem iptal edildi")))
            return
        
        if not getTc.isnumeric():
            self.TcCalculatorPage.textBrowser_logConsole.append(str(gen_error_text("Tc numrası sadece rakamlardan oluşmalıdır, işlem iptal edildi")))
            return
        
        if getCount < 1:
            self.TcCalculatorPage.textBrowser_logConsole.append(str(gen_error_text("Hesaplama adeti 0 olamaz, işlem iptal edildi ")))
            return
        
        
        check_before_tc_calculator = gecerlilik_kontrol(tc=getTc)
        
        if check_before_tc_calculator["success"] != True:
            self.TcCalculatorPage.textBrowser_logConsole.append(str(gen_error_text
                ("Girilen Tc numarası geçersiz bu nedenle bu numara üzerinden hesaplama yapılamaz, işlem iptal edildi ")))
            return
        
        ileriye_donuk, geriye_donuk = tc_uretici(uretilecek_tc=getTc,olustuma_adedi=getCount)
        
        self.TcCalculatorPage.textBrowser_logConsole.append(str(gen_info_text("Hesaplama başaryıla tamamlandı.")))
        self.TcCalculatorPage.textBrowser_logConsole.append("<br>[ INFO ]: İleriye Dönük")
        for tc in ileriye_donuk:
            tc = f"{tc}"
            self.TcCalculatorPage.textBrowser_logConsole.append(str(tc))
            
        self.TcCalculatorPage.textBrowser_logConsole.append("<br>[ INFO ]: Geriye Dönük")
        for tc in geriye_donuk:
            tc = f"{tc}"
            self.TcCalculatorPage.textBrowser_logConsole.append(tc)
        
        self.TcCalculatorPage.textBrowser_logConsole.append(str(gen_info_text("İşlem başarıyla tamamlandı")))
        
        
    def clearLogConsole(self):
        self.TcCalculatorPage.textBrowser_logConsole.setText("<B>LOG AND RESULTS: </B>")    
        
    