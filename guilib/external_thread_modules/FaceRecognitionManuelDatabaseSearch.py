from PyQt5.QtCore import QThread, pyqtSignal
import sqlite3
from guilib.html_text_generator.html_draft import gen_error_text,gen_info_text
from hivelibrary.env import DB_FACE_RECOGNITION_TABLE

class manuelDatabaseSearcherThread(QThread):
    threadSignal = pyqtSignal(dict)
    
    
    def __init__(self, db_cnn:sqlite3.Connection, db_curosr:sqlite3.Cursor,search_keywords:str, selected_search:int):
        super().__init__()
        
        
        self.databaseConnections = db_cnn
        self.databaseCursor = db_curosr
        self.searchKeyword = search_keywords
        self.searchType = selected_search
        
    
    def __status(self,text):
        data_dict = { "success":None, "end":False, "text":text, "data":None }
        self.threadSignal.emit(data_dict)
    
    
    
    def __finaly(self, success_status:bool, data, text:str):
        data_dict = {"success":success_status, "end":True, "data":data, "text":text}
        self.threadSignal.emit(data_dict)
        
        
        
    def run(self):
        self.__status(text=gen_info_text("Arama işlemi başladıldı."))
        if self.searchType == 0:
            STATIC_SQL_COMMAND = f"SELECT * FROM {DB_FACE_RECOGNITION_TABLE} WHERE face_name LIKE ?"
            searchString = "%"+str(self.searchKeyword)+"%"
            STATIC_DATA_TUPLE = (searchString, )
            
            try:
                resutls = self.databaseConnections.execute(STATIC_SQL_COMMAND,STATIC_DATA_TUPLE).fetchall()
                if len(resutls) < 1:
                    self.__finaly(success_status=False,data=None,text=gen_error_text("ilgili terim için veritabanında sonuç bulunamadı"))
                    return
                
                self.__finaly(success_status=True,data=resutls,text=gen_info_text(f"İşlem başarıyla tamamlandı, toplam {len(resutls)} sonuç var."))
                return
            except Exception as err:
                self.__finaly(success_status=False, data=None,text=gen_error_text(f"İşlem sistemsel hata nedeniyle başarısız oldu, sebep {err}"))
                return
            
        
        # resim sha1 ile arama 
        if self.searchType == 1:
            STATIC_SQL_COMMAND = f"SELECT * FROM {DB_FACE_RECOGNITION_TABLE} WHERE picture_sha1_hash LIKE ?"
            searchString = "%"+str(self.searchKeyword)+"%"
            STATIC_DATA_TUPLE = (searchString, )
            
            try:
                resutls = self.databaseConnections.execute(STATIC_SQL_COMMAND,STATIC_DATA_TUPLE).fetchall()
                if len(resutls) < 1:
                    self.__finaly(success_status=False,data=None,text=gen_error_text("ilgili terim için veritabanında sonuç bulunamadı"))
                    return
                
                self.__finaly(success_status=True,data=resutls,text=gen_info_text(f"İşlem başarıyla tamamlandı, toplam {len(resutls)} sonuç var."))
                return
            except Exception as err:
                self.__finaly(success_status=False, data=None,text=gen_error_text(f"İşlem sistemsel hata nedeniyle başarısız oldu, sebep {err}"))
                return
            
        # tüm kayıtları getirme
        if self.searchType == 2:
            STATIC_SQL_COMMAND = f"SELECT * FROM {DB_FACE_RECOGNITION_TABLE}"
            try:
                resutls = self.databaseConnections.execute(STATIC_SQL_COMMAND).fetchall()
                if len(resutls) < 1:
                    self.__finaly(success_status=False,data=None,text=gen_error_text("ilgili terim için veritabanında sonuç bulunamadı"))
                    return
                
                self.__finaly(success_status=True,data=resutls,text=gen_info_text(f"İşlem başarıyla tamamlandı, toplam {len(resutls)} sonuç var."))
                return
            except Exception as err:
                self.__finaly(success_status=False, data=None,text=gen_error_text(f"İşlem sistemsel hata nedeniyle başarısız oldu, sebep {err}"))
                return
        