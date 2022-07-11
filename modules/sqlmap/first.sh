if [[ -d "$HOME/Hack-Tools/termux"  ]] ; then
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
	clear && sleep 1 && echo 
	printf "${green}sqlmap başarıyla kuruldu...!${reset}\n"
	echo 
fi  
