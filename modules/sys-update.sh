#!/bin/bash
clear
echo "Kontroller yapılıyor...!"
clear
while :
do 
	if [[ -d "$HOME/Hack-Tools/debian" ]] ; then
		echo "Sistem güncelleniyor...!"
		echo "Yeni paket listesi alınıyor ( bu işlem kali linux'da bug lı olabilir atlyabilirsiniz...! )"
		sleep 2
		sudo apt-get update 
		clear
		echo "Tam sistem yükseltmesi yapılıyor...!"
		sleep 1
		sudo apt-get full-upgrade -y	
		clear
		echo "=============================="
		echo
		echo "Sistem başarıyla güncellendi...!"
		echo 
		echo "=============================="
		echo
		read -p "Devam etmek için ENTER"
		break
	elif [[ -d "$HOME/Hack-Tools/parrot" ]] ; then
		echo "Sistem güncelleniyor...!"
		sleep 1
		sudo parrot-upgrade -y
		clear
		echo "=============================="
		echo
		echo "Sistem başarıyla güncellendi...!"
		echo
		echo "=============================="
		echo
		read -p "Devam etmek için ENTER"
		break
	elif [[ -d "$HOME/Hack-Tools/arch" ]] ; then
		echo "Sistem güncelleniyor...!"
		sleep 1
		sudo pacman -Syu -y
		clear
		echo "=============================="
		echo 
		echo "Sistem başarıyla güncellendi...!"
		echo 
		echo "=============================="
		echo 
		read -p "Devam etmek için ENTER"
		break
	else 
		echo "Kurulum tamamlanmamış...!"
		echo "Lütfen kurulumu tamamlayın...!"
		sleep 1
		clear 
		break
		
	fi
done 
