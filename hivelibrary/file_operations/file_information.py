import os


def sizeMB(file_path:str) -> str:
    data_is = os.path.getsize(file_path)
    kb_size = data_is / 1024
    if kb_size < 1.0:
        return f"{round(data_is,2)} Bayt"
    
    mb_size = kb_size / 1024
    if mb_size < 1.0:
        return f"{round(kb_size,2)} KB"
    
    return f"{round(mb_size,2)} MB"


        