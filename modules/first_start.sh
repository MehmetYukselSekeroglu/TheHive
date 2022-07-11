source modules/function_lib.sh 
if [[  -d "$HOME/Hack-Tools" ]];then
    echo "Hack-Tools klasörü bulundu...!" && sleep 0.4
else 
    mkdir $HOME/Hack-Tools
    mkdir $HOME/Hack-Tools/tmp
    while :
    do  
        clear
        echo "Kurulum başlatılıyor...!"
        echo "=============================="
        echo "1 - Onaylıyorum devam"
        echo "2 - Onaylamıyorum & çıkış"
        echo ""
        echo "=============================="
        echo ""
        read -p "-İşlem-> " kurulum_select
        if [[ "$kurulum_select" = "1" ]] ; then 
            clear
            echo "=============================="
            echo ""
            echo "Başlatılıyor...!"
            echo ""
            echo "=============================="
            echo ""
            echo "$HOME/Hack-Tools oluşturuluyor...!"               
            sleep 2 && break
        elif [[ "$kurulum_select" = "2" ]];then 
            clear
            echo "=============================="
            echo ""
            echo "İptal edildi, çıkılıyor...!"
            echo ""
            echo "=============================="        
            sleep 1
            exit
        else 
            bilinmeyen_girdi
        fi
    done
fi 

while :
do
   
    if [[ -d "$HOME/Hack-Tools/debian" ]];then
        break
    elif [[ -d  "$HOME/Hack*Tools:/arch" ]];then 
        break
    elif [[ -d "$HOME/Hack-Tools/parrot" ]];then
        break
    else 
        clear
        echo "=============================="
        echo ""    
        echo "kurulum modu:"
        echo "Lütfen kullandığınız dağıtımı seçiniz: "
        echo "1 - Parrot os"    
        echo "2 - Debian ve debian tabanlılar"
        echo "3 - Arch ve arch tabanlı dağıtımlar"
        echo ""
        echo "0 - Kurulumu iptal et ve çık"
        echo "=============================="
        echo ""
        read -p "-Seçim-> " dist_select
        
        if [[ "$dist_select" = "1"  ]];then
            mkdir $HOME/Hack-Tools/parrot
            echo ""
            echo "İşlem başarılı...!"
            sleep 1 && break
            
        elif [[ "$dist_select" = "2"  ]];then
            mkdir $HOME/Hack-Tools/debian
            echo ""
            echo "İşlem başarılı...!"
            sleep 1 && break
            
        elif [[ "$dist_select" = "3"  ]];then
            mkdir $HOME/Hack-Tools/arch
            echo ""
            echo "İşlem başarılı...!"
            sleep 1 && break 
        elif [[ "$dist_select" = "0"  ]];then
            echo ""
            echo "İptal ediliyor...!"
            sleep 1 && exit
        else 
            bilinmeyen_girdi
            clear 
        fi
    fi
done
clear
