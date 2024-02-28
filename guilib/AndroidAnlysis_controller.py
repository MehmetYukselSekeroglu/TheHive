from guilib.AndroidAnlysisScreen import Ui_AndroidAnlysisWidget
from guilib.html_text_generator import html_draft

from hivelibrary.AndroidTools import androguard_tools
from hivelibrary.hash_tools import all_hash

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os

DEFAULT_SPACE:int="30"

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

    def __finalyReturner(self, success:bool=False, end:bool=True, message:str=None):
        return self.threadSignal.emit({
            "success":success,
            "end":end,
            "message":message
        })

    def run(self):
        general_iformation = androguard_tools.get_information_standard(apk_path=self.targetApkFile)
        hash_information = all_hash(file_path=self.targetApkFile)
        
        if general_iformation[0] != True:    
            self.__finalyReturner(success=False, end=True, message=html_draft.gen_error_text(general_iformation[1]))
            return
        
        
        apk_info = general_iformation[1]
        
        apk_name = apk_info[0]
        packet_anem = apk_info[1]
        apk_target_sdk = apk_info[2]
        apk_min_sdk = apk_info[3]
        apk_max_sdk = apk_info[4]
        apk_internalVersion = apk_info[5]
        apk_displayedVersion= apk_info[6]
        apk_permissions_list = apk_info[7]
        apk_services_list = apk_info[8]
        apk_v1_issigned = apk_info[9]
        apk_v2_issigned = apk_info[10]
        apk_v3_issigned = apk_info[11]
        included_librarys_list = apk_info[12]
        included_files_list = apk_info[13]
        
        
        
        RETURN_TEXT = f"""
[ INFO ] FILE PATH:{self.targetApkFile}<br>
[ INFO ] DATE:None<br>
<br>
[ INFO ] HASHES:<br>
MD-5: {hash_information["md5"]}<br>
SHA-1: {hash_information["sha1"]}<br>
SHA-256: {hash_information["sha256"]}<br>
<br>
[ INFP ] PACKAGE INFORMATION:<br>
<br>
Apk Name: {apk_name}<br>
Package Name: {packet_anem}<br>
Displayed Version: {apk_displayedVersion}<br>
Internal Version: {apk_internalVersion}<br>
Target SDK: {apk_target_sdk}<br>
Minimum SDK: {apk_min_sdk}<br>
Maximum SDK: {apk_max_sdk}<br>
V1 Signature: {apk_v1_issigned}<br>
V2 Signature: {apk_v2_issigned}<br>
V3 Signature: {apk_v3_issigned}<br><br>"""



        if len(apk_services_list) > 0:
            RETURN_TEXT += """[ INFO ] SERVICES:<br><br>"""

            for file in apk_services_list:
                RETURN_TEXT += f"""{file}<br>"""

            RETURN_TEXT += "<br><br>"
        else:
            RETURN_TEXT += """[ INFO ] NO SERVICES<br><br>"""

        if len(apk_permissions_list) > 0:
            RETURN_TEXT += """[ INFO ] PERMISSIONS:<br><br>"""

            for file in apk_permissions_list:
                RETURN_TEXT += f"""{file}<br>"""

            RETURN_TEXT += "<br><br>"
        else:
            RETURN_TEXT += """[ INFO ] NO PERMISSIONS<br><br>"""




        if len(included_librarys_list) > 0:
            RETURN_TEXT += """[ INFO ] INCLUDED LIBRARY:<br><br>"""

            for file in included_librarys_list:
                RETURN_TEXT += f"""{file}<br>"""

            RETURN_TEXT += "<br><br>"
        else:
            RETURN_TEXT += """[ INFO ] NO INCLIDED LIBRARY<br><br>"""






        self.__runningReturner(message=RETURN_TEXT)        
        


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
        

        
        