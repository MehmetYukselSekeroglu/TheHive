import subprocess
import os
import json
import sys
import time

# TheHive Wimdows Controller 
# 


# Return Codes 
# -1 -> Config File Not Found 



CONFIG_PATH = "config" + os.path.sep + "config.json"


def p_error(msg):
    print(f"[ERROR]: {msg}")

def p_info(msg):
    print(f"[INFO]: {msg}")

def p_warn(msg):
    print(f"[WARNING]: {msg}")   


def printHelp():
    currentFile = sys.argv[0]
    print("\n")
    print(f"--- TheHive Windows Controller Help Menu ---\n")
    print(f"python {currentFile} --help\t\t\t:open this menu and exit")
    print(f"python {currentFile} --generate-container\t:generate new docker container for TheHive")
    print(f"python {currentFile} --prepare-psql\t\t:prepare PostgreSQL server")
    print(f"python {currentFile} --remove-container\t\t:stop and remove docker container !DANGER!")
    print(f"python {currentFile} --start-container\t\t:start the container")
    print(f"python {currentFile} --stop-container\t\t:stop the container")
    print(f"python {currentFile} --check-commands\t\t:check required command status")
    print(f"python {currentFile} --sql-shell:\t\t:start sql shell for container")
    print(f"python {currentFile} --install-pip-packaget\t:install required pip packagets")
    print(f"python {currentFile} --wizard\t\t\t:otomatik indirme yardımcısı")

    print("\n")




def executeSelf(param:str):
    _commands_is = [str(sys.executable.replace(os.sep, os.path.sep)), "windows.py", param]

    subprocess.run(_commands_is,stdout=sys.stdout,shell=True)
    

def startHive():
    _commands_is = [str(sys.executable.replace(os.sep, os.path.sep)), "main.py"]
    subprocess.run(_commands_is,shell=True, stdout=sys.stdout)



def checkCommands(cmd:str) -> None:

    _commands_is = ["powershell","Get-Command", cmd ,"-ErrorAction", "SilentlyContinue"]
    _err = ""
    _std_out = ""
    commandStatus = subprocess.run(_commands_is,capture_output=True,shell=True)
    
    if commandStatus.returncode != 0:
        p_error(f"{cmd} not found, install and add path !")
        print(commandStatus.returncode)
        sys.exit(1)
    else:
        p_info(f"{cmd} detected the system, good...")



if not os.path.exists(CONFIG_PATH):
    p_error(f"Config file not found: {CONFIG_PATH}")
    sys.exit(-1)
    

with open(CONFIG_PATH, "r") as configFile:
    JsonData = json.loads(configFile.read())
    

p_info(f"Reading Config File: {CONFIG_PATH}")

databaseNmae = JsonData["database_config"]["database"]
databasePassword = JsonData["database_config"]["password"]
databaseUser = JsonData["database_config"]["user"]
databaseHostname = JsonData["database_config"]["host"]
databasePort = JsonData["database_config"]["port"]

databaseSchemaPath = JsonData["database_schema"]
databaseMaxConnection = 500
containerPackageName ="postgres"   # container package name

WindowsBinaryPath = "binary" + os.path.sep + "windows" + os.path.sep

# reference!
# -d -p 5432:$db_port -e POSTGRES_PASSWORD=$db_password $container_package_name -N $postgre_max_connections


containerNmae = databaseNmae + "-postresql-container"


# reference
#    docker exec -t $container_name psql -p $db_port -h $db_hostname -U $db_username -c "CREATE DATABASE \"$db_name\";"

# reference
#     docker exec -t $container_name psql -p $db_port -h $db_hostname -U $db_username -d "$db_name" -f $CONTAINER_SCHEMA_PATH




def stopContainer():
    _command = [
        "powershell", "docker", "stop", containerNmae
    ]

    commandStatus = subprocess.run(_command,capture_output=True,shell=True)

    if commandStatus.returncode != 0:
        p_error(f"container durdurma işlemi başarısız oldu!\t{containerNmae}")
        print(f"*"*100)
        print(commandStatus.stderr.decode("utf-8"))
        print(f"*"*100)
        sys.exit(2)
    else:
        p_info(f"Başarıyla duruldu:\t{containerNmae}")


def startContainer():
    _command = [
        "powershell", "docker", "start", containerNmae
    ]

    commandStatus = subprocess.run(_command,capture_output=True,shell=True)

    if commandStatus.returncode != 0:
        p_error(f"container başlatma işlemi başarısız oldu!\t{containerNmae}")
        print(f"*"*100)
        print(commandStatus.stderr.decode("utf-8"))
        print(f"*"*100)
        sys.exit(2)
    else:
        p_info(f"Başarıyla başlatıldı:\t{containerNmae}")
        
        
        
def preparePsql():
    _command = [
        "powershell", "docker", "exec", "-t", str(containerNmae), "psql", "-p" ,str(databasePort),
        "-h", str(databaseHostname), "-U", str(databaseUser), f"""--command "CREATE DATABASE {databaseNmae}" """
    ]
    p_info(f"Making new database: {databaseNmae}")
    commandStatus = subprocess.run(_command,capture_output=True,shell=True)

    if commandStatus.returncode != 0:
        p_error("PostgreSQL preparing işleminde hata oldu!")
        print(f"*"*100)
        print(commandStatus.stderr.decode("utf-8"))
        print(commandStatus.stdout.decode("utf-8"))
        print(f"*"*100)
        sys.exit(2)
        
    _command = [
        "powershell", "docker", "exec", "-t", str(containerNmae), "psql", "-p", str(databasePort), "-h", str(databaseHostname),
        "-d", str(databaseNmae), "-f", databaseSchemaPath 
    ]
    
    p_info(f"Executing schema: {_command}")
    commandStatus = subprocess.run(_command,capture_output=True,shell=True)

    if commandStatus.returncode != 0:
        p_error("PostgreSQL .sql import işleminde hata oldu!")
        print(f"*"*100)
        print(commandStatus.stderr.decode("utf-8"))
        print(f"*"*100)
        sys.exit(2)

    p_info("PostgreSQL hazır!")



def installPackage(package:str) -> None:
    _command = ["powershell", "python", "-m", "pip", "install", package]
    commandStatus = subprocess.run(_command,capture_output=True,shell=True)

    if commandStatus.returncode != 0:
        p_error(f"indirme işlemi başarısız oldu!\t{package}")
        print(f"*"*100)
        print(commandStatus.stderr.decode("utf-8"))
        print(f"*"*100)
        sys.exit(2)
    else:
        p_info(f"Başarıyla indirildi:\t{package}")

def installPipPackaget():
    
    
    
    
    with open("requirements.txt", "r",encoding="utf-8") as pipFile:
        p_info("pip paketleri kuruluyor...")
        for line in pipFile:
            line = line.strip()
            
            if line == "insightface":
                p_warn(f"Daha sonra indirilecek:\t{line}")
                continue
            
            installPackage(line)
            
        
    
    p_info("Gereksiz kaynak harcanmasın diye önceden derlenmiş paketlere geçildi...")

    for packaget in os.listdir(WindowsBinaryPath):
        if packaget.endswith(".whl"):
            installPackage(package=str(WindowsBinaryPath+packaget))

    p_info("işlem tamamlandı")


def generateDocker():
    
    _command = ["powershell", "docker", "run", "--name", containerNmae, "-d", "-p", f"5432:{databasePort}",
                "-e",f"POSTGRES_PASSWORD={databasePassword}", str(containerPackageName), "-N" ,str(databaseMaxConnection)  ]

    commandStatus = subprocess.run(_command,capture_output=True,shell=True)

    if commandStatus.returncode != 0:
        p_error("Yeni docker container oluşturma işleminde hata oldu!")
        print(f"*"*100)
        print(commandStatus.stderr.decode("utf-8"))
        print(f"*"*100)
        sys.exit(2)
        return
    else:
        p_info("Yeni docker container başarıyla oluşturuldu!")
        return



if len(sys.argv) < 2:
    printHelp()
    sys.exit(1)


currentParam = sys.argv[1]



if currentParam.lower() == "--help":
    printHelp()
    sys.exit(0)
    

elif currentParam == "--generate-container":
    generateDocker()
    
elif currentParam == "--prepare-psql":
    preparePsql()
    
elif currentParam == "--install-pip-packaget":
    installPipPackaget()

elif currentParam == "--start-container":
    startContainer()
    
elif currentParam == "--stop-container":
    stopContainer()
    
elif currentParam == "--start-hive":
    startHive()

elif currentParam == "--wizard":
    p_info("Otomatik indirme başlatılıyor...")
    
    executeSelf("--check-commands")
    executeSelf("--install-pip-packaget")
    executeSelf("--generate-container")
    p_info("container ın stabil olması için 10 saniye uyku moduna girildi...")
    time.sleep(10)
    executeSelf("--prepare-psql")
    executeSelf("--start-hive")
    
    
elif currentParam == "--check-commands":
    p_info("Checking Required Commands ...")
    checkCommands("docker")
    checkCommands("pip")
    sys.exit(0)



