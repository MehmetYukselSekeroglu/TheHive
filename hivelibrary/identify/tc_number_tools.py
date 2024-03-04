

"""
01.12.2022 Developed By Prıme Security | Automatic Tc Number Calculator
Github Page: https://github.com/MehmetYukselSekeroglu/tc-hesaplayici
"""





#girilen tc numarası matematiksel olarak geçerlimi kontrol eder 
def gecerlilik_kontrol(tc:str) -> dict:
    if len(tc) != 11:
        return { "success": False, "data":"TC numarası 11 hane olmadığı için geçerli değildir" }
    
    if not tc.isnumeric():
        return { "success": False, "data":"Tc numarası nümerik olmadığı için geçerli değildir" }

    step_1 = int(tc[0]) + int(tc[2]) + int(tc[4]) + int(tc[6]) + int(tc[8])
    step_1 = step_1 * 7

    step_2 = int(tc[1]) + int(tc[3]) + int(tc[5]) + int(tc[7])
    step_2 = step_2 * 9

    final_indis_10 = step_1 + step_2
    final_indis_10 = final_indis_10 % 10
    final_indis_11 = 0

    for z in range(10):    
        final_indis_11 = final_indis_11 + int(tc[z])

    final_indis_10 = str(final_indis_10)
    final_indis_11=final_indis_11%10
    final_indis_11 = str(final_indis_11)

    if final_indis_10 == tc[9] and final_indis_11 == tc[10]:
        return { "success": True, "data":f"{str(tc)} numarası geçerlidir" }
    
    return { "success":False, "data":"Tc numarası geçerisz yapıdadır" }
    
def kontrol_basamakları(ilk_9_indis):
    tc = str(ilk_9_indis)
    step_1 = int(tc[0]) + int(tc[2]) + int(tc[4]) + int(tc[6]) + int(tc[8])
    step_1 = step_1 * 7

    step_2 = int(tc[1]) + int(tc[3]) + int(tc[5]) + int(tc[7])
    step_2 = step_2 * 9

    final_indis_10 = step_1 + step_2
    final_indis_10 = final_indis_10 % 10 
    final_indis_11 = 0
    tc=f"{tc}{final_indis_10}"
    for i in range(10):
        final_indis_11 = final_indis_11 + int(tc[i])
    final_indis_10 = str(final_indis_10)
    final_indis_11 = final_indis_11 % 10
    final_indis_11 = str(final_indis_11)
    
    final= final_indis_10+final_indis_11
    return final



def tc_uretici(uretilecek_tc,olustuma_adedi):
    olustuma_adedi = int(olustuma_adedi)
    ilk_9indis = uretilecek_tc[0:9]
    ilk_9indis = int(ilk_9indis)
    geriye_donuk = ilk_9indis
    ileri_donuk = ilk_9indis
    ileri_donuk_liste=[]
    geriye_donuk_liste=[]
    a = 0
    while (a <= int(olustuma_adedi)):
        geriye_donuk = geriye_donuk - 29999
        dondurulecek_deger = f"{geriye_donuk}{kontrol_basamakları(geriye_donuk)}"
        if gecerlilik_kontrol(dondurulecek_deger)["success"]:
            geriye_donuk_liste.append(dondurulecek_deger)
            a= a+1 
    b = 0
    while (b <= int(olustuma_adedi)):
        ileri_donuk = ileri_donuk + 29999
        dondurulecek_deger = str(ileri_donuk)+str(kontrol_basamakları(ileri_donuk))
        if gecerlilik_kontrol(dondurulecek_deger)["success"]:
            ileri_donuk_liste.append(dondurulecek_deger)
            b=b+1
    return ileri_donuk_liste,geriye_donuk_liste

