source modules/function_lib.sh

printf "${green}Kontroller yapılıyor...!${reset}\n"
if [[ -d "$HOME/Hack-Tools/phoneinfoga" ]];then
	printf "${red}Phoneinfoga zaten kurulu...!${reset}\n"
else 
	if [[ ! -e "/bin/curl" ]];then 
		if [[ -d "$HOME/Hack-Tools/debian" || -d "$HOME/Hack-Tools/parrot" ]];then 
			sudo apt install -y curl
			clear
		elif [[ -d "$HOME/Hack-Tools/arc" ]];then 
			sudo pacman -S curl -y
			clear 
		else 
			clear
			kurulum_yapilmamis
		fi 
	fi  
	printf "${red}Kuruluyor...!${reset}\n"
	mkdir $HOME/Hack-Tools/phoneinfoga
	cd $HOME/Hack-Tools/phoneinfoga
	curl -sSL https://raw.githubusercontent.com/sundowndev/phoneinfoga/master/support/scripts/install | bash
	clear
	if [[ -e "$HOME/Hack-Tools/phoneinfoga/phoneinfoga" ]];then
		printf "${green}Kurulum başarılı...!${reset}\n"
		sleep 1
		exit
	else 
		printf "${red}Kurulum başarısız...!${reset}\n"
		sleep 2
		exit
	fi 
fi 
while :
do 
	clear
	printf "${green}==============================\n"
	printf "\n"
	printf "Sorgulanacak numara örnek-> (+905554442211)\n"
	printf "\n"
	printf "exit veya EXIT yazarak çıkabilirsiniz...! \n"
	printf "==============================${reset}"
	echo 
	echo 
	read -p "Numara-> " phone_number 
	if [[ "$phone_number" = "exit" || "$phone_number" = "EXIT" ]];then 
		printf "${red}Çıkış yapılıyor...!${reset}"
		sleep 1
		clear
		break
	else 
		cd $HOME/Hack-Tools/phoneinfoga
		clear
		./phoneinfoga scan -n "$phone_number"
		standart_cikis
	fi 


done 
	
	
	
