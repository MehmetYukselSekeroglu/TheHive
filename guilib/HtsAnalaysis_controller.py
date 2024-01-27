from hivelibrary.env import DEFAULT_TEMP_DIR
from guilib.HtsAnalaysisScreen import Ui_HTSanalaysis

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QUrl, QThread,pyqtSignal


import folium
import os
import io
import time
import datetime

from guilib.html_text_generator.html_draft import gen_error_text,gen_info_text
from hivelibrary.file_operations.file_information import sizeMB
from hivelibrary.hash_tools import file_hash_sha1
from hivelibrary.hts_toolkit.format_detector import HtsToolkit


class HTS_analaysisWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.HTS_analaysis = Ui_HTSanalaysis()
        self.HTS_analaysis.setupUi(self)
        self.setWindowTitle("HTS Analiz Ekranı")
        
        
        self.HTS_analaysis.pushButton_selectFile.clicked.connect(self.selectAnyFile)
        self.HTS_analaysis.pushButton_clearAll.clicked.connect(self.clearAllOutputs)
        
        self.selectedTargetFilePath = None
        self.isSupportedFormat = None
        self.HTStool = HtsToolkit()
        self.BackendAnalaysThread = QThread()        
    
    
    def checkFormat(self) -> None:
        pass
        
    def startAnalays(self) -> None:
        pass
    
    def stopAnalays(self) -> None:
        pass
    
    def threadSignalHandler(self) -> None:
        pass
    
    
    def clearAllOutputs(self) -> None:
        self.selectedTargetFilePath = None
        self.isSupportedFormat = None
        
        self.HTS_analaysis.textBrowser_targetFileSize.clear()
        self.HTS_analaysis.textBrowser_logConsole_tab1.setText("<B>LOG CONSOLE:</B>")
        self.HTS_analaysis.textBrowser_targetFileFormatStatus.clear()
        self.HTS_analaysis.textBrowser_targetFilePathShow.clear()
        self.HTS_analaysis.textBrowser_targetFileSha1Hash.clear()
        
    
    def selectAnyFile(self) -> None:
        fileSelector = QFileDialog()
        fileSelector.setNameFilter("File (*.*)")
        
        if fileSelector.exec_():
            self.selectedTargetFilePath = fileSelector.selectedFiles()[0]

        if self.selectedTargetFilePath == None or not os.path.exists(str(self.selectedTargetFilePath)):
            self.HTS_analaysis.textBrowser_targetFilePathShow.setText(gen_error_text("Ivalid file selections, proccess stopped"))
            self.selectedTargetFilePath = None
            return
        
        self.HTS_analaysis.textBrowser_targetFilePathShow.setText(str(self.selectedTargetFilePath))
        self.HTS_analaysis.textBrowser_targetFileSha1Hash.setText(file_hash_sha1(self.selectedTargetFilePath))
        self.HTS_analaysis.textBrowser_targetFileSize.setText(f"{sizeMB(self.selectedTargetFilePath)}")
        
        detectedFormat = self.HTStool.detect_hts_record_formats(targetFilePath=self.selectedTargetFilePath)
        
        if detectedFormat == "UNSUPPORTED":
            self.HTS_analaysis.textBrowser_targetFileFormatStatus.setText("Desteklenmeyen dosya formatı.")
            return
        
        self.HTS_analaysis.textBrowser_targetFileFormatStatus.setText(detectedFormat)
        
        
        
    
