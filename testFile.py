from guilib.FaceVerificationFromImage_controller import *

if __name__ == "__main__":
    q_app = QApplication([])
    win = FaceVerificationScreen_from_image()
    win.show()
    q_app.exec_()