# -*- coding: utf-8 -*-
# Project: TheHive v2 Remastred
# Official GitHub Address: https://github.com/MehmetYukselSekeroglu/TheHive
# Developed By Prime Security
# Version: v2.0.0 Testing

# importing hive toolkit
from hivelibrary import console_tools
from hivelibrary.env import *
from hivelibrary import database_tools
from hivelibrary import database_structure

# importing python packagets
from PyQt5.QtWidgets import *
import sqlite3

# importing gui 
from guilib.login_controller import LoginScreen
from guilib.new_account_controller import NewAccountScreen
from guilib.main_controller import TheHive_mainPage



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


if database_tools.check_admin_is_generated(db_cursor=DB_CURSOR)["success"] == True:
    standartApp = QApplication([])
    standartWindow = LoginScreen(sqlite_cnn=DB_CNN,sqlite_curosr=DB_CURSOR,targetWindow=TheHive_mainPage)
    standartWindow.show()
    standartApp.exec_()
    
else:
    console_tools.LogPrinter("admin account not be detect starting account manager")
    firstStartApp = QApplication([])
    firstStartWindow = NewAccountScreen(db_connections=DB_CNN,db_cursor=DB_CURSOR,targetWindow=TheHive_mainPage)
    firstStartWindow.show()
    firstStartApp.exec_()


        
        
        





