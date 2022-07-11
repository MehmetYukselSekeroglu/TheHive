clear
source modules/function_lib.sh
echo "Kontroller yapılıyor...."
while :
do 

    if [[ -d "$HOME/Hack-Tools/netdiscover" ]];then
        echo "Netdiscover kurulu...!"
        clear
        echo "=============================="
        echo 
        echo "Q ya basarak netdiscover'dan çıkabilirsiniz!"
        echo 
        echo "=============================="
        echo ""
        read -p "Anladım ENTER"
        sudo netdiscover 
        standart_cikis
        break && clear
    else

        if [[ -d "$HOME/Hack-Tools/debian" || -d "$HOME/Hack-Tools/parrot" ]] ;then
            echo "Netdiscover kuruluyor...!"
            sleep 1
            sudo apt-get install netdiscover -y 
            clear
            mkdir $HOME/Hack-Tools/netdiscover 
            echo "=============================="
            echo 
            echo "Tool başarıyla kuruldu...."
            echo "Toolu menüden çalıştırabilirsiniz...!"
            standart_cikis
            break && clear
        elif [[ -d "$HOME/Hack-Tools/arch" ]];then
            echo "Netdiscover kuruluyor...!"
            sleep 1
            sudo pacman -S netdiscover -y && clear 
            mkdir $HOME/Hack-Tools/netdiscover
            tool_kuruldu
            standart_cikis
        else
            kurulum_yapilmamis 
        fi 
    fi
done 
