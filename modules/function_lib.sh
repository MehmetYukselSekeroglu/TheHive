#renkleri import etmesi daha kolay olsun diye 

red='\033[1;31m'
green='\033[1;32m'
yellow='\033[1;33m'
blue='\033[1;34m'
light_cyan='\033[1;96m'
reset='\033[0m'

#standart kullanıcılar için olan komutların path ları
COMMAND_PATH_1="/bin"
COMMAND_PATH_2="/usr/bin"
COMMAND_PATH_3="/usr/share/bin"


#root yetkisi gerektiren komutların path ları
ADMIN_COMMAND_PATH_1="/sbin"
ADMIN_COMMAND_PATH_2="/usr/sbin"
ADMIN_COMMAND_PATH_3="/usr/local/sbin"



function COMMAND_CONTROL(){

	searchto="$1"

	if [[ -e "$COMMAND_PATH_1/$searchto" || -e "$COMMAND_PATH_2/$searchto" || -e "$COMMAND_PATH_3/$searchto" || -e "$ADMIN_COMMAND_PATH_1/$searchto" || -e "$ADMIN_COMMAND_PATH_2/$searchto" || -e "$ADMIN_COMMAND_PATH_3/$searchto" ]] ; then
		command_status="1"
	else 
		command_status="0"
	fi 
	
	if [[ "$command_status" = "0" ]] ; then 
		if [[ -d "$HOME/Hack-Tools/debian" || -d "$HOME/Hack-Tools/parrot" ]] ; then
			printf "$green $searchto indiriliyor...! ${reset}\n"
			sudo apt-get install -y $searchto 
		elif [[ -d "$HOME/Hack-Tools/arc" ]] ; then 
			printf "$green $searchto indiriliyor...!\n ${reset}"
			sudo pacman -S $searchto -y 
		else
			kurulum_yapilmamis
		fi 	
	fi 
		

}





function bilinmeyen_girdi(){
    echo ""
    printf "${red}==============================\n"
    echo ""
    printf "Bilinmeyen girdi...!${reset}\n"
    echo ""
    printf "==============================${reset}\n"
    sleep 1
    clear 
}

function kurulum_yapilmamis(){
    clear 
    printf "${red}==============================\n"
    echo 
    printf "Kurulum yapılmamış...!\n"
    echo    
    printf "==============================${reset}\n"
    exit
}

function yakinda_eklenecek(){
    printf "${light_cyan}Bu alan çok yakında eklenecek...!${reset}\n"
    sleep 1
    clear
}

function standart_cikis(){
    echo 
    echo "=============================="
    echo 
    read -p "Devam etmek için ENTER"
    clear
}

	
function tool_kuruldu (){
    sleep 1
    clear					
    printf "${green}==============================\n"
    echo ""
	printf "Tool başarıyla kuruldu...!\n"
	printf "Toolu menüden çalıştırabilirsiniz...!\n"
	echo ""
	printf "==============================${reset}\n"
	echo ""
	read -p "Çıkmak için ENTER"
}
function githubdan_dosya_aliniyor(){
    echo "=============================="
    echo 
    echo "GitHub/GitLab'dan gerekli dosyalar alınıyor...!"
    echo 
    echo "=============================="
}
function start_bashshells(){
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
function login_standart() {	
	clear 
	printf """ ${red}
 ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ 
█       █  █ █  █       █  █ █  █   █  █ █  █       █
█▄     ▄█  █▄█  █    ▄▄▄█  █▄█  █   █  █▄█  █    ▄▄▄█
  █   █ █       █   █▄▄▄█       █   █       █   █▄▄▄ 
  █   █ █   ▄   █    ▄▄▄█   ▄   █   █       █    ▄▄▄█
  █   █ █  █ █  █   █▄▄▄█  █ █  █   ██     ██   █▄▄▄ 
  █▄▄▄█ █▄▄█ █▄▄█▄▄▄▄▄▄▄█▄▄█ █▄▄█▄▄▄█ █▄▄▄█ █▄▄▄▄▄▄▄█
${reset}
"""
	printf "${green}	By @TheKoba\n\n${reset}"
	printf "${blue}Telegram Grubumuza Katılın! https://t.me/SiberGuvenlikChat_Tr ${reset}\n"
	printf "${red}UYARI:Bu yazılım yanlızca eğitim amaçlıdır bir yere/kişilere \nzarar vermek amacıyla KULLANMAYINIZ!${reset}\n"
    sleep 2.5
}
