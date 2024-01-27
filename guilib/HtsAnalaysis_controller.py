from hivelibrary.env import DEFAULT_TEMP_DIR
from guilib.HtsAnalaysisScreen import Ui_HTSanalaysis

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QUrl, QThread,pyqtSignal


import folium
import os
import io
import time
import datetime






class HTS_analaysisWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.HTS_analaysis = Ui_HTSanalaysis()
        self.HTS_analaysis.setupUi(self)
        self.setWindowTitle("HTS Analiz Ekranı")
        

        self.HTS_analaysis.menubar
    
    def selectExcelFile(self):
        pass    

        