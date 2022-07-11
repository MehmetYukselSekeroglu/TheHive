#renkleri import etmesi daha kolay olsun diye 

red='\033[1;31m'
green='\033[1;32m'
yellow='\033[1;33m'
blue='\033[1;34m'
light_cyan='\033[1;96m'
reset='\033[0m'


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
function githubdan_dosya_alınıyor(){
    echo "=============================="
    echo 
    echo "GitHub'dan gerekli dosyalar alınıyor...!"
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
	printf "${red}UYARI:Bu yazılım yanlızca eğitim amaçlıdır kötüye kullanım\n"
	printf "ve herhangi bir yere/kişilere zarar vermek amacıyla KULLANMAYINIZ!\n${reset}"
    sleep 2.5
}
