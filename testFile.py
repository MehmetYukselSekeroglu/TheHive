from guilib.TcNumberCalculator_controller import TcCalculatorWidget
from PyQt5.QtWidgets import *
            
if __name__ == "__main__":
    app = QApplication([])
    win = TcCalculatorWidget()
    win.show()
    app.exec_()