#!/usr/bin/env python3 

import random
import os
from pydub import AudioSegment
SUPPORTED_SOUND_FORMATS = ["MP3","OGG","FLAC","AAC","AIFF","WMA","WAV"]

# SES DEN METNE FONKSIYONUNDA GOOGLE API ICIN * FORMATDAN VAW FORMATINA CEVIRME FONKSIYONIU 
def GenericAudioConverter(target_file_path:str, temp_dir_path:str, TARGET_FILE_FORMAT="mp3") -> list:
    """ Desteklenen formatlardaki ses dosyalarını vaw foarmatına dönüştütüt
        Desteklenen formatlar -> "MP3","OGG","FLAC","AAC","AIFF","WMA","WAV"
    Args:
        target_file_path (str): hedef dosyanın dosya yolu 
        temp_dir_path (str, optional): final olarak oluşan *.vaw dosyasının kayıt konumu. Defaults to TEMP_DIR.
    Returns:
        dict: key: success -> true,false eğer urum başarılı ise success:true ve path döner değilse code:hata durumu
    UYARI: geri döndürülen path kendisi silinmez
    """
    TEMP_DIR = temp_dir_path
    
    if not os.path.exists(target_file_path) or not os.path.exists(temp_dir_path):
        return {"success":"false", "code":"invaid path"}
    
    target_file_extensions = target_file_path.split(".")
    target_file_extensions = target_file_extensions[len(target_file_extensions)-1]

    supported_formats = ["MP3","OGG","FLAC","AAC","AIFF","WMA","WAV"]
    
    if target_file_extensions.upper() not in supported_formats:
        return {"success":"false", "code":"not supported file extensions"}

    LoadedAudio = AudioSegment.from_file(target_file_path, format=target_file_extensions)
    export_name = TEMP_DIR+"exported_file_"+str(random.randint(1,999))+"."+TARGET_FILE_FORMAT
    
    # dosyanın export edilmesi 
    LoadedAudio.export(export_name, format=TARGET_FILE_FORMAT)

    if os.path.exists(export_name):
        return {"success":"true", "path":str(export_name)}
    else:
        return { "success":"false", "code":"export error"}


