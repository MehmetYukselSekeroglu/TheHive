import sqlite3


from hivelibrary.env import DB_BLOB_STORAGE, DB_SYSTEM_TABLE, DB_LOCAL_AUTHENTICATE_TABLE
from hivelibrary.env import DB_DATA_TYPE__USER
from hivelibrary.env import APPLICATION_NAME_KEY
from hivelibrary.hash_tools import loginCreditHhasher

def check_db_init_status(db:sqlite3.Connection, db_cursor:sqlite3.Cursor) -> bool:
    try:
        STATIC_SQL_COMMAND = f"SELECT * FROM {DB_SYSTEM_TABLE} WHERE uniq_key=?"
        STATIC_DATA_TUPLE = (APPLICATION_NAME_KEY,)
        
        result = db_cursor.execute(STATIC_SQL_COMMAND,STATIC_DATA_TUPLE ).fetchall()        
        if len(result) < 1:
            return False
        
        return True


    except Exception:
        return False



def insertData_systemTable(db:sqlite3.Connection, db_cursor:sqlite3.Cursor, sql_key:str, key_value:str) -> dict:
    try:
        STATIC_SQL_COMMAND = f"SELECT * FROM {DB_SYSTEM_TABLE} WHERE uniq_key=?"
        STATIC_DATA_TUPLE = (sql_key,)
        results = db_cursor.execute(STATIC_SQL_COMMAND, STATIC_DATA_TUPLE).fetchall()

        if len(results) != 0:
            return {"success":True, "data":"key alredy in use" }
        
        STATIC_SQL_COMMAND = f"INSERT INTO {DB_SYSTEM_TABLE} (uniq_key, value) VALUES (?, ?)"
        STATIC_DATA_TUPLE = (sql_key, key_value)
        db_cursor.execute(STATIC_SQL_COMMAND, STATIC_DATA_TUPLE)
        db.commit()
        return {"success":True, "data":"key and value successfuly inserted" }
    except Exception as err:
        return {"success":False, "data":f"data insert failed, {err}"}
    

def insertData_blobTable(db:sqlite3.Connection, db_cursor:sqlite3.Cursor, uniq_key:str, blob_data, data_type=DB_DATA_TYPE__USER,info_notes="NULL"):
    try:
        STATIC_SQL_COMMAND = f"SELECT * FROM {DB_BLOB_STORAGE} WHERE unique_blob_key=?"
        STATIC_DATA_TUPLE = (uniq_key)
        results = db_cursor.execute(STATIC_SQL_COMMAND,STATIC_DATA_TUPLE).fetchall()
        
        if len(results) != 0:
            return {"success":True, "data":"key alredy in use" }
        
        
        STATIC_SQL_COMMAND = f"INSERT INTO {DB_BLOB_STORAGE} (unique_blob_key, key_value, data_type, information_notes) VALUES (?, ?, ?, ?)"
        STATIC_DATA_TUPLE = (uniq_key, blob_data, data_type, info_notes)
        db_cursor.execute(STATIC_SQL_COMMAND, STATIC_DATA_TUPLE)
        db.commit()
        return { "success":True, "data":"key and value successfuly inserted" }
    
    except Exception as err:
        return { "success":False, "data":f"data insert failed, {err}" }
    
    
    
    
def is_authenticated(username:str, password:str,  db_cursor:sqlite3.Cursor) -> dict:
    """
    Yerel kimlik doğrulaması için otonom fonksiyon

    Args:
        username (str): doğrulama verisi
        password (str): doğrulama verisi
        db_cursor (sqlite3.Cursor): veritabanı ile iletişim için

    Returns:
        dict: { "success" -> Başarılı ise True değilse False, "data" -> durum için bilgi mesajı }
    """
    try:
        username = loginCreditHhasher(username)
        password = loginCreditHhasher(password)
    
        STATIC_SQL_COMMAND = f"SELECT * FROM {DB_LOCAL_AUTHENTICATE_TABLE} WHERE username=? AND password=?"
        STATIC_DATA_TUPLE = (username, password)
        
        result = db_cursor.execute(STATIC_SQL_COMMAND, STATIC_DATA_TUPLE).fetchall()
        
        if len(result) < 1:
            return {"success":False, "data":"user is not authenticated"}
        
        return {"success":True , "data":"user is authenticated"}
        
        
    except Exception as err:
        return {"success":False, "data":"database error"}
    
    


def generate_admin_accounts(username:str, password:str,db:sqlite3.Connection, db_cursor:sqlite3.Cursor) -> dict:
    try:
        STATIC_SQL_COMMAND = f"SELECT * FROM {DB_LOCAL_AUTHENTICATE_TABLE}"
        
        result = db_cursor.execute(STATIC_SQL_COMMAND).fetchall()
        
        if len(result) != 0:
            return {"success":False, "data":"only 1 user is acceptable"}
        
        username = loginCreditHhasher(username)
        password = loginCreditHhasher(password)
        
        STATIC_SQL_COMMAND = f"INSERT INTO {DB_LOCAL_AUTHENTICATE_TABLE} (username, password) VALUES (?, ?)"
        STATIC_DATA_TUPLE = (username, password)
        
        db_cursor.execute(STATIC_SQL_COMMAND,STATIC_DATA_TUPLE)
        db.commit()
        
        return {"success":True, "data":"user successfuly generated"}
            
    except Exception as err:
        return {"success":False , "data":f"database error: {err}"}
    
    
    
def change_admin_password(username:str, old_password:str, new_password:str, new_password_confirm:str) -> dict:
    pass
    

def check_admin_is_generated(db_cursor:sqlite3.Cursor) -> dict:
    try:
        STATIC_SQL_COMMAND = f"SELECT * FROM {DB_LOCAL_AUTHENTICATE_TABLE}"
        results = db_cursor.execute(STATIC_SQL_COMMAND).fetchall()
        
        if len(results) < 1:
            return { "success":False, "data":"no user in databsae" }
    
        return {"success":True, "data":"admin account successfuly"}
    
    except Exception as err:
        return {"success":False, "data":"database error"}