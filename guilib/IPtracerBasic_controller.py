from guilib.IPtracerBasicScreen import Ui_IPTracerWidget_ipinfoio
from guilib.html_text_generator.html_draft import gen_error_text,gen_info_text

from PyQt5.QtWidgets import *
from PyQt5 import QtGui 
from PyQt5 import QtCore


from hivelibrary.env import DEFAULT_LOGO_PATH
from hivelibrary.map_tools import drawNewMap
from hivelibrary.osint.reverse_ip import reverseIpLookup_ipinfoio

class BasicIPtracerWidget(QWidget):
    
    def __init__(self):
        super().__init__()
    
    
        self.BasicIpTracer = Ui_IPTracerWidget_ipinfoio()
        self.BasicIpTracer.setupUi(self)
        self.setWindowTitle("IP Tracer Basic")
        self.BasicIpTracer.textBrowser_logConsole.setText("<B>LOG CONSOLE:</B>")
        
        self.showDefaultMap()
        
        self.BasicIpTracer.pushButton_clearResults.clicked.connect(self.clearOutputs)
        self.BasicIpTracer.pushButton_startQuery.clicked.connect(self.startIpTracer)



    def startIpTracer(self):
        self.showDefaultMap()
        self.BasicIpTracer.textBrowser_logConsole.setText("<B>LOG CONSOLE:</B>")
        getInput = self.BasicIpTracer.lineEdit_ipInput.text()
        getInput = str(getInput)
        
        if len(getInput) < 1:
            self.BasicIpTracer.textBrowser_logConsole.append(gen_error_text("No ip input, process stopped"))
            return
        
        resultDict = reverseIpLookup_ipinfoio(target_ip=getInput)
        
        if resultDict["success"] != True:
            self.BasicIpTracer.textBrowser_logConsole.append(gen_error_text(resultDict["data"]))
            return
        
        if resultDict["cordinate"] != None:
            dict_is = resultDict["cordinate"]
            dict_is = str(resultDict["cordinate"]).split(",")
            mapData = drawNewMap(cordinate_array_or_tuple=dict_is, note_text="IP network distribution point or location")    
            self.BasicIpTracer.webView_mapView.setHtml(mapData)    
        
        for dict_key in resultDict["dict"].keys():
            name_is = str(dict_key).upper()
            self.BasicIpTracer.textBrowser_logConsole.append(f"<B>[ {name_is} ]:</B> {resultDict['dict'][dict_key]}")
        
    
    def clearOutputs(self):
        self.showDefaultMap()
        self.BasicIpTracer.textBrowser_logConsole.setText("<B>LOG CONSOLE:</B>")
        self.BasicIpTracer.lineEdit_ipInput.clear()
        
    
    def showDefaultMap(self):
        self.BasicIpTracer.webView_mapView.setHtml(drawNewMap(cordinate_array_or_tuple=(0.0,0.0),zoom_start=1))
        