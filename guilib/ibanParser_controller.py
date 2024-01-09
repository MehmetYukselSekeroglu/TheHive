from PyQt5.QtWidgets import *

from guilib.ibanParserScreen import Ui_iban_parser_form

from hivelibrary.osint import iban_parser

import json

class ibanParserPage(QWidget):
    def __init__(self):
        super().__init__()
        
        self.ibanParserWidget = Ui_iban_parser_form()
        self.ibanParserWidget.setupUi(self)
        
        self.setWindowTitle("iban parser")
        
        self.lastParsedData = {}
        self.resultPrinted = False
        self.ayrac = "-"*30
        
        self.ibanParserWidget.pushButton_clearResult.clicked.connect(self.clearInputAndOutput)
        self.ibanParserWidget.pushButton_parse_iban.clicked.connect(self.parseTargetIban)
        self.ibanParserWidget.pushButton_save_result.clicked.connect(self.saveResultFromFile)
        
    def clearInputAndOutput(self):
        self.ibanParserWidget.textBrowser_resultConsole.setHtml("<B>RESULT</B><br>") 
        self.ibanParserWidget.lineEdit_iban_input.clear()  
        self.resultPrinted = False
    
    def saveResultFromFile(self):
        # notes
        # index 0 == fro human txt
        # index 1 == fro machines json
        
        if self.ibanParserWidget.comboBox_saveType.currentIndex() == 0:
            saveFileName, _ = QFileDialog.getSaveFileName(self, "Save Result",filter="Text file (*.txt)")


            if not saveFileName:
                err_msg = f"[ - ] Save file not selected"
                self.ibanParserWidget.textBrowser_resultConsole.append(err_msg)
                return         
                
                
            if self.resultPrinted != True:
                err_msg = f"[ - ] There are no results to save"
                self.ibanParserWidget.textBrowser_resultConsole.append(err_msg)
                return
                
            
            self.ibanParserWidget.textBrowser_resultConsole.append(self.ayrac)
            self.ibanParserWidget.textBrowser_resultConsole.append("[ + ] Saving operation started")
                
            with open(saveFileName, "w") as saveFile:
                saveFile.write(self.lastParsedData["text"])
                      
            self.ibanParserWidget.textBrowser_resultConsole.append("[ + ] File successfuly saved ")

        elif self.ibanParserWidget.comboBox_saveType.currentIndex() == 1:
            saveFileName, _ = QFileDialog.getSaveFileName(self, "Save Result",filter="Json file (*.json)")


            if not saveFileName:
                err_msg = f"[ - ] Save file not selected"
                self.ibanParserWidget.textBrowser_resultConsole.append(err_msg)
                return         
                
                
            if self.resultPrinted != True:
                err_msg = f"[ - ] There are no results to save"
                self.ibanParserWidget.textBrowser_resultConsole.append(err_msg)
                return
                
            
            self.ibanParserWidget.textBrowser_resultConsole.append(self.ayrac)
            self.ibanParserWidget.textBrowser_resultConsole.append("[ + ] Saving operation started")
                
            with open(saveFileName, "w") as saveFile:
                json.dump(self.lastParsedData["json"],saveFile)
                      
            self.ibanParserWidget.textBrowser_resultConsole.append("[ + ] File successfuly saved ")
    
    def parseTargetIban(self):
        input_iban = self.ibanParserWidget.lineEdit_iban_input.text()
        self.ibanParserWidget.textBrowser_resultConsole.append(f"[ + ] Proccess started, pls wait...")
        result = iban_parser.get_all_data_for_iban(input_iban)
        if result["success"] != True:
            err_msg = f"""Parse job failed.<br>Api response: {result["data"]}"""
            self.ibanParserWidget.textBrowser_resultConsole.append(err_msg)
            return
        
        result_is = result["data"]
        raw_iban = result_is["raw_iban"]
        country = result_is["country"]
        max_leng= result_is["max_leng"]
        account_control = result_is["account_control"]
        bank_brach = result_is["bank_brach"]
        country_number = result_is["country_number"]
        local_bank_code = result_is["local_bank_code"]
        reserve_code = result_is["reserve_code"]
        account_number = result_is["account_number"]
        account_number_raw = result_is["account_number_raw"]
        hesap_eki_kodu = result_is["hesap_eki_kodu"]
        bank_name = result_is["bank_name"]
        sube_kodu = result_is["sube_kodu"]
        sube_il = result_is["sube_il"]
        sube_ilce = result_is["sube_ilce"]
        output_text = f"""<B>STATUS:</B> iban successfuly parsed <br>
<B>Input iban:</B> {raw_iban}   <br>
<B>Country:</B> {country}   <br>
<B>Country number:</B> {country_number} <br>
<B>Max leng:</B> {max_leng} <br>
<B>Account Control Support:</B> {account_control} <br>
<B>Bank branc:</B> {bank_brach} <br>
<B>Local bank code::</B> {local_bank_code} <br>
<B>Reserve code:</B> {reserve_code} <br>
<B>Raw account number:</B> {account_number_raw} <br>
<B>Account number:</B> {account_number} <br>
<B>Bank name:</B> {bank_name}   <br>
<B>Branch code:</B> {sube_kodu} <br>
<B>Branch city:</B> {sube_il}   <br>
<B>Branch district:</B> {sube_ilce} <br>
"""
        to_save = output_text.replace("<B>","").replace("</B>","").replace("<br>","")
        self.lastParsedData["text"] = to_save
        self.lastParsedData["json"] = result
        
        self.ibanParserWidget.textBrowser_resultConsole.setHtml(output_text)
        self.resultPrinted = True