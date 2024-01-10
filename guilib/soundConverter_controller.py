from PyQt5.QtWidgets import *

from guilib.soundConverterScreen import Ui_SounConverter_widget
from hivelibrary.sound_converter import *

import shutil
import os

class soundConverterPage(QWidget):
    def __init__(self, output_dir:str, temp_dir:str):
        super().__init__()
        
        if not str(os.sep) in temp_dir:
            temp_dir += str(os.sep)
        
        if not str(os.sep) in output_dir:
            output_dir+= str(os.sep)
        
        self.soundConverterWidget = Ui_SounConverter_widget()
        self.soundConverterWidget.setupUi(self)
        
        self.OUTPUT_DIRECTORY = output_dir
        self.TEMP_DIRECTORY = temp_dir
        self.soundConverterSelectedFile = None
        
        self.setWindowTitle("Sound Converter")
        
        self.soundConverterWidget.pushButton_soundConverter_selectSoundFile.clicked.connect(self.soundConverterSelectTargetFile)
        self.soundConverterWidget.pushButton_soundConverter_runConvert.clicked.connect(self.soundConverterRunConvert)
        
        
    def clearSoundConverterLogConsole(self):
        self.soundConverterWidget.textBrowser_soundConverter_logConsole.clear()
        self.soundConverterWidget.textBrowser_soundConverter_logConsole.setText(f"<B>Log Console: </B><br>")
        
        
    def soundConverterRunConvert(self):
        self.clearSoundConverterLogConsole()
        if self.soundConverterSelectedFile == None or not os.path.exists(self.soundConverterSelectedFile) or not os.path.isfile(self.soundConverterSelectedFile):
            err_msg = "Error: Invalid file selections"
            self.soundConverterWidget.textBrowser_soundConverter_sourceFile_print.setText(err_msg)
            return
        
        output_name = self.soundConverterWidget.lineEdit_soundConverter_outputName_input.text()
        target_format = self.soundConverterWidget.comboBox_soundConverter_selectTargetFormat.currentText()
        
        if output_name.split(".")[-1].upper() in SUPPORTED_SOUND_FORMATS:
            err_msg = "[ - ] Error: Not add extensions in output name!"
            self.soundConverterWidget.textBrowser_soundConverter_logConsole.append(err_msg)
            return
        
        if self.soundConverterSelectedFile.split(".")[-1].upper() == target_format.upper():
            err_msg = "[ - ] Error: Input format == output format proccess stopped!"
            self.soundConverterWidget.textBrowser_soundConverter_logConsole.append(err_msg)
            return
        
        self.soundConverterWidget.textBrowser_soundConverter_logConsole.append("[ + ] Starting convert")

        
        convert_status = GenericAudioConverter(target_file_path=self.soundConverterSelectedFile, temp_dir_path=self.TEMP_DIRECTORY,TARGET_FILE_FORMAT=target_format)
        if convert_status["success"] != "true":
            self.soundConverterWidget.textBrowser_soundConverter_logConsole.append(f"[ - ] Converting failed: {convert_status['code']}")
            return
        
        raw_path_output = convert_status["path"]
        finally_output_name = output_name + "." + target_format
        finally_output_name = self.OUTPUT_DIRECTORY + finally_output_name
        
        shutil.copyfile(src=raw_path_output, dst=finally_output_name)

        self.soundConverterWidget.textBrowser_soundConverter_logConsole.append(f"[ + ] Removing temp files")
        os.remove(raw_path_output)
            
            
        the_final_message = f"[ + ] Proccess successfuly complated.<br>[ + ] Your file: {finally_output_name}<br>"
        self.soundConverterWidget.textBrowser_soundConverter_logConsole.append(the_final_message)
    
    
    def soundConverterSelectTargetFile(self):
        file_dialog =  QFileDialog()
        file_dialog.setNameFilter("Sound Files (*.mp3 *.vaw *.flac *.opus *.ogg *.aac *.wma)")

        if file_dialog.exec_():
            self.soundConverterSelectedFile = file_dialog.selectedFiles()[0]
        
        if self.soundConverterSelectedFile == None or not os.path.exists(self.soundConverterSelectedFile) or not os.path.isfile(self.soundConverterSelectedFile):
            err_msg = "Error: Invalid file selections"
            self.soundConverterWidget.textBrowser_soundConverter_sourceFile_print.setText(err_msg)
            return
        
        self.soundConverterWidget.textBrowser_soundConverter_sourceFile_print.setText(self.soundConverterSelectedFile)