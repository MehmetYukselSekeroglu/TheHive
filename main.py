from hivelibrary import console_tools
from hivelibrary.env import *
from hivelibrary import database_tools
from hivelibrary import database_structure


from PyQt5.QtWidgets import *


import sqlite3
import threading
import pathlib
import os
import sys


# Start database connections
DB_CNN = sqlite3.connect(DATABASE_PATH,check_same_thread=False)
DB_CURSOR = DB_CNN.cursor()

if database_tools.check_db_init_status(DB_CNN,DB_CURSOR) == False:
    console_tools.InformationPrinter(f"Database init started")
    console_tools.LogPrinter("Inıting database schema")
    DB_CURSOR.executescript(database_structure.DATABASE_STRUCTURE_COMMAND)
    print(database_tools.insertData_systemTable(db=DB_CNN,db_cursor=DB_CURSOR,sql_key=APPLICATION_VENDOR_KEY, key_value=APPLICATION_VENDOR_VALUE))
    print(database_tools.insertData_systemTable(db=DB_CNN,db_cursor=DB_CURSOR,sql_key=APPLICATION_NAME_KEY, key_value=APPLICATION_NAME_VALUE))
    print(database_tools.insertData_systemTable(db=DB_CNN,db_cursor=DB_CURSOR,sql_key=APPLICATION_VERSION_KEY, key_value=APPLICATION_VERSION_VALUE))









