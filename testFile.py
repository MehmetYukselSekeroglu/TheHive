from guilib.FaceRecognition_controller import FaceRecognitionWidget
from PyQt5.QtWidgets import *
from hivelibrary.database_structure import FACE_RECOGNITION_DATABASE_STRUCTUR_COMMAND
from hivelibrary.face_recognition_database_tools import recognitionDbTools
import sqlite3 
#import cv2
#import insightface
if __name__ == "__main__":

    db = sqlite3.connect("hive_database.sqlite3",check_same_thread=False)
    db_curosr = db.cursor()

    
    app = QApplication([])
    win = FaceRecognitionWidget(db_cnn=db,db_curosr=db_curosr)
    win.show()
    app.exec_()
    