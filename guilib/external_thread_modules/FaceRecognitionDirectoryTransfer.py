from PyQt5.QtCore import QThread, pyqtSignal
import os
import threading
import time

from guilib.html_text_generator.html_draft import *
from hivelibrary.face_recognition_database_tools import recognitionDbTools
from hivelibrary.os_information import max_thread_calculator
from hivelibrary.database_tools import connection_function
from hivelibrary.psqlConfig import POSTGRESQL_CONFIG


class directoryAdderThread(QThread):

    statusSignal = pyqtSignal(dict)
    
    
    def __init__(self, faceAnalayserUI:object ,targetDirectory:str, databaseConnections, databaseCursor):
        super().__init__()
        
        self.connectionConfig = POSTGRESQL_CONFIG
        self.targetDirectory = targetDirectory
        self.databaseConnections = databaseConnections
        self.databaseCursor = databaseCursor
        self.faceAnalayserUI = faceAnalayserUI
        self.threadKillStatus = False
        self.supportedFromats = [".jpg", ".jpeg", ".png", ".webm" ]
        
        
        
        self.maxThreadCount = max_thread_calculator()
        self.THREAD_STORAGE_ARRAY = []
        
        self.totalAddedCount = 0
        self.totalIslenen = 0
        
        
        
        if os.name == "nt":
            check_digit = str(self.targetDirectory[-2:])
            if not str(os.path.sep) in check_digit:
                self.targetDirectory = str(self.targetDirectory) + str(os.path.sep)
        else:
            check_digit = str(self.targetDirectory[-1])
            if not str(os.path.sep) in check_digit:
                self.targetDirectory = str(self.targetDirectory) + str(os.path.sep)
    
    
    

    
    def run(self):
        import cv2
        from hivelibrary.file_operations.generic_tools import binaryData
        

        
        totalFile = len(os.listdir(self.targetDirectory))
        
        
        
        self.__runningStatus(text="Ekleme sistemi başlatıldı")
        self.__runningStatus(text=f"Kullanılan thread sayısı: {self.maxThreadCount}")
        
        for singleFile in os.listdir(self.targetDirectory):
            if self.threadKillStatus == True:
                return_text = f"""<B>İşlem İptal edildi son durum</B><br>
<B>Toplam klasör içeriği: </B>{totalFile}<br>
<B>Toplam eklenen resim:  </B>{self.totalAddedCount}<br>
<B>Toplam işlemden geçirilen resim: </B>{self.totalIslenen} <br>
<B>Eklenemeyen, atlanan resim: </B> {str(self.totalIslenen - self.totalAddedCount)}<br>
{"-"*20}<br>"""
                self.__runningStatus(text=return_text)
                self.__finalyStatus(text=gen_info_text("Thread killed by user"),success_status=False)
                return 


            

            def thread_function(database_connection_func,signleTarget) -> None:
                try:
                    
                    db, db_curosr = database_connection_func(self.connectionConfig)
                    
                    databaseTools = recognitionDbTools(db_cnn=db,db_curosr=db_curosr)
                    fullImagePath = str(self.targetDirectory + signleTarget)

                    if not os.path.isfile(fullImagePath):
                        self.__runningStatus(text=gen_info_text(f"Dosya bir dizin bu nedenle atlandı: {signleTarget}"))
                        db.close()
                        return
                    
                    file_name, currentExtensions = os.path.splitext(fullImagePath)
                    file_name = file_name.split(str(os.path.sep))[-1]
                    if not currentExtensions.endswith(".png") and not currentExtensions.endswith(".jpg") and not currentExtensions.endswith(".jpeg") and not currentExtensions.endswith(".webm"):
                        self.__runningStatus(text=gen_info_text(f"Desteklenmeyen dosya uzantısı atlandı : {signleTarget}"))
                        db.close()
                        return
                    
                    cv2_data = cv2.imread(fullImagePath)
                    binary_data = binaryData(fullImagePath)

                    results = databaseTools.insertImageFromDB(
                        cv2_image_data=cv2_data,
                        image_binary_data=binary_data,face_name=file_name,
                        insightface_face_analyser_ojb=self.faceAnalayserUI
                        )

                    if results["success"] == True:
                        self.totalAddedCount += 1
                    else:
                        self.__runningStatus(text=gen_error_text(f"{results['data']}, {signleTarget} "))

                    self.totalIslenen +=1
                    if self.totalIslenen % 10 == 0:
                        self.__runningStatus(text=gen_info_text(f"Durum: {totalFile}/{self.totalIslenen}"))

                    db.close()
                    return

                except Exception as err:
                    self.__runningStatus(text=gen_error_text(f"Hata nedeniyle dosya atlandı, {err}"))
                    db.close()
                    return
            
            if threading.active_count() <= self.maxThreadCount:
                worker_thread = threading.Thread(
                    daemon=True,
                    target=thread_function,
                    args=(connection_function,singleFile)
                )
                worker_thread.start()
            else:
                
                while threading.active_count() > self.maxThreadCount:
                    time.sleep(0.5)
                    continue
                            
                worker_thread = threading.Thread(
                    daemon=True,
                    target=thread_function,
                    args=(connection_function,singleFile)
                )
                worker_thread.start()
                
            

                
                
        
                
        self.__runningStatus(text=gen_info_text(f"Durum: {totalFile}/{self.totalAddedCount}"))    
        return_text = f"""<B>İşlem Başarıyla Tamamlandı</B><br>
<B>Toplam klasör içeriği: </B>{totalFile}<br>
<B>Toplam eklenen resim:  </B>{self.totalAddedCount}<br>
<B>Toplam işlemden geçirilen resim: </B>{self.totalIslenen} <br>
<B>Eklenemeyen, atlanan resim: </B> {str(self.totalIslenen - self.totalAddedCount)}<br>
{"-"*20}<br>"""
        self.__finalyStatus(success_status=True,text=return_text)

    
    def stop(self):
        self.threadKillStatus = True
    
    def __runningStatus(self, text:str):
        data_dict = { "success":None, "end":False, "text":text}
        self.statusSignal.emit(data_dict)
        
    def __finalyStatus(self, text:str, success_status:bool):
        data_dict = {"success":success_status, "end":True, "text":text }
        self.statusSignal.emit(data_dict)