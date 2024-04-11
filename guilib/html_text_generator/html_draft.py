from hivelibrary.console_tools import GetTime

def gen_error_text(text:str) -> str:
    return f"[ {GetTime()} ] <B>[ ERROR ]: </B>{text}"


def gen_info_text(text:str) -> str:
    return f"[ {GetTime()} ] <B>[ INFO ]: </B>{text}"