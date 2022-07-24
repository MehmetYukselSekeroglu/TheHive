#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 17:11:50 2022

@author: wesker
"""

import os
os.system("bash modules/sqlmap/first.sh")
os.system("clear")

def print_banner():
    print("""
 _____  _          _  _  _           
|_   _|| |_   ___ | || |(_)__ __ ___ 
  | |  |   \ / -_)| __ || |\ V // -_)
  |_|  |_||_|\___||_||_||_| \_/ \___|

	Sorulara yanıt vererek taramayı başlatabilirsiniz:
 """)
    print("\n\n")
    
def standart_inputs():
    target_url = input("URL giriniz-> ")
    show_dbs = input("Veritabanları gösterilsinmi? 1-0 -> ")
    scan_domain = input("Sitedeki olası tüm açıklar taransınmı? 0-3 ->")
    show_dump_screen = input("Verileri ekrana yazdı? 1-0 -> ")
    scan_forms = input("Formlar taransınmı? 1-0 -> ")
    scan_risk = input("Tarama ağırlığı? 1-3 -> ")
    scan_lvl = input("ANlık istek sayısı? 1-5 -> ")
    scan_threads = input("İşlem hızlndırma? 1-10 -> ")
    use_bypass = input("WAF-IPS-IDS Bypass kullan? 1-0 -> ")
    user_agents = input("Random useragent kullanılsınmı? 1-0 -> ")
    auto_quest = input("Sorular otomatik cevplansınmı? 1-0 -> ") 
    print("\n")

    if user_agents == "1":    
        user_agent = "--random-agent"

    elif user_agents == "0":
        user_agent = ""
    else:
        print("User agent ön tanımlı 0 ayarlandı..!")
        user_agent = ""    
    
    scan_domain_control=("1","2","3")
    if scan_domain in scan_domain_control:
        crawl = f"--crawl={scan_domain}"
        acıkk_tarama = "Evet"
    elif scan_domain == "0":
        crawl = ""
	    acık_tarama = "Hayır"
    else:
        print("Açık taramsaı ön tanımlı kapalı olarak ayarlandı...!")
    	crawl = ""
        k_tarama = "Hayır"
    if auto_quest == "1":
        batch = "--batch"
        batch_durum = "Evet"
    elif auto_quest == "0":
        batch = ""
        batch_durum = "Hayır"
    else: 
        print("batch ön tanımlı evet ayarlandı...!")
        batch = "--batch"
        batch_durum = "Evet"

    if show_dbs == "0":
        dbs = ""
        dbs_durum = "Hayır"
    elif show_dbs == "1":
        dbs = "--dbs"
        dbs_durum = "Evet"
    else:
        print("Ön tanımlı değer 1 ayarlandı...!")
        dbs = "--dbs"
        
    if show_dump_screen == "1":
        dump = "--dump"
        ekrana_yazdir = "Evet"
    elif show_dump_screen == "0":
        dump = ""
        ekrana_yazdir = "Hayır"
    else:
        print("Ekrana yazdırma ön tanımlı 1 ayarlandı...!")
        dump = "--dump"
        ekrana_yazdir = "Evet"
            
    if scan_forms == "1":
        form_durum = "Evet"
        forms = "--forms"
    elif scan_forms == "0":
        form_durum = "Hayır"
        forms = ""
    else:
        print("Form ön tanımlı 0 olarak ayarlandı...!")
        form_durum = "Hayır"
        forms = ""
        #########################
        risk_control = ("1","2","3")

    if scan_risk in risk_control:
        risk = f"--risk={scan_risk}"
    else:
        print("Risk ön tanımlı değer olarak 1 ayarlandı...!")
        risk = "--risk=1"
        scan_risk="1"
        
        ######################
    lvl_control = ("1","2","3","4","5")
    if scan_lvl in lvl_control:
        lvl = f"--level={scan_lvl}"
    else:
        print("level ön tanımlı değer 1 olark kullnılıyor...!")
        lvl = "--level=1"
        scan_lvl = "1"
################
    threads_control = ("1","2","3","4","5","6","7","8","9","10")
    if scan_threads in threads_control:
        threads = f"--threads={scan_threads}"
    else:
        print("Threads ön tanımlı değer 3 olarak ayarlandır...!")
        threads = "--threads=3"
    
    if use_bypass == "1":
        home_dir = os.environ['HOME']
        bypass_dir_list = list
        bypass_dir_list = os.listdir(f"{home_dir}/Hack-Tools/sqlmap/tamper/")
        print("\nBypass dosyasını seçiniz: \n")
        print("""0eunion.py               commentbeforeparentheses.py   least.py                     randomcomments.py     sp_password.py
apostrophemask.py        concat2concatws.py            lowercase.py                 schemasplit.py        substring2leftright.py
apostrophenullencode.py  dunion.py                     luanginx.py                  sleep2getlock.py      symboliclogical.py
appendnullbyte.py        equaltolike.py                misunion.py                  space2comment.py      unionalltounion.py
base64encode.py          equaltorlike.py               modsecurityversioned.py      space2dash.py         unmagicquotes.py
between.py               escapequotes.py               modsecurityzeroversioned.py  space2hash.py         uppercase.py
binary.py                greatest.py                   multiplespaces.py            space2morecomment.py  varnish.py
bluecoat.py              halfversionedmorekeywords.py  ord2ascii.py                 space2morehash.py     versionedkeywords.py
chardoubleencode.py      hex2char.py                   overlongutf8more.py          space2mssqlblank.py   versionedmorekeywords.py
charencode.py            htmlencode.py                 overlongutf8.py              space2mssqlhash.py    xforwardedfor.py
charunicodeencode.py     ifnull2casewhenisnull.py      percentage.py                space2mysqlblank.py
charunicodeescape.py     ifnull2ifisnull.py            plus2concat.py               space2mysqldash.py
commalesslimit.py        informationschemacomment.py   plus2fnconcat.py             space2plus.py
commalessmid.py          __init__.py                   randomcase.py                space2randomblank.py
""")
    bypass_selections = input("\n\n\nTamper dosyasını seçiniz -> ")
    if bypass_selections in bypass_dir_list:
        tamper_file = bypass_selections
        print("Seçim başarılı...!")
        os.system("sleep 1")
        os.system("clear")
        tamper_command = f"--tamper=\"{tamper_file}\""

    else:
        print("Tamoper douyası bulunamadı on tanımlı base64encode.py kullanılıyor...!")
        tamper_file = "base64encode.py"
        tamper_command = f"--tamper=\"{tamper_file}\""
    else :
        print("IDS-IPS-WAF bypass ön tanımlı 0 olarak ayarlandı...!")
        tamper_command = ""

    #user information block
    print("###########################################\n")
    print("Tarama başlatılıyor...Özellikler:")
    print(f"Hedef -> {target_url}")
    print(f"Veri tabanlarını göser -> {dbs_durum}")
    print(f"Verileri ekrana yazdır -> {ekrana_yazdir}")
    print(f"Formları tara -> {form_durum}")
    print(f"Tarama ağırlığı -> {scan_risk}")
    print(f"Anlık istek sayısı -> {scan_lvl}")
    print(f"Tarama hızlandırma -> {threads}")
    print(f"Soruları otomatik cevaplama -> {batch_durum}")
    print(f"Açık tarama: {acık_tarama} derinlik: {scan_domain}")
    print("\n###########################################")
    
    #main command is here 
    home_dir = os.environ['HOME']
    os.system(f"python3 {home_dir}/Hack-Tools/sqlmap/sqlmap.py -u \"{target_url}\" --eta {dbs} {dump} {forms} {risk} {lvl} {threads} {tamper_command} {user_agent} {batch} {crawl}")

    os.system("sleep 1")
    input("Devam etmek için ENTER ")    




