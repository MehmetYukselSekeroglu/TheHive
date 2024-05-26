#!/usr/bin/env bash

red='\033[1;31m'
green='\033[1;32m'
yellow='\033[1;33m'
blue='\033[1;34m'
light_cyan='\033[1;96m'
reset='\033[0m'


source "etc/os-release"


if [[ "$UID" != "0" ]]; then

    printf "$red[!]$reset This Script Only Running As root!\n"
    exit -1 
fi



if [[ "$ID" = "kali" ]] ;then
    printf "$yellow[+]$reset Detected System:\t $NAME $VERSION \n"
    printf "$yellow[+]$reset Starting installer... \n"

    printf "$yellow[+]$reset Installing libpython3-dev ...\n"
    apt install libpython3-dev 2> /dev/null

    printf "$yellow[+]$reset Installing PostgrSQL ... \n"
    apt install postgresql 2> /dev/null

    printf "$yellow[+]$reset Installing python3 python3-pip python3-pyqt5 ...\n"
    apt install python3 python3-pip python3-pyqt5 python3-pyqt5.qtwebengine python3-pyqt5.qtwebkit 2> /dev/null

    printf "$yellow[+]$reset Installing python3-opencv ...\n"
    apt install python3-opencv 2> /dev/null

    printf "$yellow[+]$reset Installing docker.io docker-compose ... \n"
    apt install docker.io docker-compose 2> /dev/null

    printf "$yellow[+]$reset Installing pip packaget ... \n"
    pip install pydub psutil colorama beautifulsoup4 requests opencv-python onnxruntime insightface numpy shodan

    

    printf "$yellow[+]$reset All downloads successfuly ... \n"
    printf "$yellow[+]$reset Creating PostgreSQL server on docker ... \n"








fi	















