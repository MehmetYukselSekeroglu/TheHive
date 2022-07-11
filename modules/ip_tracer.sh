#!/bin/bsh
clear
source modules/function_lib.sh 
echo "Kontroller yapılıyor...!"
sleep 1
while :
do 
    if [[ -d "$HOME/Hack-Tools/IP-Tracer" ]];then
        echo "IP-Tracer kurulu...!"
        echo && clear
        echo "=============================="
        echo    
        echo "- IP-tracer -"
        echo "1- Kendi ip adresini sorgula"
        echo "2- Belirli bir ip adresini sorgula"
        echo "3- Tool'u güncelle"
        echo
        echo "99- Çıkış"
        echo 
        echo "=============================="
        read -p "-İşlem-> " ip_tracer_slc    
        echo && clear
        if [[ "$ip_tracer_slc" = "1" ]];then
            cd $HOME/Hack-Tools/IP-Tracer
            bash ip-tracer -m 
            standart_cikis

        elif [[ "$ip_tracer_slc" = "2" ]];then
            clear 
            echo "=============================="
            echo 
            read -p "Sorgulanacak ip adresini giriniz -> "
            echo 
            echo "=============================="
            echo 
            cd $HOME/Hack-Tools/IP-Tracer
            bash ip-tracer -t $REPLY
            standart_cikis

        elif [[ "$ip_tracer_slc" = "99" ]];then 
            echo "Çıkış yapılıyor...!"
            sleep 1
            break
        elif [[ "$ip_tracer_slc" = "3" ]];then
            yakinda_eklenecek
        else
            bilinmeyen_girdi 
        fi 
    else 
        if [[ -d "$HOME/Hack-Tools/debian" || -d "$HOME/Hack-Tools/parrot" ]];then
            clear && echo 
            echo "IP-Tracer kuruluyor...!"
            echo "Gereksinimler kuruluyor...!"
            sleep 1
            sudo apt-get install -y git
            sleep 1 && clear && echo 
            echo "GitHub'dan gerekli dosyalar alınıyor...!"
            sleep 1            
            git clone https://github.com/rajkumardusad/IP-Tracer.git $HOME/Hack-Tools/IP-Tracer
	    chmod +x $HOME/Hack-Tools/IP-Tracer/install 
            chmod +x $HOME/Hack-Tools/IP-Tracer/ip-tracer
            bash $HOME/Hack-Tools/IP-Tracer/install 
            clear
            tool_kuruldu
		    standart_cikis
        elif [[ -d "$HOME/Hack-Tools/arch" ]];then 
            clear && echo 
            echo "IP-Tracer kuruluyor...!"
            githubdan_dosya_alınıyor
            sleep 1
            sudo pacman -S git -y
            sleep 1 && clear
            githubdan_dosya_alınıyor
            git clone https://github.com/rajkumardusad/IP-Tracer.git $HOME/Hack-Tools/IP-Tracer
	    chmod +x $HOME/Hack-Tools/IP-Tracer/install 
            chmod +x $HOME/Hack-Tools/IP-Tracer/ip-tracer
            bash $HOME/Hack-Tools/IP-Tracer/install 
            clear 
            tool_kuruldu
            standart_cikis
        else 
            kurulum_yapilmamis
        fi     
    fi
done





