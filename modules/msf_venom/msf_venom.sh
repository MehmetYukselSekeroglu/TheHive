#!/bin/bash

echo "kontroller yapılıyor...!"
clear
if [[ -e "/bin/msfvenom" ]];then
	echo "Msfvenom kurulu...!"
	if [[ ! -d "$HOME/Hack-Tools/msf" ]];then 
		mkdir $HOME/Hack-Tools/msf
	fi 
elif [[ -d "$HOME/Hack-Tools/msf" ]];then
	echo "msfvenom kurulu...!"
	if [[ ! -d "$HOME/Hack-Tools/msf" ]];then 
		mkdir $HOME/Hack-Tools/msf
	fi 
####################### apk tool derlemesi başarısız olduğu için geçici olarak askıya alındı######################
#elif [[ ! -e "/bin/apktool" ]] ; then
#	if [[ -d "$HOME/Hack-Tools/debian" || -d "$HOME/Hack-Tools/parrot" || -d "$HOME/Hack-Tools/arc" ]] ; then
#		echo "Apktool bulunamadı kuruluyor...!"
#		sleep 1
#		git clone https://github.com/iBotPeaches/Apktool.git $HOME/Hack-Tools/apktool
#		clear 
#		cd $HOME/Hack-Tools/apktool
#		chmod +x gradlew
#		sudo ./gradlew
#	else 
#		echo "Kurulum tamamlanmamış...!"
#		sleep 1
#		exit 
#	fi 
#elif [[ -e "/bin/apktool" && ! -e "$HOME/Hack-Tools/apktool" ]] ; then
#	if [[ -d "$HOME/Hack-Tools/debian" || -d "$HOME/Hack-Tools/parrot" || -d "$HOME/Hack-Tools/arc" ]] ; then
#		echo "Apktool bulunamadı kuruluyor...!"
#		sleep 1
#		git clone https://github.com/iBotPeaches/Apktool.git $HOME/Hack-Tools/apktool
#		clear 
#		cd $HOME/Hack-Tools/apktool
#		chmod +x gradlew
#		sudo ./gradlew
#	else 
#		echo "Kurulum tamamlanmamış...!"
#		sleep 1
#		exit 
#	fi 


else 
	echo "Msfvenom kuruluyor...!"
	curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/	msfupdate.erb > msfinstall.sh 
	#tool un ilk satırında standart shell (sh) olduğu belirtilmiştir
	sh msfinstall.sh 
	rm -rf msfinstall.sh #kurulum bitince gereksiz kurulum dosyalarını siliyor  
	mkdir $HOME/Hack-Tools/msf # ikincil kontrol yapısı için kendi dizininde klasör oluşturuyor
	clear
	echo "=============================="
	echo
	echo "Kurulum başarılı...!"
	echo 
	echo "=============================="
	echo
	sleep 1
fi 
clear
echo "=============================="
echo "=============================="
echo 
echo "          ! === UYARI === !"
echo
echo "=LÜTFEN OLUŞTURDUĞUNUZ DOSYALARI VE TOOLU="
echo
echo "===VİRÜS TOTAL'E ATMYINIZ BU İŞLEM==="
echo
echo "=======TOOLU ÖLDÜRÜR!======="
echo
echo "=============================="
echo "=============================="
echo
read -p "Okudum anladım ENTER"
#işlem döngüsü alanı
while :
do 
clear
echo "V--> Msfvenom <--V"
echo ""
echo "Platform seçiniz:"
echo "1- Windows"
echo "2- Android"
echo "3- php kodu"
echo
echo "99- Çıkış" 

read -p "-İşlem-> " msf_select
if [[ "$msf_select" = "1" ]];then
	bash moduls/msf_venom/windows.sh 
elif [[ "$msf_select" = "2" ]];then 
	bash moduls/msf_venom/android.sh 

elif [[ "$msf_select" = "3" ]];then
	echo "Çok yakında...!"
	sleep 1
	
elif [[ "$msf_select" = "99" ]];then
	echo "Çıkış yapılıyor...!"
	sleep 1 && break
else 
	echo "Bilinmeyen girdi...!"
	sleep 1
fi 
done
