#!/bin/bash
while :
do 
    clear
    source modules/main_logo.sh 
    login_standart
    echo "=============================="
    echo 
    echo "99 - İptal & çıkış"
    echo
    echo "Bu işlem kalıcıdır lütfen onay metnini giriniz...!"
    echo
    echo "lütfen \"onaylıyorum\" yazınız"
    echo
    read -p "-> " confirm_str 
    echo
    echo "=============================="
    if [[ "$confirm_str" = "onaylıyorum" || "$confirm_str" = "ONAYLIYORUM"  ]] ; then
        clear
        echo "=============================="
        echo
        echo "Siliniyor: $HOME/Hack-Tools/nmap"
        echo "Siliniyor: $HOME/Hack-Tools/msf"
        echo "Siliniyor: $HOME/Hack-Tools/tmp"
        rm -rf $HOME/Hack-Tools/nmap/*
        rm -rf $HOME/Hack-Tools/msf/*
        rm -rf $HOME/Hack-Tools/tmp/*
        echo
        echo "=============================="
        echo 
        echo "İşlem başarılı...!"
        echo 
        read -p "Devam etmek için ENTER "
        break
    elif [[ "$confirm_str" = "99" ]] ; then 
        echo "=============================="
        echo
        echo "İptal ediliyor...!"
        echo
        echo "=============================="
        sleep 1 && break
    else 
        echo "Metni doğru giriniz...!" && sleep 1
    fi
done 
