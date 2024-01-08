from colorama import *
import time



# COLOR CODES
kalın ="\033[1m"
kalın_reset ="\033[0m"
green = Fore.GREEN
blue = Fore.BLUE
color_reset = Fore.RESET
red = Fore.RED
orange = "\033[38;5;208m"


def GetTime():
    """
    herhangi parametre almadan sisteme ait güncel zamanı 
    saat:dakika:saniye olarak döndürür

    Returns:
        str: saat:dakika:saniye
    """
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec
    formatted_time = f"{hour:02d}:{minute:02d}:{second:02d}"
    
    return formatted_time

# BILGILENDIRMELER ICIN 
def InformationPrinter(mesages:str):
    
    print(f"{green}[{GetTime()}]{kalın} [INFO]: {kalın_reset}{blue}{mesages} {color_reset}")


# HATA MESAJLARI ICIN 
def ErrorPrinter(mesages:str):
    print(f"{red}[{GetTime()}]{kalın} [ERROR]: {kalın_reset}{blue}{mesages}{color_reset}")


# Uyarıları için
def WarnPrinter(mesages:str):
    print(f"{orange}[{GetTime()}]{kalın} [WARNING]: {kalın_reset}{blue}{mesages}{color_reset}")


#Log mesajları için
def LogPrinter(mesages:str):
    print(f"{blue}[{GetTime()}] [LOG]: {blue}{mesages}{color_reset}")


def TitlePrinter(your_title:str):
    print(f"{kalın}{blue}>> {your_title}{color_reset}{kalın_reset}")