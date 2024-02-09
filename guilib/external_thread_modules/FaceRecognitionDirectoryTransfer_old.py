from PyQt5.QtCore import QThread, pyqtSignal
import os

from guilib.html_text_generator.html_draft import *
from hivelibrary.face_recognition_database_tools import recognitionDbTools


class directoryAdderThread(QThread):

    statusSignal = pyqtSignal(dict)
    
    
    def __init__(self, faceAnalayserUI:object ,targetDirectory:str, databaseConnections, databaseCursor):
        super().__init__()
        
        self.targetDirectory = targetDirectory
        self.databaseConnections = databaseConnections
        self.databaseCursor = databaseCursor
        self.faceAnalayserUI = faceAnalayserUI
        self.threadKillStatus = False
        self.supportedFromats = [".jpg", ".jpeg", ".png", ".webm" ]
        
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
        
        totalAddedCount = 0
        totalIslenen = 0
        
        totalFile = len(os.listdir(self.targetDirectory))
        
        databaseTools = recognitionDbTools(db_cnn=self.databaseConnections,db_curosr=self.databaseCursor)
        
        self.__runningStatus(text="Ekleme sistemi başlatıldı")
        
        for singleFile in os.listdir(self.targetDirectory):
            if self.threadKillStatus == True:
                return_text = f"""<B>İşlem İptal edildi son durum</B><br>
<B>Toplam klasör içeriği: </B>{totalFile}<br>
<B>Toplam eklenen resim:  </B>{totalAddedCount}<br>
<B>Toplam işlemden geçirilen resim: </B>{totalIslenen} <br>
<B>Eklenemeyen, atlanan resim: </B> {str(totalIslenen - totalAddedCount)}<br>
{"-"*20}<br>"""
                self.__runningStatus(text=return_text)
                self.__finalyStatus(text=gen_info_text("Thread killed by user"),success_status=False)
                return 
            try:
                fullImagePath = str(self.targetDirectory + singleFile)
            
                if not os.path.isfile(fullImagePath):
                    self.__runningStatus(text=gen_info_text(f"Dosya bir dizin bu nedenle atlandı: {singleFile}"))
                    continue
            
                file_name, currentExtensions = os.path.splitext(fullImagePath)
                file_name = file_name.split(str(os.path.sep))[-1]
                if not currentExtensions.endswith(".png") and not currentExtensions.endswith(".jpg") and not currentExtensions.endswith(".jpeg") and not currentExtensions.endswith(".webm"):
                    self.__runningStatus(text=gen_info_text(f"Desteklenmeyen dosya uzantısı atlandı : {singleFile}"))
                    continue
                
                cv2_data = cv2.imread(fullImagePath)
                binary_data = binaryData(fullImagePath)

                results = databaseTools.insertImageFromDB(cv2_image_data=cv2_data,image_binary_data=binary_data
                    ,face_name=file_name,insightface_face_analyser_ojb=self.faceAnalayserUI)
            
                if results["success"] == True:
                    totalAddedCount += 1
                else:
                    
                    self.__runningStatus(text=gen_error_text(f"{results['data']}, {singleFile} "))
                
                totalIslenen +=1
                if totalIslenen % 10 == 0:
                    self.__runningStatus(text=gen_info_text(f"Durum: {totalFile}/{totalIslenen}"))

            
            except Exception as err:
                self.__runningStatus(text=gen_error_text(f"Hata nedeniyle dosya atlandı, {err}"))
                continue
            
                
        self.__runningStatus(text=gen_info_text(f"Durum: {totalFile}/{totalAddedCount}"))    
        return_text = f"""<B>İşlem Başarıyla Tamamlandı</B><br>
<B>Toplam klasör içeriği: </B>{totalFile}<br>
<B>Toplam eklenen resim:  </B>{totalAddedCount}<br>
<B>Toplam işlemden geçirilen resim: </B>{totalIslenen} <br>
<B>Eklenemeyen, atlanan resim: </B> {str(totalIslenen - totalAddedCount)}<br>
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