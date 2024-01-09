#!/usr/bin/env python3 
"""
BU ARAÇ OSINT CERCEVESİ İCERİSİNDE BİLGİ TOPLAMAK AMACIYLA YAZILMIS OLUP 
KOTU AMACLI KULLANIM DURUMUNDA SORUMLULUK KISIYE AITTIR 

AMACI DUNYA CAPINDA GECERLI OLAN IBAN NUMARASININ KENDİ İCERİSİNDE BARINDIRMI OLDUGU 
BILGILERI KULLANARAK BILGI TOPLAMAKTIR INTERNET BAGLANTISINA GEREK DUYMAZ TAMAMEN 
CEVRIM DISI OLARAK CALISABILMEKTEDIR 


LİSANS: MIT 
YAZAR: TheKoba-dev 
TELEGRAM: @BayTapsan 
BELGE DUZENLENME:07.11.2022


KULLANIM:
python3 dosya.py -i "çözümlenecek_iban"

UYARI: IBAN'I YAZARKEN BOSLUK KULLANMYAINIZ 
"""
from colorama import *
import os
import requests
from bs4 import BeautifulSoup


def country_detect (raw_1) -> dict:
    global max_leng
    global account_control
    global bank_branch
    global status_sepa
    try:
        country_number = raw_1[0] + raw_1[1]
        country_number = str(country_number)
        if not country_number.isalpha():
            return { "success":False, "data":"invalid iban number" }
        country_number = country_number.upper()
    except Exception:
        return { "success":False, "data":"missing iban data" }
    
    
    if country_number == "TR":
        country = "Turkey"
        max_leng = 26
        
        status_sepa = False
        account_control = False
        bank_branch = True
        
    elif country_number == "DE":
        country = "Almanya"
        max_leng =22
        
        status_sepa = True
        account_control = True
        bank_branch = True
            
    elif country_number == "AD":
        country = "Andora"
        max_leng = 24
        
        status_sepa = False
        account_control = False
        bank_branch = True
        
    elif country_number == "AL":
        country = "Arnavutluk"
        max_leng = 28
        
        status_sepa = False
        account_control = False
        bank_branch = True
        
    elif country_number == "AT":
        country = "Avusturya"
        max_leng = 20
        
        status_sepa = True
        account_control = True
        bank_branch = True
        
    elif country_number == "AZ":
        country = "Azerbaycan"
        max_leng = 28
        
        status_sepa = False
        account_control = False
        bank_branch = False
                
    elif country_number == "BH":
        country = "Bahreyn"
        max_leng = 22
        
        status_sepa = False
        account_control = False
        bank_branch = False
        
    elif country_number == "BY":
        country = "Belarus"
        max_leng = 28
        
        status_sepa = False
        account_control = False
        bank_branch = False
        
    elif country_number == "BE":
        country = "Belçika"
        max_leng = 16
        
        status_sepa = True
        account_control = True
        bank_branch = True
        
    elif country_number == "AE":
        country = "Birleşik Arap Emirlikleri"
        max_leng = 23
        
        status_sepa = False
        account_control = False
        bank_branch = False
        
    elif country_number == "GB":
        country = "Birleşik Krallık"
        max_leng = 22
        
        status_sepa = True
        account_control = True
        bank_branch = True
        
    elif country_number == "BA":
        country = "Bosna Hersek"
        max_leng = 20
        
        status_sepa = False
        account_control = True
        bank_branch = True
        
    elif country_number == "BR":
        country = "Brezilya"
        max_leng = 29
        
        status_sepa = False
        account_control = False
        bank_branch = True
        
    elif country_number == "BG":
        country = "Bulgaristan"
        max_leng = 22
        
        status_sepa = True
        account_control = False
        bank_branch = True
        
    elif country_number == "GI":
        country = "Cebelitarık"
        max_leng = 23
        
        status_sepa = True
        account_control = False
        bank_branch = True
        
    elif country_number == "DK":
        country = "Danimarka"
        max_leng =  18
        
        status_sepa = True
        account_control = False
        bank_branch = True
        
    elif country_number == "DO":
        country = "Dominik Cumhuriyeti"
        max_leng = 28
        
        status_sepa = False
        account_control = False
        bank_branch = True
        
    elif country_number == "TL":
        country = "Doğu Timor"
        max_leng = 23
        
        status_sepa = False
        account_control = True
        bank_branch = False
        
    elif country_number == "SV":
        country = "El Salvador"
        max_leng = 28
        
        status_sepa = False
        account_control = False
        bank_branch = False
        
    elif country_number == "EE":
        country = "Estonya"
        max_leng = 20
        
        status_sepa = True
        account_control = True
        bank_branch = True
        
    elif country_number == "FO":
        country = "Faroe Adaları"
        max_leng = 18
        
        status_sepa = True
        account_control = False
        bank_branch = True
        
    elif country_number == "PS":
        country = "Filistin"
        max_leng = 29
        
        status_sepa = False
        account_control = False
        bank_branch = False
        
    elif country_number == "FI":
        country = "Finlandiya"
        max_leng = 18
        
        status_sepa = True
        account_control = True
        bank_branch = True
        
    elif country_number == "FR":
        country = "Fransa"
        max_leng = 27
        
        status_sepa = True
        account_control = True
        bank_branch = True
        
    elif country_number == "GL":
        country = "Grönland"
        max_leng = 18
        
        status_sepa = True
        account_control = False
        bank_branch = True
        
    elif country_number == "GT":
        country = "Guatemala"
        max_leng = 28
        
        status_sepa = False
        account_control = False
        bank_branch = False
        
    elif country_number == "GE":
        country = "Gürcistan"
        max_leng = 22
        
        status_sepa = False
        account_control = False
        bank_branch = False
        
    elif country_number == "NL":
        country = "Hollanda"
        max_leng = 18
        
        status_sepa = True
        account_control = True
        bank_branch = True
        
    elif country_number == "HR":
        country == "Hırvatistan"
        max_leng = 21
        
        status_sepa = True
        account_control = True
        bank_branch = False
        
    elif country_number == "IE":
        country = "İrlanda"
        max_leng = 22
        
        status_sepa = True
        account_control = True
        bank_branch = True
        
    elif country_number == "ES":
        country = "İspanya"
        max_leng = 24
        
        status_sepa = True
        account_control = True
        bank_branch = True
        
    elif country_number == "IL":
        country = "İsrail"
        max_leng = 23
        
        status_sepa = False
        account_control = False
        bank_branch = True
        
    elif country_number == "SE":
        country = "İsveç"
        max_leng = 24
        
        status_sepa = True
        account_control = True
        bank_branch = True
        
    elif country_number == "CH":
        country = "İsviçre"
        max_leng = 21
        
        status_sepa = True
        account_control = True
        bank_branch = True
        
    elif country_number == "IT":
        country = "İtalya"
        max_leng = 27
        
        status_sepa = True
        account_control = True
        bank_branch = True
        
    elif country_number == "IS":
        country = "İzlanda"
        max_leng = 26
        
        status_sepa = True
        account_control = True
        bank_branch = True
        
    elif country_number == "ME":
        country = "Karadağ"
        max_leng = 22
        
        status_sepa = False
        account_control = True
        bank_branch = False
        
    elif country_number == "QA":
        country = "Katar"
        max_leng = 29
    
        status_sepa = False
        account_control = False
        bank_branch = False
        
    elif country_number ==  "KZ":
        country = "Kazakistan"
        max_leng = 20

        status_sepa = False
        account_control = False
        bank_branch = False
        
    elif country_number == "XK":
        country = "Kosova"
        max_leng = 20
        
        status_sepa = False
        account_control = True
        bank_branch = True
        
    elif country_number == "CR":
        country = "Kostarika"
        max_leng = 22
        
        status_sepa = False
        account_control = True
        bank_branch = False
        
    elif country_number == "KW":
        country = "Kuveyt"
        max_leng = 30
        
        status_sepa = False
        account_control = False
        bank_branch = False
        
    elif country_number == "CY":
        country = "Kıbrıs"
        max_leng = 28

        status_sepa = True
        account_control = False
        bank_branch = True
        
    elif country_number == "LV":
        country = "Letonya"
        max_leng = 21
        
        status_sepa = True
        account_control = False
        bank_branch = False
        
    elif country_number == "LI":
        country = "Lihtenştayn"
        max_leng = 21
        
        status_sepa = True
        account_control = True
        bank_branch = True
        
    elif country_number == "LT":
        country = "Litvanya"
        max_leng = 20

        status_sepa = True
        account_control = False
        bank_branch = True
        
    elif country_number == "LB":
        country = "Lübnan"
        max_leng = 28

        status_sepa = False
        account_control = False
        bank_branch = False
        
    elif country_number == "LU":
        country = "Lüksemburg"
        max_leng = 20

        status_sepa = True
        account_control = False
        bank_branch = False
        
    elif country_number == "HU":
        country = "Macaristan"
        max_leng = 28
        

        status_sepa = True
        account_control = True
        bank_branch = True
        
    elif country_number == "MK":
        country = "Makedonya"
        max_leng = 19
        
        status_sepa = False
        account_control = True
        bank_branch = False

    elif country_number == "MT":
        country = "Malta"
        max_leng = 31
        
        status_sepa = True
        account_control = False
        bank_branch = True
        
    elif country_number == "MU":
        country = "Mauritius"
        max_leng = 30
        
        status_sepa = False
        account_control = False
        bank_branch = True
        
    elif country_number == "MD":
        country = "Moldova"
        max_leng = 24
        
        status_sepa = False
        account_control = False
        bank_branch = False
        
    elif country_number == "MC":
        country = "Monako"
        max_leng = 27
        
        status_sepa = True
        account_control = True
        bank_branch = True
        
    elif country_number == "MR":
        country = "Moritanya"
        max_leng = 27
        
        status_sepa = False
        account_control = True
        bank_branch = True
        
    elif country_number == "PK":
        country = "Pakistan"
        max_leng = 24
        
        status_sepa = False
        account_control = False
        bank_branch = False
        
    elif country_number == "PL":
        country = "Polonya"
        max_leng = 28
        
        status_sepa = True
        account_control = True
        bank_branch = True
        
    elif country_number == "PT":
        country = "Portekiz"
        max_leng = 25

        status_sepa = True
        account_control = True
        bank_branch = True
        
    elif country_number == "RO":
        country = "Romanya"
        max_leng = 24
        
        status_sepa = True
        account_control = False
        bank_branch = False
        
    elif country_number == "LC":
        country = "Saint Lucia"
        max_leng = 32

        status_sepa = False
        account_control = False
        bank_branch = False
        
    elif country_number == "SM":
        country = "San Marino"
        max_leng = 27
        
        status_sepa = True
        account_control = True
        bank_branch = True
        
    elif country_number == "ST":
        country = "Sao Tome ve Principe"
        max_leng = 25

        status_sepa = False
        account_control = False
        bank_branch = False
        
    elif country_number == "SC":
        country = "Seyşeller"
        max_leng = 31
        
        status_sepa = False
        account_control = False
        bank_branch = False
        
    elif country_number == "SK":
        country = "Slovak Cumhuriyeti"
        max_leng = 24

        status_sepa = True
        account_control = True
        bank_branch = False
        
    elif country_number == "SI":
        country = "Slovenya"
        max_leng = 19
        
        status_sepa = True
        account_control = True
        bank_branch = True
        
    elif country_number == "SA":
        country = "Suudi Arabistan"
        max_leng = 24

        status_sepa = False
        account_control = False
        bank_branch = False
        
    elif country_number == "RS":
        country = "Sırbistan"
        max_leng = 22
        
        status_sepa = False
        account_control = True
        bank_branch = False
        
    elif country_number == "TN":
        country = "Tunus"
        max_leng = 24
        
        status_sepa = False
        account_control = True
        bank_branch = True
        
    elif country_number == "UA":
        country = "Ukrayna"
        max_leng = 29
        
        status_sepa = False
        account_control = False
        bank_branch = True
        
    elif country_number == "VG":
        country = "Virgin Adaları, İngiliz"
        max_leng = 24
        
        status_sepa = False
        account_control = False
        bank_branch = False
        
    elif country_number == "GR":
        country = "Yunanistan"
        max_leng = 27
        
        status_sepa = True
        account_control = False
        bank_branch = True
        
    elif country_number == "CZ":
        country = "Çek Cumhuriyeti"
        max_leng = 24
        
        status_sepa = True
        account_control = True
        bank_branch = False
        
    elif country_number == "JO":
        country = "Ürdün"
        max_leng = 30
        
        status_sepa = False
        account_control = False
        bank_branch = True
        
    elif country_number == "IQ":
        country = "Irak"
        max_leng = 23
        
        status_sepa = False
        account_control = False
        bank_branch = False
        
    else :
        country = "Not detected"
        error_satut = True

    return {
        "success":True,
        "data":{
            "country":country,
            "max_leng": max_leng,
            "sepa":status_sepa,
            "account_control":account_control,
            "bank_brach":bank_branch,
            "country_number":country_number
        }
    }
    

def iban_parametres(iban_1):
    global control_number_global 
    global bank_code_local
    global rezerve_code  
    global müsteri_nosu_raw
    if country_detect(iban_1)["success"] == True:
        if country_detect(iban_1)["data"]["country"] == "Turkey":
            try:
                control_number_global = iban_1[2] + iban_1[3]
                bank_code_local = iban_1[4] + iban_1[5] + iban_1[6] + iban_1[7] + iban_1[8]
                rezerve_code = iban_1[9]
                account_number = iban_1[10:26]
                sube_kodu = iban_1[10:14]
                müsteri_nosu_raw = iban_1[13:22]
                hesap_eki_kodu = iban_1[22:]
            except Exception:
                return {"success":False, "data":"missing data"}
            
            if bank_code_local == "00001":
                bank_name = "TC Merkez Bankası"
            elif bank_code_local == "00004":
                bank_name = "İller Bankası"
            elif bank_code_local == "00010":
                bank_name = "Ziraat Bankası"
            elif bank_code_local == "00012":
                bank_name = "Halkbank"
            elif bank_code_local == "00015":
                bank_name = "Vakıflar Bankası"
            elif bank_code_local == "00017":
                bank_name = "Kalkınma Bankası"
            elif bank_code_local == "00029":
                bank_name = "Birleşik Fon Bankası"
            elif bank_code_local == "00032":
                bank_name = "Türk Ekonomi Bankası"
            elif bank_code_local == "00046":
                bank_name = "Akbank"
            elif bank_code_local == "00059":
                bank_name = "Şekerbank"
            elif bank_code_local == "00062":
                bank_name = "Garanti Bankası"
            elif bank_code_local == "00064":
                bank_name = "İş Bankası"
            elif bank_code_local == "00067":
                bank_name = "Yapı ve Kredi Bankası"
            elif bank_code_local == "00099":
                bank_name = "ING Bank"
            elif bank_code_local == "00100":
                bank_name = "Adabank"
            elif bank_code_local == "00111":
                bank_name = "Finansbank"
            elif bank_code_local == "00123":
                bank_name = "HSBC"
            elif bank_code_local == "00132":
                bank_name = "Takasbank"
            elif bank_code_local == "00134":
                bank_name = "Denizbank"
            elif bank_code_local == "00135":
                bank_name = "Anadolu Bank"
            elif bank_code_local == "00137":
                bank_name = "Rabobank"
            elif bank_code_local == "00138":
                bank_name = "Dilerbank"
            elif bank_code_local == "00139":
                bank_name = "GSD Bank"
            elif bank_code_local == "00141":
                bank_name = "Nurol Yatırım Bankası"
            elif bank_code_local == "00142":
                bank_name = "Bankpozitif Kredi ve Kalkınma Bankası"
            elif bank_code_local == "00143":
                bank_name = "Aktif Yatırım Bankası"
            elif bank_code_local == "00146":
                bank_name = "Odea Bank"
            elif bank_code_local == "00147":
                bank_name = "Bank of Tokyo-Mitsubishi UFJ Turkey"
            elif bank_code_local == "00203":
                bank_name = "Albaraka Türk Katılım Bankası"
            elif bank_code_local == "00205":
                bank_name = "Kuveyt Türk Katılım Bankası"
            elif bank_code_local == "00206":
                bank_name = "Türkiye Finans Katılım Bankası"
            elif bank_code_local == "00209":
                bank_name = "Ziraat Katılım Bankası"
            elif bank_code_local == "00210":
                bank_name = "Vakıf Katılım Bankası"
            elif bank_code_local == "00806":
                bank_name = "Merkezi Kayıt Kuruluşu"
            elif bank_code_local == "00109":
                bank_name = "ICBC Turkey Bank"
            else:
                else_proc = "0"
                return {"success":False, "data":"0"}
        #16
        else:
            control_number_global = "DESTEKLENMİYOR"
            bank_code_local =  "DESTEKLENMİYOR"
            rezerve_code = "DESTEKLENMİYOR"
            account_number =  "DESTEKLENMİYOR"
            sube_kodu = "DESTEKLENMİYOR"
            müsteri_nosu_raw = "DESTEKLENMİYOR"
            hesap_eki_kodu = "DESTEKLENMİYOR"
            bank_name = "DESTEKLENMİYOR"
        
        return {
                "success":True,
                "data":{
                    "control_number":control_number_global,
                    "local_bank_code":bank_code_local,
                    "reserve_code":rezerve_code,
                    "account_number":account_number,
                    "bank_name":bank_name,
                    "sube_kodu":sube_kodu,
                    "account_number_raw":müsteri_nosu_raw,
                    "hesap_eki_kodu":hesap_eki_kodu
                }
            }


def get_all_data_for_iban(iban):
    iban = str(iban)
    orig_iban = iban
    iban = iban.replace(" ","")
    ulke = country_detect(iban)

    if ulke["success"] != True:
        return {
            "success":False,
            "data":"IBAN not be valid"
        }


    others_data = iban_parametres(iban)

    if others_data["success"] != True:
        return {
            "success":False,
            "data":"IBAN not be valid"
        }


    raw_iban_leng = len(iban)
    standart_leng = ulke["data"]["max_leng"]


    scrap_url=url=f"https://iban.gen.tr/iban-cozumleme-ve-dogrulama?kod={iban}"
    try:
        sorgulama=requests.get(url=scrap_url)
        ayıklamanmıs_data=BeautifulSoup(sorgulama.content,"html.parser")
        data_1=ayıklamanmıs_data.find(attrs={"class":"table table-bordered table-sm table-resolve-verify"})
        data_1=data_1.find_all('td')
        try:
            iban_il=data_1[2]
            iban_ilce=data_1[1]
        except Exception:
            iban_il,iban_ilce=">> ALINAMADI <<"
        iban_il = str(iban_il)
        iban_ilce = str(iban_ilce)

        iban_il = iban_il.strip('<td>')
        iban_il= iban_il.strip('</td>')
    
        iban_ilce= iban_ilce.strip('<td>')
        iban_ilce = iban_ilce.strip('</td>')

    except Exception as err:
        iban_il = None
        iban_ilce = None

    



    return {
        "success":True,
        "data":{
            "raw_iban": iban,
            "country":ulke['data']['country'],
            "max_leng": ulke['data']['max_leng'],
            "sepa":ulke['data']['sepa'],
            "account_control":ulke['data']['account_control'],
            "bank_brach":ulke['data']['bank_brach'],
            "country_number":ulke['data']['country_number'],
            "local_bank_code":others_data['data']['local_bank_code'],
            "reserve_code":others_data['data']['reserve_code'] ,
            "account_number":others_data['data']['account_number'],
            "account_number_raw":others_data['data']['account_number_raw'],
            "hesap_eki_kodu":others_data['data']['hesap_eki_kodu'],
            "bank_name":others_data['data']['bank_name'],
            "sube_kodu":others_data['data']['sube_kodu'],
            "sube_il":iban_il,
            "sube_ilce":iban_ilce,

            
        }
    }
    
    