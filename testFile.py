from guilib.IPtracerBasic_controller import BasicIPtracerWidget


from PyQt5.QtWidgets import *



app = QApplication([])
win = BasicIPtracerWidget()
win.show()
app.exec_()