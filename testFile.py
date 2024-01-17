from guilib.TcNumberValidationChecker_controller import TcValidatorCheckerWidget
from PyQt5.QtWidgets import *
            
if __name__ == "__main__":
    app = QApplication([])
    win = TcValidatorCheckerWidget()
    win.show()
    app.exec_()