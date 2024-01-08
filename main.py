from hivelibrary import console_tools
from hivelibrary.env import *
from hivelibrary import database_tools
from hivelibrary import database_structure


from PyQt5.QtWidgets import *

from guilib.TheHive_mainWindow import Ui_TheHve_MainWindow # for test imports
from guilib.login_controller import LoginScreen
from guilib.new_account_controller import NewAccountScreen
import sqlite3
import threading
import pathlib
import os
import sys



# Start database connections
DB_CNN = sqlite3.connect(DATABASE_PATH,check_same_thread=False)
DB_CURSOR = DB_CNN.cursor()
DBS_CONF = [DB_CNN, DB_CURSOR]

if database_tools.check_db_init_status(*DBS_CONF) == False:
    console_tools.LogPrinter(f"Database init started")
    console_tools.LogPrinter("Inıting database schema")
    DB_CURSOR.executescript(database_structure.DATABASE_STRUCTURE_COMMAND)
    print(database_tools.insertData_systemTable(*DBS_CONF,sql_key=APPLICATION_VENDOR_KEY, key_value=APPLICATION_VENDOR_VALUE))
    print(database_tools.insertData_systemTable(*DBS_CONF,sql_key=APPLICATION_NAME_KEY, key_value=APPLICATION_NAME_VALUE))
    print(database_tools.insertData_systemTable(*DBS_CONF,sql_key=APPLICATION_VERSION_KEY, key_value=APPLICATION_VERSION_VALUE))


console_tools.LogPrinter("Database alredy configurated")



class mainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainEkran = Ui_TheHve_MainWindow()
        self.mainEkran.setupUi(self)




if database_tools.check_admin_is_generated(db_cursor=DB_CURSOR)["success"] == True:
    app = QApplication([])
    app_win = LoginScreen(sqlite_cnn=DB_CNN,sqlite_curosr=DB_CURSOR,targetWindow=mainApp)
    app_win.show()
    app.exec_()
    
    
else:
    console_tools.LogPrinter("admin account not be detect starting account manager")
    main_application = QApplication([])
    main_window = NewAccountScreen(db_connections=DB_CNN,db_cursor=DB_CURSOR,targetWindow=mainApp)
    main_window.show()
    main_application.exec_()


        
        
        





