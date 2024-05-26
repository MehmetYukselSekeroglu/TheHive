import requests

def lookup_bin(target_bin) -> list[bool, str]:
    
    REQ_HEADERS = {"Accept-Version" : "3"}
    RAW_BIN_INPUT = str(target_bin)
    target_bin = str(target_bin[:6])
    REQ_URL:str = f"https://lookup.binlist.net/{target_bin}"
    
    

    try:
        query_req = requests.get(url=REQ_URL, headers=REQ_HEADERS)
    except Exception as err:
        err_msg = "❌ Server error, rety after 60 seconds."
        return [ False,  err_msg]    
    
    
    if query_req.status_code == 404 or query_req.status_code == 400:
        err_msg = "❌ Not valid BIN, BIN not found!"
        return [ False,  err_msg]
    
    if query_req.status_code == 429:
        err_msg = "❌ API full, rety after 60 seconds."
        return [ False, err_msg ]
    
    if query_req.status_code != 200:
        err_msg = "❌ Server error, rety after 60 seconds."
        return [ False, err_msg ]

    try:
        req_data = query_req.json()
    
    except Exception as err:
        err_msg = f"❌ {err}, rety after 60 seconds."
        return [ False, err_msg ]
    
    if "scheme" in req_data.keys():
        card_vendor = str(req_data["scheme"])
    else:
        card_vendor = "NULL"
        
    if "type" in req_data.keys():
        card_type = str(req_data["type"])
    else:
        card_type = "NULL"
        
    if "brand" in req_data.keys():
        card_brand = str(req_data["brand"])
    else:
        card_brand = "NULL"
    
    if type(req_data["country"]) == dict:
        if "name" in req_data["country"].keys():
            card_country_name = str(req_data["country"]["name"])
        else:
            card_country_name = "NULL"
    else:
        card_country_name = "NULL"
    
    if type(req_data["bank"]) == dict:
        if "name" in req_data["bank"].keys():
            card_bank_name = str(req_data["bank"]["name"])
        else:
            card_bank_name = "Failed to detect bank name."    
    else:
        card_bank_name = "Failed to detect bank name."    
    
    if card_vendor == "NULL" and card_type=="NULL" and card_brand=="NULL" and card_country_name == "NULL":
        err_msg = "❌ Not valid BIN, no info for target BIN!"
        return [ False,  err_msg]
    
    return_text = f"""Valid BIN ✅
BIN: {target_bin}
Vendor: {card_vendor}
Type: {card_type}
Brand: {card_brand}
Country: {card_country_name}
Bank: {card_bank_name} 

Source: {REQ_URL}"""


    return [ True, return_text ]
    
    
    
    