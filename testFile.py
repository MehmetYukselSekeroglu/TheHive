from guilib.FaceDetection_controller import *




if __name__ == "__main__":
    q_app = QApplication([])
    win = FaceDetectionWidget()
    win.show()
    q_app.exec_()