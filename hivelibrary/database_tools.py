from hivelibrary.env import DB_BLOB_STORAGE, DB_SYSTEM_TABLE, DB_LOCAL_AUTHENTICATE_TABLE
from hivelibrary.env import DB_DATA_TYPE__USER
from hivelibrary.env import APPLICATION_NAME_KEY
from hivelibrary.hash_tools import loginCreditHhasher
import psycopg2


from hivelibrary.types import t_PsqlCursor,t_PsqlCnn

def connection_function(db_config_dict) -> object:
    cnn= psycopg2.connect(**db_config_dict)
    cursor = cnn.cursor()
    return cnn, cursor


def check_db_init_status(db, db_cursor:t_PsqlCursor) -> bool:
    try:
        STATIC_SQL_COMMAND = "SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name=%s)"
        STATIC_DATA_TUPLE = (DB_SYSTEM_TABLE, )
        db_cursor.execute(STATIC_SQL_COMMAND, STATIC_DATA_TUPLE)
        results = db_cursor.fetchall()[0][0]
        if results == False:
            return False

        STATIC_SQL_COMMAND = f"SELECT EXISTS (SELECT 1 FROM {DB_SYSTEM_TABLE} WHERE unique_key=%s)"
        STATIC_DATA_TUPLE = (APPLICATION_NAME_KEY, )
        db_cursor.execute(STATIC_SQL_COMMAND, STATIC_DATA_TUPLE)
        results = db_cursor.fetchall()[0][0]
        if results == False:
            return False
        
        return True
    except Exception:
        return False


def check_exists_systemTable(db_curosr:t_PsqlCursor, sql_key:str) -> list[bool, str]:
    try:
        STATIC_SQL_COMMAND = f"SELECT * FROM {DB_SYSTEM_TABLE} WHERE unique_key=%s"
        STATIC_DATA_TUPLE = ( str(sql_key), )
        db_curosr.execute(STATIC_SQL_COMMAND, STATIC_DATA_TUPLE)
        results = db_curosr.fetchall()
        if len(results) < 1:
            return [ False, "Key not exists" ]
        return [ True, "key exists"]
    except Exception as err:
        return [ False, err ]
    

def insertData_systemTable(db:t_PsqlCnn, db_cursor:t_PsqlCursor, sql_key:str, key_value:str) -> dict:
    try:
        STATIC_SQL_COMMAND = f"SELECT * FROM {DB_SYSTEM_TABLE} WHERE unique_key=%s"
        STATIC_DATA_TUPLE = (sql_key,)
        db_cursor.execute(STATIC_SQL_COMMAND, STATIC_DATA_TUPLE)
        results = db_cursor.fetchall()
        if len(results) != 0:
            return {"success":True, "data":"key alredy in use" }
        
        STATIC_SQL_COMMAND = f"INSERT INTO {DB_SYSTEM_TABLE} (unique_key, value) VALUES (%s, %s)"
        STATIC_DATA_TUPLE = (sql_key, key_value)
        db_cursor.execute(STATIC_SQL_COMMAND, STATIC_DATA_TUPLE)
        db.commit()
        return {"success":True, "data":"key and value successfuly inserted" }
    except Exception as err:
        return {"success":False, "data":f"data insert failed, {err}"}
    



def insertData_blobTable(db, db_cursor, unique_key:str, blob_data, data_type=DB_DATA_TYPE__USER,info_notes="NULL"):
    try:
        STATIC_SQL_COMMAND = f"SELECT * FROM {DB_BLOB_STORAGE} WHERE unique_blob_key=%s"
        STATIC_DATA_TUPLE = (unique_key,)
        db_cursor.execute(STATIC_SQL_COMMAND,STATIC_DATA_TUPLE)
        results = db_cursor.fetchall()
        if len(results) != 0:
            return {"success":True, "data":"key alredy in use" }
        
        STATIC_SQL_COMMAND = f"INSERT INTO {DB_BLOB_STORAGE} (unique_blob_key, key_value, data_type, information_notes) VALUES (%s, %s, %s, %s)"
        STATIC_DATA_TUPLE = (unique_key, blob_data, data_type, info_notes)
        db_cursor.execute(STATIC_SQL_COMMAND, STATIC_DATA_TUPLE)
        db.commit()
        return { "success":True, "data":"key and value successfuly inserted" }
    
    except Exception as err:
        return { "success":False, "data":f"data insert failed, {err}" }
    
    
    
    
def is_authenticated(username:str, password:str,  db_cursor:t_PsqlCursor) -> dict:
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
        STATIC_SQL_COMMAND = f"SELECT * FROM {DB_LOCAL_AUTHENTICATE_TABLE} WHERE username=%s AND password=%s"
        STATIC_DATA_TUPLE = (username, password)
        db_cursor.execute(STATIC_SQL_COMMAND, STATIC_DATA_TUPLE)
        result = db_cursor.fetchall()
        if len(result) < 1:
            return {"success":False, "data":"user is not authenticated"}
        
        return {"success":True , "data":"user is authenticated"}
    except Exception as err:
        return {"success":False, "data":"database error"}
    
    


def generate_admin_accounts(username:str, password:str,db:t_PsqlCnn, db_cursor:t_PsqlCursor) -> dict:
    try:
        STATIC_SQL_COMMAND = f"SELECT * FROM {DB_LOCAL_AUTHENTICATE_TABLE}"
        db_cursor.execute(STATIC_SQL_COMMAND)
        result = db_cursor.fetchall()
        if len(result) != 0:
            return {"success":False, "data":"only 1 user is acceptable"}
        username = loginCreditHhasher(username)
        password = loginCreditHhasher(password)
        STATIC_SQL_COMMAND = f"INSERT INTO {DB_LOCAL_AUTHENTICATE_TABLE} (username, password) VALUES (%s, %s)"
        STATIC_DATA_TUPLE = (username, password)
        db_cursor.execute(STATIC_SQL_COMMAND,STATIC_DATA_TUPLE)
        db.commit()
        return {"success":True, "data":"user successfuly generated"}
    except Exception as err:
        return {"success":False , "data":f"database error: {err}"}
    
    
    
def change_admin_password(username:str, new_password:str, db, db_cursor ) -> dict:
    try:
        username = loginCreditHhasher(username)
        new_password = loginCreditHhasher(new_password)
        STATIC_SQL_COMMAND = f"UPDATE {DB_LOCAL_AUTHENTICATE_TABLE} SET password=%s WHERE username=%s"
        STATIC_DATA_TUPLE = (new_password, username)
        db_cursor.execute(STATIC_SQL_COMMAND, STATIC_DATA_TUPLE)
        db.commit()
        return {"success":True,"data":"Password successfuly updated"}
    except Exception as err:
        return {"success": False, "data":"database error"}
    

def check_admin_is_generated(db_cursor) -> dict:
    try:
        STATIC_SQL_COMMAND = f"SELECT * FROM {DB_LOCAL_AUTHENTICATE_TABLE}"
        db_cursor.execute(STATIC_SQL_COMMAND)
        results = db_cursor.fetchall()
        if len(results) < 1:
            return { "success":False, "data":"no user in databsae" }
        return {"success":True, "data":"admin account successfuly"}
    except Exception as err:
        return {"success":False, "data":"database error"}
    
    


def getValue_systemTable(db_cursor,sql_key) -> dict:
    try:
        pass
    except Exception as err:
        return { "success":False, "data":"database error" }