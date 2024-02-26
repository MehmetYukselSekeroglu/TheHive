from guilib.AndroidAnlysisScreen import Ui_AndroidAnlysisWidget
from guilib.html_text_generator import html_draft

from hivelibrary.AndroidTools import androguard_tools

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os



"""
*** ANDROID ANALIZ ARAC SETI ***
Prime Securtiy 2024 | primesecurity.net.tr 

Android paket (APK) analiz aracı.

Temel Analiz:
androgurd üzerinden temel paket analizi (servisler, izinler, dosyalar vs)

Hash:
Dosyaya ait hash bilgileri 

VirüsTotal:
Dosyayı virüs total üzerinden analiz etme özelliği
"""

class backendWorker(QThread):
    threadSignal = pyqtSignal(dict)
    
    
    def __init__(self, targetApkPath:str):
        super().__init__()
        
        self.targetApkFile = targetApkPath

    
    def __runningReturner(self, message:str):
        return self.threadSignal.emit({
            "success":None,
            "end":False,
            "message":message,
            
        })


    def run(self):
        general_iformation = androguard_tools.get_information_standard(apk_path=self.targetApkFile)
        
        if general_iformation[0] != True:
            pass
        
        
        
        


class AndroidAnlysisPage(QWidget):
    def __init__(self):
        super().__init__()
        
        # temel sistem tanımlandı
        self.AndroidPage = Ui_AndroidAnlysisWidget()
        self.AndroidPage.setupUi(self)
        self.setWindowTitle("Android Anlysis")
        self.AndroidPage.lineEdit_showTargetPath.setDisabled(True)
        
        
        # buton sinyalleri slolata bağlandı
        self.AndroidPage.pushButton_selectFile.clicked.connect(self.selectTargetFile)
        self.AndroidPage.pushButton_startAnlysis.clicked.connect(self.startAnlysis)
        self.AndroidPage.pushButton_stopAnlysis.clicked.connect(self.stopAnlysis)
        self.AndroidPage.pushButton_saveReport.clicked.connect(self.saveReport)
        
        # global değişkenler tanımlandı
        self.BackendWorkerThread = QThread()
        self.SelectedTargetFile = None
        
        
        
    def selectTargetFile(self) -> None:
        # Android .apk dosyalarının seçimi 
        fileSelector = QFileDialog()
        fileSelector.setNameFilter("APK Files (*.apk)")
        if fileSelector.exec_():
            self.SelectedTargetFile = fileSelector.selectedFiles()[0]
        
        # seçim yapıldımı kontrol edilir 
        if self.SelectedTargetFile == None:
            self.AndroidPage.lineEdit_showTargetPath.setText("Ivalid file selections, proccess stopped")
            self.SelectedTargetFile = None
            return
        
        # seçilen dosya sistemde gerçekten varmı kontrol edilir
        if not os.path.exists(self.SelectedTargetFile) or not os.path.isfile(self.SelectedTargetFile):
            self.AndroidPage.lineEdit_showTargetPath.setText("Ivalid file selections, proccess stopped")
            self.SelectedTargetFile = None
            return
        
        # seçim doğru yapıldıysa değişkene atandı
        self.AndroidPage.lineEdit_showTargetPath.setText(self.SelectedTargetFile)
        
    
    def startAnlysis(self) -> None:
        
        # çalışan bir analiz varmı kontrol edilir 
        if self.BackendWorkerThread.isRunning():
            self.AndroidPage.textBrowser_logConsole.append(html_draft.gen_error_text("Aktif bir işleö devam ederken tekrar istek yapılamaz."))
            return
        
        # gerekli değişkenler atanmışmı kontrol edilir 
        if self.SelectedTargetFile == None:
            self.AndroidPage.textBrowser_logConsole.append(html_draft.gen_error_text("Kaynak dosya seçilmedi, işlem iptal edildi"))
            return
        
        # uygulama donmasın diye QThread tanımlanır ve çalışır 
        self.BackendWorkerThread = backendWorker(targetApkPath=self.SelectedTargetFile)
        self.BackendWorkerThread.threadSignal.connect(self.threadSignalHandler)
        self.BackendWorkerThread.start()
        
    
    def stopAnlysis(self) -> None:
        
        # Çalışan bir thread varmı kontrol edilir 
        if not self.BackendWorkerThread.isRunning():
            self.AndroidPage.textBrowser_logConsole.append(html_draft.gen_error_text("Durdurulacak aktif bir analiz işlemi yoktur"))
            return
        
        # çalışan bir thread varsa durdurulur ve beklenir 
        self.BackendWorkerThread.quit()
        self.BackendWorkerThread.wait()
        self.AndroidPage.textBrowser_logConsole.append(html_draft.gen_info_text("Aktif analiz işlemi kullanıcı tarafından sonlandırıldı"))
    
    
    def saveReport(self) -> None:
        # rapor kayıt fonksiyonu
        pass
        
    
    
    def threadSignalHandler(self, threadData) -> None:  
        self.AndroidPage.textBrowser_logConsole.append(str(threadData["message"]))
        

        
        