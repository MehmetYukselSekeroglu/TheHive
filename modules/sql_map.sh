#!/bin/bash

clear 
#termux için kontr4oller 
if [[ -d "$HOME/Hack-Tools/termux" ]] ; then 
	using_termux="1"
else 
	using_termux="0"
fi
#renk atamaları
red='\033[1;31m'
green='\033[1;32m'
yellow='\033[1;33m'
blue='\033[1;34m'
light_cyan='\033[1;96m'
reset='\033[0m'

#####################KONTROL KISMI###################33
printf "${green}Kontroller yapılıyor...!${reset} \n"
sleep 1

if [[ -d "$HOME/Hack-Tools/sqlmap" ]];then 
	printf "${green}sqlmap zaten kurulu...!${reset}\n"
else 
	printf "${red}sqlmap kuruluyor...!${reset}\n"
	sleep 1 
	if [[ "$using_termux" = "1" ]];then 
		pkg install -y git 
		pkg install -y python3 
		clear 
	fi 
	git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git $HOME/Hack-Tools/sqlmap
	mkdir $HOME/Hack-Tools/sqlmap/log 
	clear 
	sleep 1
	echo 
	printf "${green}sqlmap başarıyla kuruldu...!${reset}\n"
	echo 
fi 
all_input () 
{
	echo 
	read -p "URL'yi giriniz -> " target_url 
	read -p "Veri tabanları gösterilsinmi? 1-0 -> " show_dbs
	read -p "Verileri ekrana yazıdr? 1-0 -> " show_dump_screen
	read -p "Formları tara? -> " scan_forms
	read -p "Tarama ağırlığı 1-3 -> " scan_risk
	read -p "Anlık istek sayısı 1-5 -> " scn_lvl
	read -p "İşlem hızlandırma? 1-10 -> " scan_treads
	read -p "WAF-IPS-IDS Bypass kullan? 1-0 -> " use_bypass
	echo 
}
control_funcionts ()
{
	if [[ "$show_dbs" = "0" ]] ; then 
		dbs=""
		dbs_durum="hayır"
	elif [[ "$show_dbs" = "1" ]] ; then 
		dbs="--dbs"
		dbs_durum="evet"
	else 
		printf "${red}Dbs ön tanımlı 1 ayarlandı...!${reset}\n"
		dbs="--dbs"
	fi 
	##################################
	
	if [[ "$show_dump_screen" = "1" ]] ; then 
		dump="--dump"
		ekrana_yazdir="evet"
	elif [[ "$show_dump_screen" = "0" ]] ; then 
		dump=""
		ekrana_yazdir="hayır"
	else 
		printf "${red}Ekrana yazdırma ön tanımlı 0 ayarlandı...!${reset}\n"
		dump=""
		ekrana_yazdir="hayır"
	fi 
	##################################
	
	if [[ "$scan_forms" = "1" ]] ; then 
		form_durum="evet"
		forms="--forms"
	elif [[ "$scan_forms" = "0" ]] ; then 
		form_durum="hayır"
		forms=""
	else 
		printf "${red}Forms ön tanımlı 0 ayarlandı...!${reset}\n"
		forms=""
		form_durum="hayır"
	fi 
	###################################

	if (( $scan_risk > 4 )) ; then 
		risk="--risk=$scan_risk"
	elif (( $scan_risk == 4 )) ; then
		risk="--risk=$scan_risk"
	else
		printf "${red}Risk ön tanımlı değer 1 olark kullnılıyor...!${reset}\n" 
		risk="--risk=1"
	fi 
	##################################
	if (( $scn_lvl > 5 )) ; then 
		lvl="--level=$scn_lvl"
	elif (( $scn_lvl == 5 )) ; then
		lvl="--level=$scn_lvl"
	else 
		printf "${red}level ön tanımlı değer 1 olark kullnılıyor...!${reset}\n"
		lvl="--level=1"
	fi 
	###################################
	if (( $scan_treads > 10 )) ; then 
		threads="--threads=$scan_treads"
	elif (( $scan_treads == 10 )) ; then 
		threads="--threads=$scan_treads"
	else 
		printf "${red}Threads ön tanımlı değer 3 olark kullnılıyor...!${reset}\n"
		threads="--threads=3"
	fi 
	
}

bypass_functions ()
{
 
	ls $HOME/Hack-Tools/sqlmap/tamper/
	echo 
	printf "${green}Bypass için kullanılacak tamper dosyasının adını giriniz:${reset}\n"
	printf "${green}Birden fazla kullanmak için aralarına , koyarak yazınız..!${reset}\n"
	read -p "--> " tamper_file 
	tamper_file_path="$HOME/Hack-Tools/sqlmap/tamper/$tamper_file"	 
}

all_input

control_funcionts


if [[ "$use_bypass" = "1" ]] ; then
	bypass_functions
	tamper="--tamper=\"$tamper_file_path\""
else
	$tamper=""
fi 
	
printf "${green}Tarama başlatılıyor...! \n"
printf "Özellikler: \n"
echo "Hedef -> $target_url"
echo "$threads"
echo "$lvl"
echo "$risk"
echo "Form taraması -> $form_durum"
echo "Sonuçları ekrana yazıdır -> $ekrana_yazdir "
echo "Veri tabanları listesini ekrana yazıdır -> $dbs_durum"
echo 
printf "==============================${reset}\n"
echo 
printf "${blue}Komut: python3 $HOME/Hack-Tools/sqlmap/sqlmap.py -u \"$target_url\" $dbs $dump $forms $risk $lvl $threads ${reset}\n"
sleep 1

python3 $HOME/Hack-Tools/sqlmap/sqlmap.py -u "$target_url" $dbs $dump $forms $risk $lvl $threads $tamper

read -p "Devam etmek için ENTER "




