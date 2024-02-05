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
    
    day_is = current_time.tm_mday
    mount_is = current_time.tm_mon
    year_is = current_time.tm_year
    zone_is = current_time.tm_zone
    
    formatted_time = f"{day_is}/{mount_is}/{year_is} {hour:02d}:{minute:02d}:{second:02d}"
    
    return formatted_time

# BILGILENDIRMELER ICIN 
def InformationPrinter(mesages:str):
    
    print(f"{green}[{GetTime()}]{kalın} [ info ]: {kalın_reset}{mesages}")


# HATA MESAJLARI ICIN 
def ErrorPrinter(mesages:str):
    print(f"{red}[{GetTime()}]{kalın} [ error ]: {kalın_reset}{mesages}")


# Uyarıları için
def WarnPrinter(mesages:str):
    print(f"{orange}[{GetTime()}]{kalın} [ warning ]: {kalın_reset}{mesages}")


#Log mesajları için
def LogPrinter(mesages:str):
    print(f"{blue}[{GetTime()}] [ log ]: {mesages}")


def TitlePrinter(your_title:str):
    print(f"{kalın}{blue}>> {your_title}{color_reset}{kalın_reset}")