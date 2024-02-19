
import requests
from urllib.parse import urlparse


def virustotal_url_scanner(target_url, vt_api_key) -> list:
    target_url = str(target_url)
    vt_api_key = str(vt_api_key)

    STATIC_URL_SCAN_API_URL = "https://www.virustotal.com/vtapi/v2/url/scan"
    request_parametres = {
        "apikey" : vt_api_key,
        "url" : target_url
        }
    
    rawReq = requests.post(url=STATIC_URL_SCAN_API_URL, data=request_parametres)

    if rawReq.status_code == 200:
        try:
            parsed_req = rawReq.json()
            if parsed_req["response_code"] == 1:
                scan_id_is = parsed_req["scan_id"]
                return [ True, str(scan_id_is) ]
            
            else:
                return [ False, "API isteği kabul etmedi veya edemedi" ]
        except Exception:
            return [ False, "Veri işlenirken hata gerçekleşti" ]
    else:
        return [ False, f"İstek geçersiz durum kodu döndürdü kod: {str(rawReq.status_code)}" ]
    


def virustotal_url_response_handler(vt_api_key, is_response_id) -> list:
    vt_api_key = str(vt_api_key)
    is_response_id = str(is_response_id)

    # api url
    STATIC_REPORT_URL = "https://www.virustotal.com/vtapi/v2/url/report"

    request_prametres = {
        "apikey" : vt_api_key,
        "resource" : is_response_id
        }
    
    get_results = requests.get(url=STATIC_REPORT_URL, params=request_prametres)

    if get_results.status_code == 200:
        try:
            results_json = get_results.json()
            
            # if respons success
            if results_json["response_code"] == 1:
                target_url = results_json["url"]
                vt_sonuc_linki = results_json["permalink"]
                toplam_tarayan = results_json["total"]
                tespit_edilen = results_json["positives"]
                tarama_tarihi = results_json["scan_date"]
                
                return [True, [ target_url, toplam_tarayan, tespit_edilen, tarama_tarihi, vt_sonuc_linki ] ]

            else:
                return [ False, "API isteği kabul etmedi veya edemedi" ]            
            
        # error exceptions and feedback
        except Exception:
            return [False, f"Veri işlenirken hata gerçekleşti"]
    else:
        return [ False, f"İstek geçersiz durum kodu döndürdü kod: {str(get_results.status_code)}" ]

def is_url(string):
    parsed_url = urlparse(string)
    if parsed_url.netloc:
        return True
    return False