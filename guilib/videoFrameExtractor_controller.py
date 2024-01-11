from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal

from guilib.videoFrameExtractorScreen import Ui_video2framWidget

import os

class extractFrameThread(QThread):
    statusSignal = pyqtSignal(dict)
    
    def __init__(self, targetFilePath, OutputDirPath, ):
        super().__init__()
    
        self.targetFilePath = targetFilePath
        self.OutputDirPath = OutputDirPath
        
        self.threadStopSignal = False
           
    
    
    def stop(self):
        self.threadStopSignal = True
        msg = {"end":True,"success":False,
        "update_bar": True,
        "text":f"<B>INFO: </B>Thread killed by user!",
        "progress_value": 0 
        }
        self.statusSignal.emit(msg)
        return
    def run(self):
        msg = {"end": False,"success":None,"update_bar": False,
            "text":"<B>INFO:</B> Backend thread started.",
            "progress_value": 0}
        self.statusSignal.emit(msg)


        msg = {"end":False,"success":None,"update_bar": False,
            "text":"<B>WARNING: </B>Please note that the output size may be very high depending on the size of the video file.",
            "progress_value":0
        }
        self.statusSignal.emit(msg)

        
        
        msg = {"end":False,"success":None,"update_bar": False,
            "text":"<B>INFO: </B>importing cv2 (OpenCV)",
            "progress_value":0
        }
        self.statusSignal.emit(msg)
        import cv2
        try:
            prepared_video = cv2.VideoCapture(self.targetFilePath)
        except Exception as err:
            msg = {"end":True,"success":False,"update_bar": False,
                "text":f"<B>ERROR: </B>{err}",
                "progress_value":0
            }
            self.statusSignal.emit(msg)
            return
        
        msg = {"end":False,"success":None,"update_bar": False,
            "text":"<B>INFO: </B>Reading video and counting frames",
            "progress_value":0
        }
        self.statusSignal.emit(msg)
        
        totalFrame = 0
        while True:
            
            if self.threadStopSignal == True:
                return
            is_succes, _ = prepared_video.read()
            if is_succes:
                totalFrame += 1
            else:
                break
            
            if totalFrame % 1000 == 0:
                msg = {"end":False,"success":None,"update_bar": False,
            "text":f"<B>INFO: </B> Counting frame: <B>{totalFrame}</B> ",
            "progress_value":0
            }
                self.statusSignal.emit(msg)         
        
        msg = {"end":False,"success":None,"update_bar": False,
            "text":f"<B>INFO: </B> Total frame: <B>{totalFrame}</B> ",
            "progress_value":0
        }
        self.statusSignal.emit(msg)
        
        prepared_video.release()
        prepared_video = cv2.VideoCapture(self.targetFilePath)
        
        msg = {"end":False,"success":None,
            "update_bar": False,
            "text":f"<B>INFO: </B> Starting extractions ",
            "progress_value":0
        }
        self.statusSignal.emit(msg)
        
        save_number = 0
        while True :
            if self.threadStopSignal == True:
                return
            is_succes, now_frame = prepared_video.read()
            if is_succes:
                
                cv2.imwrite(f"{self.OutputDirPath}frame_{save_number}.png", now_frame)
                save_number += 1
            else:               
                msg = {"end":False,"success":None,
                "update_bar": True,
                "text":f"<B>INFO: </B>Status: {save_number}/{totalFrame}",
                "progress_value": 100
                }
                self.statusSignal.emit(msg)
                break
            
            if save_number % 10 == 0:
                msg = {"end":False,"success":None,
                "update_bar": True,
                "text":f"<B>INFO: </B>Status: {save_number}/{totalFrame}",
                "progress_value": int((save_number / totalFrame) *100 )
                }
                self.statusSignal.emit(msg)

    
        msg = {"end":True,"success":True,
        "update_bar": True,
        "text":f"<B>INFO: </B>Status: Complated!",
        "progress_value": 100 
        }
        self.statusSignal.emit(msg)
        
        
        
        
class VideoFrameExtractorPage(QWidget):
    def __init__(self):
        super().__init__()
        
        
        self.video2framePage = Ui_video2framWidget()
        self.video2framePage.setupUi(self)
        
        self.setWindowTitle("Video Frame Extractor")
        
        self.video2framePage.pushButton_selectOutputDir.clicked.connect(self.selectOutputDirectory)
        self.video2framePage.pushButton_selectVideoFile.clicked.connect(self.selectInputFile)
        self.video2framePage.pushButton_startExtraction.clicked.connect(self.startExtractions)
        self.video2framePage.pushButton_stopCurrentJob.clicked.connect(self.cancelProccess)
        
        
        self.targetVideoFile_is_selected = False
        self.targetOutputDir_is_selected = False
        self.resultPrinted = False
    
    def threadSignalHandler(self, result_dict):
        if result_dict["end"] == True and result_dict["success"] == True:
            self.video2framePage.textBrowser_logAndResults.append(str(result_dict["text"]))
            return
        
        
        if result_dict["update_bar"] == True:
            self.video2framePage.progressBar_statusPrinterBar.setValue(result_dict["progress_value"])
            
            if "text" in result_dict.keys():
                self.video2framePage.textBrowser_logAndResults.append(str(result_dict["text"]))
            return
        
        self.video2framePage.textBrowser_logAndResults.append(str(result_dict["text"]))
    
    
    
    
    def selectOutputDirectory(self):
        self.targetOutputDir_is_selected = False
        folder_dialog = QFileDialog()
        folder_dialog = QFileDialog.getExistingDirectory(self,"Select Ouput Directory")

        if folder_dialog:
            if os.name == "nt":
                check_digit = str(folder_dialog[-2:])
                if not str(os.path.sep) in check_digit:
                    folder_dialog = str(folder_dialog) + str(os.path.sep)
            else:
                check_digit = str(folder_dialog[-1])
                if not str(os.path.sep) in check_digit:
                    folder_dialog = str(folder_dialog) + str(os.path.sep)

        if folder_dialog == None or not os.path.exists(folder_dialog) or not os.path.isdir(folder_dialog):
            err_msg = "Error: Invalid file selections"
            self.video2framePage.textBrowser_outputDirPathPrint.setText(err_msg)
            return
        
        if len(os.listdir(folder_dialog)) != 0:
            err_msg = "Error: Selected directory not empty"
            self.video2framePage.textBrowser_outputDirPathPrint.setText(err_msg)
            return          
        
        self.selectOutputDirectory = folder_dialog
        self.targetOutputDir_is_selected = True
        self.video2framePage.textBrowser_outputDirPathPrint.setText(folder_dialog)
        
        
    
    def cancelProccess(self):
        if not self.backEndWorkerThread.isRunning():
            err_msg = "<B>ERROR: </B>No running jobs!"
            self.video2framePage.textBrowser_logAndResults.append(err_msg)
            return
        
        
        info_msg = "<B>INFO: </B>Sending kill signal..."
        self.video2framePage.textBrowser_logAndResults.append(info_msg)
        self.backEndWorkerThread.stop()

    
    def selectInputFile(self):
        self.targetVideoFile_is_selected = False
        file_dialog =  QFileDialog()
        file_dialog.setNameFilter("Video Files (*.avi *.mp4 *.mkv *.mov *.flv *.wmv *.webm *.mpeg *.mpg)")

        if file_dialog.exec_():
            self.targetVideoFile = file_dialog.selectedFiles()[0]
        
        if self.targetVideoFile == None or not os.path.exists(self.targetVideoFile) or not os.path.isfile(self.targetVideoFile):
            err_msg = "Error: Invalid file selections"
            self.video2framePage.textBrowser_inputFilePathPrint.setText(err_msg)
            return
        
        
        self.selectInputFile = self.targetVideoFile
        self.targetVideoFile_is_selected = True
        self.video2framePage.textBrowser_inputFilePathPrint.setText(self.targetVideoFile)
    

    def clearLogResultConsole(self):
        self.video2framePage.textBrowser_logAndResults.clear()
        self.video2framePage.textBrowser_logAndResults.setText(f"<B>LOG AND RESULTS: </B><br>")
    
    def startExtractions(self):
        self.resultPrinted = False
        self.clearLogResultConsole()
        
        if self.targetOutputDir_is_selected != True or self.targetOutputDir_is_selected!= True:
            self.video2framePage.textBrowser_logAndResults.append(f"<B>ERROR: </B>Video or directory not selected!")
            return
        
        self.backEndWorkerThread = extractFrameThread(targetFilePath=self.selectInputFile,OutputDirPath=self.selectOutputDirectory)
        self.backEndWorkerThread.statusSignal.connect(self.threadSignalHandler)
        self.backEndWorkerThread.start()
    
    
