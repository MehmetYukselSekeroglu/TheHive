from guilib.HtsAnalaysis_controller import HTS_analaysisWidget
from PyQt5.QtWidgets import *
from hivelibrary.database_structure import FACE_RECOGNITION_DATABASE_STRUCTUR_COMMAND

import sqlite3 
#import cv2
#import insightface
if __name__ == "__main__":
    app = QApplication([])
    win = HTS_analaysisWidget()
    win.show()
    app.exec_()
    