from PyQt5.QtWidgets import *
from guilib.ShodanApiKeyConfigurationScreen import Ui_ApiKeyConfScreen
from hivelibrary.database_tools import check_exists_systemTable
from hivelibrary.env import SHODAN_API_KEY
import os
import shodan
import shodan.exception 

class shodanApiKeyConfigurationScreen(QWidget):
    def __init__(self, db_cnn, db_cursor):
        super().__init__()
        
        
        self.DB_CONNECTIONS = db_cnn
        self.DB_CUROSR = db_cursor
        
        self.apiKeyConfScreen = Ui_ApiKeyConfScreen()
        self.apiKeyConfScreen.setupUi(self)
        
        if check_exists_systemTable(db_curosr=self.DB_CUROSR,sql_key=SHODAN_API_KEY)[0]:
            self.alredyConfigurated()
        
        self.setWindowTitle("Enter Shodan Api Key And Configure")
        
        self.apiKeyConfScreen.pushButton_exitScreen.clicked.connect(self.exitThisScreen)
        self.apiKeyConfScreen.pushButton_startConfiguration.clicked.connect(self.configureApi)
    
    def alredyConfigurated(self):
        pass
    
    def exitThisScreen(self):
        self.hide()
    
    def configureApi(self):
        pass
    
    def testApiKey(self, api_key) -> list[bool ,str]:
        try:
            SHODAN_API = shodan.Shodan(key=api_key)
            data = SHODAN_API.host("1.1.1.1")
            return [ True, "Api Key Allowed"]
            
        except shodan.exception.APIError:
            return [ False, "Invalid Api Key" ]