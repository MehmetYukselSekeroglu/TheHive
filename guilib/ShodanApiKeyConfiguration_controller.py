from PyQt5.QtWidgets import *
from guilib.ShodanApiKeyConfigurationScreen import Ui_ApiKeyConfScreen
import sqlite3
import os


class shodanApiKeyConfigurationScreen(QWidget):
    def __init__(self, db_cnn:sqlite3.Connection, db_cursor:sqlite3.Cursor):
        super().__init__()
        
        
        self.DB_CONNECTIONS = db_cnn
        self.DB_CUROSR = db_cursor
        
        self.apiKeyConfScreen = Ui_ApiKeyConfScreen()
        self.apiKeyConfScreen.setupUi(self)
        
        self.setWindowTitle("Shodan Api Key Configuration")
        
        
        