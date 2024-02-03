import requests
import json


from hivelibrary.user_agent_tools import randomUserAgent

IPINFO_IO_API_URL:str ="https://ipinfo.io/" 






def reverseIpLookup_ipinfoio(target_ip:str) -> dict:
    try:
        RESULT_DICT = {}
        
        request_url = IPINFO_IO_API_URL + target_ip
        request_headers = {"User-Agent":randomUserAgent(),}
        
        queryRequest = requests.get(url=request_url)
        
        if not queryRequest.ok:
            return { "success":False, "data":f"IP query failed, status code: {queryRequest.status_code}","cordinate":None ,"dict":None}

        queryData = queryRequest.json()
        queryKeys = queryData.keys()
        if "ip" in queryKeys:
            RESULT_DICT["ip"] = queryData["ip"]
            
        if "hostname" in queryKeys:
            RESULT_DICT["hostname"] = queryData["hostname"]
        
        if "anycast" in queryKeys:
            RESULT_DICT["anycast"] = queryData["anycast"]
        
        if "city" in queryKeys:
            RESULT_DICT["city"] = queryData["city"]
            
        if "region" in queryKeys:
            RESULT_DICT["region"] = queryData["region"]
        
        if "country" in queryKeys:
            RESULT_DICT["country"] = queryData["country"]
        
        if "loc" in queryKeys:
            RESULT_DICT["loc"] = queryData["loc"]
        
        if "org" in queryKeys:
            RESULT_DICT["org"] = queryData["org"]
        
        if "postal" in queryKeys:
            RESULT_DICT["postal"] = queryData["postal"]
        
        if "timezone" in queryKeys:
            RESULT_DICT["timezone"] = queryData["timezone"]
        


        if len(RESULT_DICT) == 1:
            return { "success":False, "data":f"Non valied ip addres: {target_ip}", "cordinate":None,"dict":None}
        
        
        if "loc" in RESULT_DICT.keys():
            return {"success":True, "data":"IP query successfuly", "cordinate":RESULT_DICT["loc"],"dict":RESULT_DICT}
        
        
        return {"success":True, "data":"IP query successfuly", "cordinate":None,"dict":RESULT_DICT}
    
    except Exception as err:
        return {"success":False, "data":f"IP query failed, error message: {err}", "cordinate":None,"dict":None}