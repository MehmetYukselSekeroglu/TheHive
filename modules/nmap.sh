source modules/function_lib.sh
echo "Kontroller yapılıyor...!"

ddos_protect_bypass(){
	clear
	echo "=============================="
	echo 
	read -p "Taranacak domain'i giriniz -> " nmap_ip
	clear
	echo 
	echo "$nmap_ip'domin adresi taranıyor...!"
	echo
	echo "=============================="
	echo
	sudo nmap -oG $HOME/Hack-Tools/nmap/log-$nmap_ip-saved.txt -T 2 -Pn -f -sn --traceroute --script traceroute-geolocation $nmap_ip
	standart_cikis
}

sql_inject_scan(){
	clear 
	echo "=============================="
	echo 
	read -p "Taranacak domain'i giriniz -> " nmap_ip
	clear 
	echo 
	sudo nmap -oG $HOME/Hack-Tools/nmap/log-$nmap_ip-saved.txt --script=http-sql-injection $nmap_ip
	standart_cikis


}

while :
do 
    if [[ -d "$HOME/Hack-Tools/nmap" ]] ; then 
    	echo "Nmap kurulu...!"
    	clear 
    	echo "=============================="
    	echo 
    	echo "- Nmap -"
    	echo "1- Port Servis + versiyon taraması"
    	echo "2- Port servis + versiyon + ayrıntılar "
    	echo "3- Port servis + versiyon + ayrıntılar + agresif tarama"
    	echo "4- Os tespit taraması"
    	echo "5- Standart tarama"
    	echo "6- Tam port taraması (65000+ port + os + versiyon + servis)"
        echo "7- Port servis + versiyon UDP taraması (güvenlik duvarı varsa şans artar)"
    #   echo "8- Port servis + versiyon + LOG karıştırıcı (Farklı ip adresleri ile istek atar)"
    	echo "8- Ters dns ile coğrafi konumlama (script taraması)"
    	echo "9- Dns brute force (subdomain bulucu script taraması)"
    	echo "İleri kullanım alanları"
    	echo "10- websitesi sql açıklarını tara"
    	echo
    	echo "98- Nmap versiyonunu göster"
    	echo "99- Çıkış"
    	echo
    	echo "=============================="
    	echo 
    	read -p "-İşlem-> " nmap_select
    	if [[ "$nmap_select" = "1" ]] ; then
    	    clear
    	    echo "=============================="
    	    echo
    	    read -p "Taranacak ip adresini giriniz -> " nmap_ip
    	    clear
    	    echo 
    	    echo "$nmap_ip'adresi taranıyor...!"
    	    echo
    	    echo "=============================="
    	    echo
    	    sudo nmap -oG $HOME/Hack-Tools/nmap/log-$nmap_ip-saved.txt -sS -sV -T 2 -Pn $nmap_ip
			standart_cikis
    	elif [[ "$nmap_select" = "2" ]] ; then
    	    clear
    	    echo "=============================="
    	    echo 
    	    read -p "Taranacak ip adresini giriniz -> " nmap_ip
    	    clear
    	    echo 
    	    echo "$nmap_ip'adresi taranıyor...!"
    	    echo
    	    echo "=============================="
    	    echo
    	    sudo nmap -oG $HOME/Hack-Tools/nmap/log-$nmap_ip-saved.txt -sS -T 2 -sV -Pn -v $nmap_ip
			standart_cikis
    	elif [[ "$nmap_select" = "3" ]] ; then
    	    clear
    	    echo "=============================="
    	    echo 
    	    read -p "Taranacak ip adresini giriniz -> " nmap_ip
    	    clear
    	    echo
    	    echo "$nmap_ip'adresi taranıyor...!"
    	    echo 
    	    echo "=============================="
    	    echo 
    	    sudo nmap -oG $HOME/Hack-Tools/nmap/log-$nmap_ip-saved.txt -sS -sV -Pn -T 2 -v -A $nmap_ip
			standart_cikis
    	elif [[ "$nmap_select" = "4" ]] ; then
    	    clear
    	    echo "=============================="
    	    echo
    	    read -p "Taranacak ip adresini giriniz -> " nmap_ip
    	    clear
    	    echo  
    	    echo "$nmap_ip'adresi taranıyor...!"
    	    echo
    	    echo "=============================="
    	    echo
    	    sudo nmap -oG $HOME/Hack-Tools/nmap/log-$nmap_ip-saved.txt -T 2 -Pn -O $nmap_ip
    	    standart_cikis
    	elif [[ "$nmap_select" = "5" ]] ; then
    	    clear
    	    echo "=============================="
    	    echo 
    	    read -p "Taranacak ip adresini giriniz -> " nmap_ip
    	    clear
    	    echo
    	    echo "$nmap_ip'adresi taranıyor...!"
    	    echo
    	    echo "=============================="
    	    echo
    	    nmap -oG $HOME/Hack-Tools/nmap/log-$nmap_ip-saved.txt -T 2 -Pn $nmap_ip
			standart_cikis
    	elif [[ "$nmap_select" = "6" ]] ; then 
    	    clear
    	    echo "=============================="
    	    echo
    	    read -p "Taranacak ip adresini giriniz -> "
    	    clear
    	    echo
    	    echo "$nmap_ip'adresi taranıyor...!"
    	    echo "Bu işlem saatler sürebilir...!"
    	    echo
    	    echo "=============================="
    	    echo 
    	    sudo nmap -oG $HOME/Hack-Tools/nmap/log-$nmap_ip-saved.txt -Pn -T 2 -sS -sV -v -O -p- $nmap_ip
			standart_cikis
        elif [[ "$nmap_select" = "7" ]] ; then
            clear
            echo "=============================="
            echo 
            read -p "Taranacak ip adresini giriniz -> " nmap_ip
            clear
            echo
            echo "$nmap_ip adresi taranıyor...!"
            echo 
            echo "=============================="
            echo 
            sudo nmap -oG $HOME/Hack-Tools/nmap/log-$nmap_ip-saved.txt -Pn -T 2 -sS -sV -PU $nmap_ip 
			standart_cikis

	elif [[ "$nmap_select" = "8" ]] ;then
		clear
		echo "=============================="
		echo
		read -p "Taranacak ip adresini giriniz -> " nmap_ip
		clear
		echo
		echo "$nmap_ip adresi taranıyor...!"
		echo
		echo "=============================="
		echo
		sudo nmap -oG $HOME/Hack-Tools/nmap/log-$nmap_ip-saved.txt -T 2 -Pn -sn --traceroute --script traceroute-geolocation $nmap_ip
		standart_cikis
	elif [[ "$nmap_select" = "9" ]] ;then
		clear
		echo "=============================="
		echo
		read -p "Taranacak domain'i giriniz örnek: google.com gibi -> " nmap_domain
		clear
		echo
		echo "$nmap_domain'domain adresi taranıyor...!"
		echo 
		echo "=============================="
		echo
		sudo nmap -oG $HOME/Hack-Tools/nmap/log-$nmap_ip-saved.txt -T 2 -Pn -sn -script dns-brute $nmap_domain
		standart_cikis
	elif [[ "$nmap_select" = "10" ]] ; then 
		sql_inject_scan
        #elif [[ "$nmap_select" = "8" ]]
        #then
        #	clear
        #	echo "=============================="
        #	echo
        #	read -p "Taranacak ip adresini giriniz -> " nmap_ip
        #	clear
        #	echo
       	#	echo "$nmap_ip adresi log karıştırıcı ile taranıyor...!"
        #	echo
        #	echo "=============================="
        #	echo
        #	sudo nmap -Pn -sS -sV -D $nmap_ip
        #	echo
        #	echo "=============================="
        #	echo
        #	read -p "Devam etmek için ENTER"
        #  
    	elif [[ "$nmap_select" = "99" ]] ; then 
    	    echo "Çıkış yapılıyor...!"
    	    sleep 1
    	    break
    	elif [[ "$nmap_select" = "98" ]] ; then 
    	    clear
    	    echo "=============================="
    	    echo
    	    nmap --version
			standart_cikis
    	else
    	    echo "Bilinmeyen girdi...!"
    	    sleep 1
    	    clear 
    	fi 
    else 
    	if [[ -d "$HOME/Hack-Tools/debian" || -d "$HOME/Hack-Tools/parrot" ]] ; then 
    	    echo "nmap kuruluyor...!"
    	    sleep 1
    	    sudo apt-get install nmap -y
    	    clear
    	    mkdir $HOME/Hack-Tools/nmap
    	    sleep 1
    	    echo "=============================="
    	    echo 
    	    echo "Tool başarıyla kuruldu...!"
    	    echo "Toolu menüden çalıştırabilirsiniz...!"
			standart_cikis
    	    clear 
    	    break
	elif [[ -d "$HOME/Hack-Tools/arch" ]] ; then 
	    echo "Nmap kuruluyor...!"
	    sleep 1
	    sudo pacman -S nmap -y
	    clear
	    mkdir $HOME/Hack-Tools/nmap
	    sleep 1
	    echo "=============================="
	    echo 
	    echo "Tool başarıyla kuruldu...!"
	    echo "Toolu menüden çalıştırabilirsiniz...!"
		standart_cikis
	    clear 
	    break
	else 
		kurulum_yapilmamis
	fi 
    fi 
done 
