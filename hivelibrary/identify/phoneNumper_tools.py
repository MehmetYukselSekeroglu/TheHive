# From https://github.com/MehmetYukselSekeroglu/TurkOperator_bilgileri




def check_number_only_TR(phone_numbber:str) -> dict:
    abone_numarası = phone_numbber[3:10]
    abone_numarası = str(abone_numarası)
    
    if len(phone_numbber) < 10:
        return {"success":False, "message":"numara olması gerekenden kısa"}
    
    if len(phone_numbber) > 10:
        return {"success":False, "message":"numara olması gerekenden uzun"}
    
    saglayıcı_kodu=phone_numbber[0:3]
    TurkTelekom = ["501", "505", "506","507","552","553","554","555","559"]
    TurkCell = ["530","531","532","533","534","535", "536", "537", "538", "539"]
    Vodafone = ["541", "542", "543", "544", "545", "546", "547", "548", "549"]
    
    operator_supported_codes = []
    if saglayıcı_kodu in TurkTelekom:
        SaglayıcıBilgisi = "TürkTelekom"
        operator_supported_codes = TurkTelekom
        
    elif saglayıcı_kodu == "551":
        SaglayıcıBilgisi = "BIMcell sanal öperatör | TürkTelekom"
        operator_supported_codes = TurkTelekom
    
    elif saglayıcı_kodu in TurkCell:
        SaglayıcıBilgisi = "Turkcell"
        operator_supported_codes = TurkCell
        
    elif saglayıcı_kodu == "516":
        SaglayıcıBilgisi = "Bursa mobile sanal öperatör | Turkcell"
        operator_supported_codes = TurkCell
        
    elif saglayıcı_kodu == "561":
        SaglayıcıBilgisi = "61cell sanal öperatör | Turkcell" 
        operator_supported_codes = TurkCell
        
    elif saglayıcı_kodu in Vodafone:
        SaglayıcıBilgisi = "Vodafone"
        operator_supported_codes = Vodafone
        
    else:
        SaglayıcıBilgisi="Tespit edilemedi, bölgesel numara olabilir"
        operator_supported_codes = [ "No Data" ]
        
    return {"success":True, "operatör":SaglayıcıBilgisi, "supported_codes":operator_supported_codes}