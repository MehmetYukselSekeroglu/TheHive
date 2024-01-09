from PyQt5.QtWidgets import *
from guilib.coomingSoonScreen import Ui_CoomingSoonScreen



class CoomingSoonPage(QWidget):
    def __init__(self, outputMessage:str):
        super().__init__()
        self.coomingPage = Ui_CoomingSoonScreen()
        self.coomingPage.setupUi(self)
        self.setWindowTitle("Coooming Soon")
        self.outputMessage = outputMessage
        self.coomingPage.textBrowser_infotmationPage.setHtml(outputMessage)