import psutil, platform, socket, os



def get_hostname() -> object:
    try:
        return socket.gethostname()
    except Exception:
        return "Failed To Detect"
    
    
def total_cpu_count() -> object:
    return os.cpu_count()


def get_active_user() -> object:
    return os.getlogin()


def patlform_info() -> object:
    return platform.platform()



# cpu and other source usaga statics
def get_cpu_usage() -> object:
    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent 


def get_battery_percentage() -> str:
    battery = psutil.sensors_battery()
    percentage = "%"+str(round(battery.percent,1)) if battery else "Bilinmiyor"
    return percentage


def get_memory_usage() -> dict:
    memory = psutil.virtual_memory()
    total = memory.total / (1024 ** 3)  # GB
    used = memory.used / (1024 ** 3)  # GB
    percentage = memory.percent
    return { "total":round(total, 1),"used": round(used,1),"yüzde": percentage}


def max_thread_calculator() -> int:
    total_cpı = total_cpu_count()
    maxThread = total_cpı
    return maxThread