echo "Kontroller yapılıyor...!"
source modules/function_lib.sh 
if [[ -d "$HOME/Hack-Tools/exiftool" ]];then
    echo "Exiftool zaten kurulu...!"
    clear && echo ""
    echo "$HOME dizini içeriği:"
    echo "=============================="
    ls $HOME
    echo ""
    echo "=============================="
    echo ""
    read -p "İncelenecek-dosya-tam-adı-> " exif_img
    echo ""
    echo "=============================="
    clear
    echo "=============================="
    echo "" 
    echo "$exif_img in meta verisi..!"
    echo ""
    echo "=============================="
    echo 
    perl $HOME/Hack-Tools/exiftool/exiftool $HOME/$exif_img
    echo ""
    echo "=============================="
    echo ""
    read -p "Çıkmak için ENTER"

else 
    echo "Exiftool kuruluyor...!"
    echo ""
    echo "=============================="
    if [[ -d "$HOME/Hack-Tools/debian"  || -d "$HOME/Hack-Tools/parrot" ]];then
        echo "Gereksinimler indiriliyor...!"
        sudo apt-get install -y perl git
        clear 
        githubdan_dosya_alınıyor
        git clone "https://github.com/exiftool/exiftool.git" $HOME/Hack-Tools/exiftool
        tool_kuruldu
        

    elif [[ -d "$HOME/Hack-Tools/arch" ]];then
        echo "Gereksinimler indiriliyor...!"
        sudo pacman -S perl git -y
        clear
        git clone "https://github.com/exiftool/exiftool.git" $HOME/Hack-Tools/exiftool
        tool_kuruldu

        
    else 
        echo "Gerekli kontrol dosyaları bulunamadı lütfen kurulum yapınız...!"
        sleep 1
        exit 
    fi
fi
    
