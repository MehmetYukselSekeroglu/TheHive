from PyQt5.QtWidgets import*
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
from guilib.voiceVerificationScreen import Ui_voiceVerificationWidget
from hivelibrary.sound_converter import ConvertAnyAudio_to_wav
from hivelibrary.identify.voice_comparsion import CompareSounds
from hivelibrary.env import DEFAULT_TEMP_DIR
import os


class comparsionThread(QThread):
    statusSignal = pyqtSignal(dict)
    
    def __init__(self ,file_path_1:str, file_path_2:str,temp_dir_path:str):
        super().__init__()
        
        self.raw_file_1 = file_path_1
        self.raw_file_2 = file_path_2
        self.temp_dir_path = temp_dir_path
        
        if not str(os.sep) in self.temp_dir_path:
            self.temp_dir_path += str(os.sep)
            
    def run(self):
        msg = {"end":False,"text":"<B>INFO:</B> Backend thread started."}
        self.statusSignal.emit(msg)
        msg = {"end":False,"success":None,"text":"<B>INFO:</B> Conversion of input files to vaw format has started."}
        self.statusSignal.emit(msg)
        raw_file_1_convert_status = ConvertAnyAudio_to_wav(target_file_path=self.raw_file_1,temp_dir_path=self.temp_dir_path)
        raw_file_2_convert_status = ConvertAnyAudio_to_wav(target_file_path=self.raw_file_2,temp_dir_path=self.temp_dir_path)
        if raw_file_1_convert_status["success"] == "false" or raw_file_2_convert_status["success"] == "false":
            msg = {"end":True, "success":False,"text":"<B>ERROR:</B> File conversion failed, proccess stoping."}
            self.statusSignal.emit(msg)
            return
        
        vaw_file_1 = raw_file_1_convert_status["path"]
        vaw_file_2 = raw_file_2_convert_status["path"]

        msg = {"end":False,"success":None,"text":"<B>INFO: </B>Comparing voice similarity rates..."}
        self.statusSignal.emit(msg)
        
        try:
            finally_status = CompareSounds(vaw_file_1, vaw_file_2)
        except Exception as err:
            finally_status = {"success":False, "code":err}
        
        if not finally_status["success"] == True:
            msg = {"end": True,"success": False,"text":f"<B>ERROR:</B> Audio comparison failed api feedback: {finally_status['code']}, proccess stoping."}
            self.statusSignal.emit(msg)
            os.remove(vaw_file_1)
            os.remove(vaw_file_2)
            return
        
        ses_benzerlik_oranı = finally_status["similarity"]
        msg = {"end":True,"success":True,"text":ses_benzerlik_oranı}
        os.remove(vaw_file_1)
        os.remove(vaw_file_2)
        self.statusSignal.emit(msg)
        

class voiceVerificationPage(QWidget):
    def __init__(self, temp_dir:str):
        super().__init__()
        
        self.voiceVerifyWidget = Ui_voiceVerificationWidget()
        self.voiceVerifyWidget.setupUi(self) 
        
        if not str(os.sep) in temp_dir:
            temp_dir += str(os.sep)
        self.TEMP_DIRECTORY = temp_dir
        
        
        self.file_1_selected = False
        self.file_2_selected = False
        self.resultPrinted = False
        
        self.setWindowTitle("Voice Verification")
        self.voiceVerifyWidget.widget_3_similarityProgressBar.setVisible(False)
        
        self.voiceVerifyWidget.pushButton_selectFile1.clicked.connect(self.selectTargetFile_1)
        self.voiceVerifyWidget.pushButton_selectFile2.clicked.connect(self.selectTargetFile_2)
        self.voiceVerifyWidget.pushButton_saveResults.clicked.connect(self.saveOutputResult)
        self.voiceVerifyWidget.pushButton_runComparsion.clicked.connect(self.runVoiceVerification)
        
        
    def saveOutputResult(self):
        saveFileName, _ = QFileDialog.getSaveFileName(self, "Save Result",filter="Text file (*.txt)")
        if not saveFileName:
            err_msg = f"[ - ] Save file not selected"
            self.voiceVerifyWidget.textBrowser_logAndResults.append(err_msg)
            return         
                
        if self.resultPrinted != True:
            err_msg = f"[ - ] There are no results to save"
            self.voiceVerifyWidget.textBrowser_logAndResults.append(err_msg)
            return
                
        self.voiceVerifyWidget.textBrowser_logAndResults.append(str("-"*30))
        self.voiceVerifyWidget.textBrowser_logAndResults.append("[ + ] Saving operation started")
        with open(saveFileName, "w") as saveFile:
            saveFile.write(self.for_save_data)
        self.voiceVerifyWidget.textBrowser_logAndResults.append("[ + ] File successfuly saved ")
    
    
    
    def clearLogResultConsole(self):
        self.voiceVerifyWidget.textBrowser_logAndResults.clear()
        self.voiceVerifyWidget.textBrowser_logAndResults.setText(f"<B>LOG AND RESULTS: </B><br>")
        self.voiceVerifyWidget.widget_3_similarityProgressBar.setVisible(False)
        
        
        
        
    def selectTargetFile_1(self):
        self.file_1_selected = False
        file_dialog =  QFileDialog()
        file_dialog.setNameFilter("Sound Files (*.mp3 *.vaw *.flac *.opus *.ogg *.aac *.wma *.m4a)")

        if file_dialog.exec_():
            self.selectedTargetFile_1 = file_dialog.selectedFiles()[0]
        else:
            self.selectedTargetFile_1 = None
        
        if self.selectedTargetFile_1 == None or not os.path.exists(self.selectedTargetFile_1) or not os.path.isfile(self.selectedTargetFile_1):
            err_msg = "Error: Invalid file selections"
            self.voiceVerifyWidget.textBrowser_voice1showPath.setText(err_msg)
            return
        
        self.voiceVerifyWidget.textBrowser_voice1showPath.setText(self.selectedTargetFile_1)
        self.file_1_selected = True
        
        
        
    def selectTargetFile_2(self):
        self.file_2_selected = False
        file_dialog =  QFileDialog()
        file_dialog.setNameFilter("Sound Files (*.mp3 *.vaw *.flac *.opus *.ogg *.aac *.wma *.m4a)")

        if file_dialog.exec_():
            self.selectedTargetFile_2 = file_dialog.selectedFiles()[0]
        else:
            self.selectedTargetFile_2 = None
        
        if self.selectedTargetFile_2 == None or not os.path.exists(self.selectedTargetFile_2) or not os.path.isfile(self.selectedTargetFile_2):
            err_msg = "Error: Invalid file selections"
            self.voiceVerifyWidget.textBrowser_voice2showPath.setText(err_msg)
            return
        
        self.voiceVerifyWidget.textBrowser_voice2showPath.setText(self.selectedTargetFile_2)
        self.file_2_selected = True
    
    
    def runVoiceVerification(self):
        self.resultPrinted = False
        self.clearLogResultConsole()
        if self.file_1_selected != True or self.file_2_selected != True:
            self.voiceVerifyWidget.textBrowser_logAndResults.append(f"<B>ERROR: </B>Sound file or files not selected!")
            return
        
        self.backEndWorkerThread = comparsionThread(file_path_1=str(self.selectedTargetFile_1), file_path_2=str(self.selectedTargetFile_2),temp_dir_path=DEFAULT_TEMP_DIR)
        self.backEndWorkerThread.statusSignal.connect(self.threadStatusHandler)
        self.backEndWorkerThread.start()
        
        
    
    def threadStatusHandler(self,result_dict:dict):
        
        if result_dict["end"] == True and result_dict["success"] == True:
            similarity_rate = result_dict["text"]
            self.resultPrinted = True
                        
            if int(similarity_rate) < 60:
                data_status = "Aynı kişi olma ihtimali çok düşük"
            elif int(similarity_rate) < 70 and int(similarity_rate) > 60:
                data_status = "Aynı kişi olma ihtimali düşük"    
            elif int(similarity_rate) >= 70:
                data_status = "Aynı kişi olma ihtimali çok yüksektir"
            
            self.voiceVerifyWidget.textBrowser_logAndResults.append(f"<B>INFO: </B>Proccess successfuly.")
            self.voiceVerifyWidget.textBrowser_logAndResults.append(f"<B>INFO: </B>{'-'*20}")
            self.voiceVerifyWidget.textBrowser_logAndResults.append(f"Similarity rate: %{similarity_rate}")
            self.voiceVerifyWidget.textBrowser_logAndResults.append(data_status)
            self.voiceVerifyWidget.textBrowser_logAndResults.append(f"<B>INFO: </B>{'-'*20}")
            self.voiceVerifyWidget.widget_3_similarityProgressBar.setVisible(True)
            self.voiceVerifyWidget.progressBar_similarityShower.setValue(int(similarity_rate))
            self.for_save_data = f"""TheHive Remastred | Voice Verification
Date: None
Voice 1 Path: {self.selectedTargetFile_1}
Voice 2 Path: {self.selectedTargetFile_2}
Similarity Rate: %{similarity_rate}
Message: {data_status}
"""         
            return
        self.voiceVerifyWidget.textBrowser_logAndResults.append(str(result_dict["text"]))
    