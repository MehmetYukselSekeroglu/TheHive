from guilib.FaceRecognition_controller import FaceRecognitionWidget
from PyQt5.QtWidgets import *
            
if __name__ == "__main__":
    app = QApplication([])
    win = FaceRecognitionWidget()
    win.show()
    app.exec_()