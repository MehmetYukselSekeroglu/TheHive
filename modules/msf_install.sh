#!/bin/bash
source modules/function_lib.sh

if [[ -e "/bin/msfconsole" ]];then	
	clear
	echo "=============================="
	echo
	echo "Metasploit-framework zaten kurulu...!"
	echo
	echo "=============================="
	sleep 1 && exit
elif [[ -d "$HOME/Hack-Tools/msf" ]]
then
	clear
	echo "=============================="
	echo
	echo "Metasploit-framework zaten kurulu...!"
	echo
	echo "=============================="
	sleep 1 && exit
else 
	clear
	echo "Kontrollet yapılıyor...!"
fi 

clear
echo "Metasploit-framework kuruluyor...!"
githubdan_dosya_alınıyor
mkdir $HOME/Hack-Tools/msf  # ikincil kontrol yapısı için kendi dizininde klasör oluşturuyor
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > $HOME/Hack-Tools/msf/msfinstall.sh 

#tool un ilk satırında standart shell (sh) olduğu belirtilmiştir
cd $HOME/Hack-Tools/msf
chmod +x msfinstall.sh 
./msfinstall.sh 
#rm -rf msfinstall.sh #kurulum bitince gereksiz kurulum dosyalarını siliyor  

clear
echo "=============================="
echo
echo "Kurulum başarılı...!"
echo "sudo msfconsole diyerek toolu başlatabilirsiniz terminalden...!"
standart_cikis

