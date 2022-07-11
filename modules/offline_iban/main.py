from lib_iban import *
import os 
while True:
    main_logo()
    print ("=============================")
    print (f"Çıkmk için EXİT yazınız...!")
    print ("Çevrimdışı iban çözümleyici\n")
    print ("Örnek kullanım: TR330001000030570718255001\n")
    raw_input_1 = input ("iban giriniz -> ")
    if raw_input_1 == "EXİT":
        break 
    a = country_detect(raw_input_1)
    b = iban_parametres(raw_input_1)

    raw_input_1_leng = len(raw_input_1)
    standart_leng = a[1]
    if raw_input_1_leng == standart_leng:
        if iban_parametres(raw_input_1) != "0":
            print ("-------------------------")
            print (f"Ülke: {a[0]}")
            print (f"Max iban uzunluğu: {a[1]}")
            print (f"SEPA desteği: {a[2]}")
            print (f"Hesap kontrolu: {a[2]}")
            print (f"Şube kontrolu: {a[4]}")
            print (f"Ülke kodu: {a[5]}")
            print (f"Global kontrol kodu: {b[0]}")
            print (f"Banka kodu: {b[1]}")
            print (f"Rezerv numrası: {b[2]}")
            print (f"Hesap numarası: {b[3]}") 
            print (f"Banka adı: {b[4]}")
            print (f"Şube kodu: {b[5]}")
            print (f"müşteri numarası (saf): {b[6]}")
            print (f"Hesap ek nosu: {b[7]}")
        else:
            print ("İban geçersizdir...!")
    elif raw_input_1_leng > standart_leng:
    
        print ("İban olması gerekenden uzun...!\n")
        print ("Bu iban geçersizdir...!")
    elif raw_input_1_leng < standart_leng:
    
        print ("İban olması gerekenden kısa...!\n")
        print ("Bu iban geçersizdir...!")
    else:
        print ("Bilinmeyen hata...!")
        

    

