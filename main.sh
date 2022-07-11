#!/bin/bash
source modules/function_lib.sh
login_standart 
bash modules/first_start.sh #kurulum kontrolu için düzenli olarak kontrol sağlar 

function tool_status()
{
    if [[ -e "modules/first_start.sh" && -e "modules/function_lib.sh" ]] ; then 
        clear
        kurulum_tespit="Bulundu"
        printf "\n${green}Tool çalışabilir kurulum ve fonksiyonlar $kurulum_tespit\n${reset}"
        echo
        read -p "Devam etmek için ENTER"
    else 
        clear
        kurulum_tespit="Bulunamadı"
        tool_stat="Kritik gereksinim dosyaları bulunamadı...!"
        printf "\n${red}$tool_stat\n${reset}"
        echo
        echo "Olası nedenler:"
        echo "Toolu kendi dizininde çalıştırmadıysanız"
        echo "Eksik veya yanlış kurulum"
        echo "Toola ait dosyaların adlarının veya içeriklerinin değiştirilmesi"
        echo "olabilir"
        echo "7 - Bash shell başlat komutu her halukarda çalışacaktır ama"
        echo
        read -p "Devam etmek için ENTER"

    fi
}

function onar()
{
    clear
	echo "=============================="
	echo
	echo "Tool manüsüne dönmek için exit yzmanız yeterli! "
	echo
	echo "=============================="
	echo
	read -p "Devam etmek için ENTER"
	clear
	bash
}
if [[ ! -d "$HOME/Hack-Tools/tmp" ]] #eğer geçici dizin tmp yi bulamazsa oluşturacak
then
	echo "tmp bulunamadı oluşturuluyor...!"
	mkdir $HOME/Hack-Tools/tmp
	sleep 0.5
fi 
rm -rf $HOME/Hack-Tools/tmp/* #kendi tmp dizinini düzenli olarak temizlemesi için

while :
do 
clear
echo "=============================="
echo ""
echo "	 - TheHive v1.6 -"
echo ""
echo "1 - Exiftool ile meta veri okuma          12-Offline iban çözümleyici"
echo "2 - Cupp ile wordlist oluştur"
echo "3 - IP-Tracer ile ip adresi takip et"
echo "4 - Netdiscover ile ağ içi arp taraması"
echo "5 - Nmap ile tarama"
echo "6 - Sistemi güncelle"
echo "7 - Bash shell başlat"
echo "8 - Metasploit-framework kur (GitHub)"
echo "9 - Msfvenom ile trojan oluştur"
echo "10- Phoneinfoga ile telefon sorgusu"
echo "11- Sqlmap ile işlemler"
echo ""
echo "96 - Tool dosyalarını kontrol et          97 - Log kayıtlarını sil..."
echo "98 - Yapımcı ve lisans bilgileri          99 - Çıkış"
echo "=============================="
echo ""
echo "Mevcut dizin -> $PWD"
echo "Home dizini -> $HOME"
echo ""
echo "=============================="
echo ""
read -p "-İşlem-> " main_select

if [[ "$main_select" = "1" ]] ; then 
    bash modules/exiftool.sh || tool_status

elif [[ "$main_select" = "2" ]] ; then
    bash modules/cupp.sh || tool_status

elif [[ "$main_select" = "3" ]] ; then   
    bash modules/ip_tracer.sh || tool_status

elif [[ "$main_select" = "4" ]]; then
    bash modules/netdiscover.sh || tool_status

elif [[ "$main_select" = "5" ]] 
then
	bash modules/nmap.sh || tool_status

elif [[ "$main_select" = "6" ]];then
	bash modules/sys-update.sh || tool_status

elif [[ "$main_select" = "7" ]] ; then
    onar

elif [[ "$main_select" = "8" ]];then
	bash modules/msf_install.sh || tool_status 

elif [[ "$main_select" = "9" ]];then
	bash modules/msf_venom/msf_venom.sh || tool_status 

elif [[ "$main_select" = "10" ]];then
	bash modules/phone_infoga.sh || tool_status
elif [[ "$main_select" = "11" ]] ; then
	clear
	python3 modules/sqlmap/sqlmap.py || tool_status

elif [[ "$main_select" = "12" ]] ; then
    if [[ ! -e "/bin/python3" ]] ; then
        echo "Python kurunuz lutfen...!"
    fi 
    clear && echo 
    echo  "Çıkmak için EXİT yazınız...!"
    echo 
    read -p "Devam etmek içi ENTER"
    clear 
    python3 modules/offline_iban/main.py || tool_status
    clear 
elif [[ "$main_select" = "96" ]];then
    tool_status
elif [[ "$main_select" = "97" ]];then
    bash modules/terminate_log.sh || tool_status


elif [[ "$main_select" = "98" ]];then
    bash modules/lisans.sh || tool_status

elif [[ "$main_select" = "99" ]];then
    echo "Çıkış yapılıyor....!"
    sleep 0.5 && break
else 
    echo "Bilinmeyen girdi...!"
    sleep 1 && clear
fi 
done 

