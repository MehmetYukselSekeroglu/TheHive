


#
# config.json generator for TheHive Remastred
#

# external library import's
import json
import sys
import os

# local library import's
from .env import CONFIG_FILE_PATH as __CONFIG_FILE_PATH__
from .consolePrint import (p_info, p_error)



# private varables
__BASE_DIR__ = os.getcwd() + os.path.sep
__TEMP_DIR__ = __BASE_DIR__ + "tmp" + os.path.sep
__DATA_DIR__ = __BASE_DIR__ + "data" + os.path.sep
__SQL_SCHMEA_PATH__ = __BASE_DIR__ + "sql" + os.path.sep + "postgresql_schema.sql"


# for json
__CONFIG_FILE_DATA__ = {
    
    "vendor":"Prime Security",
    "name":"TheHive",
    "version":"0.0.0+1",
    "base_dir":__BASE_DIR__,
    "temp_dir":__TEMP_DIR__,
    "data_dir":__DATA_DIR__,
    "database_schema":__SQL_SCHMEA_PATH__,
    
    "database_config":{
            "database":"thehive",
            "user":"postgres",
            "password":"your_secret_password",
            "host":"127.0.0.1",
            "port":"5432",
    },
    "insightface":{
        "ctx_id":-1,
        "det_thresh":0.5,
        "det_size":(640,640)
        }
    
        
    
    
    
    
    
}


# if executed the module run config generator 
if __name__ == "__main__":
    os.makedirs(str(__CONFIG_FILE_PATH__.split(os.path.sep)[-2]), exist_ok=True)

    try:
        with open(__CONFIG_FILE_PATH__,"w+") as conf_file:
            json.dump(__CONFIG_FILE_DATA__,conf_file,indent=4)
        
    except Exception as err:
        p_error(f"Failed to crate {__CONFIG_FILE_PATH__}, {err}")
        sys.exit(-1)        

    p_info(f"{__CONFIG_FILE_PATH__} successfuly generated.")
    sys.exit(0)














