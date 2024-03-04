# -*- coding: utf-8 -*-
# Project: TheHive v2 Remastred
# Official GitHub Address: https://github.com/MehmetYukselSekeroglu/TheHive
# Developed By Prime Security
# Website primesecurity.net.tr ( cooming soon )
# Version: v2.1.0 Testing 

# importing hive toolkit
from hivelibrary import console_tools
from hivelibrary.banner import printBanner

printBanner()

console_tools.InformationPrinter("importing TheHive library")
from hivelibrary.env import *
from hivelibrary import database_tools
from hivelibrary import database_structure


console_tools.InformationPrinter("importing PostgreSQL config")
from hivelibrary.psqlConfig import POSTGRESQL_CONFIG

console_tools.InformationPrinter("importing PyQt")
# importing python packagets
from PyQt5.QtWidgets import *

console_tools.InformationPrinter("importing TheHive UI")
# importing gui 
from guilib.login_controller import LoginScreen
from guilib.new_account_controller import NewAccountScreen
from guilib.main_controller import TheHive_mainPage


if not os.path.exists(DEFAULT_TEMP_DIR) or not os.path.isdir(DEFAULT_TEMP_DIR):
    os.makedirs(DEFAULT_TEMP_DIR)

if not os.path.exists(DEFAULT_ROOT_DIR_NAME) or not os.path.isdir(DEFAULT_ROOT_DIR_NAME):
    os.makedirs(DEFAULT_ROOT_DIR_NAME)

# Start database connections
DB_CNN , DB_CURSOR = database_tools.connection_function(POSTGRESQL_CONFIG)
DBS_CONF = [DB_CNN, DB_CURSOR]






console_tools.InformationPrinter("UI starting")
if database_tools.check_db_init_status(*DBS_CONF) == False:
    console_tools.InformationPrinter(f"Database init started")
    console_tools.InformationPrinter("Inıting database schema")
    DB_CURSOR.execute(database_structure.POSTGRESQL_DATABASE_STRUCTURE)
    print(database_tools.insertData_systemTable(*DBS_CONF,sql_key=APPLICATION_VENDOR_KEY, key_value=APPLICATION_VENDOR_VALUE))
    print(database_tools.insertData_systemTable(*DBS_CONF,sql_key=APPLICATION_NAME_KEY, key_value=APPLICATION_NAME_VALUE))
    print(database_tools.insertData_systemTable(*DBS_CONF,sql_key=APPLICATION_VERSION_KEY, key_value=APPLICATION_VERSION_VALUE))


console_tools.InformationPrinter("Database alredy configurated")
if database_tools.check_admin_is_generated(db_cursor=DB_CURSOR)["success"] == True:
    standartApp = QApplication([])
    standartWindow = LoginScreen(sqlite_cnn=DB_CNN,sqlite_curosr=DB_CURSOR,targetWindow=TheHive_mainPage)
    standartWindow.show()
    standartApp.exec_()
    
else:
    console_tools.InformationPrinter("admin account not be detect starting account manager")
    firstStartApp = QApplication([])
    firstStartWindow = NewAccountScreen(db_connections=DB_CNN,db_cursor=DB_CURSOR,targetWindow=TheHive_mainPage)
    firstStartWindow.show()
    firstStartApp.exec_()


        
        
        





