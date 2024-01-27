from PyQt5.QtCore import QObject, QThread, pyqtSignal




class analaysThread(QThread):
    statusSignal = pyqtSignal(dict)
    
    
    def __init__(self, targetFilePath:str, targetFileFormat:str) -> None:
        super().__init__()
        
        
        
    def run(self):
        pass