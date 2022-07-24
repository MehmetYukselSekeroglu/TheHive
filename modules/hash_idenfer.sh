source modules/function_lib.sh 

if [[ ! -d "$HOME/Hack-Tools/hash_identifer" ]] ; then 
	clear 
	printf "${green} Hashidentifer kuruluyor...!\n${reset}"
	githubdan_dosya_aliniyor
	git clone https://gitlab.com/kalilinux/packages/hash-identifier.git $HOME/Hack-Tools/hash_identifer 
	
	COMMAND_CONTROL python3
	
	sleep 1 && clear 
	tool_kuruldu

elif [[ -d "$HOME/Hack-Tools/hash_identifer" ]] ; then 
	clear 
	echo "==============================" && echo
	echo "Tool manüsüne dönmek için CTRL+C yapmanız yeterli! "
	echo && echo "==============================" && echo
	read -p "Devam etmek için ENTER"
	clear 
	python3 $HOME/Hack-Tools/hash_identifer/hash-id.py
	
fi 
	
