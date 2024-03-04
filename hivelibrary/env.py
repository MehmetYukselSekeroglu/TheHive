import os


# table structure
DB_SYSTEM_TABLE = "system_core"
DB_BLOB_STORAGE = "blob_storage"
DB_LOCAL_AUTHENTICATE_TABLE = "authentication"
DB_FACE_RECOGNITION_TABLE = "face_recognition_standart"

# Data storage types
DB_DATA_TYPE__SYSTEM = "system"
DB_DATA_TYPE__USER = "user"


# Application value 
APPLICATION_VENDOR_VALUE = "Prime Security"
APPLICATION_NAME_VALUE = "The Hive Remastred"
APPLICATION_VERSION_VALUE = "2.0.0"

DATABASE_INIT_STATUS = "database_status"

# Application database keys
APPLICATION_VENDOR_KEY = "application_vendor"
APPLICATION_NAME_KEY = "application_name"
APPLICATION_VERSION_KEY = "application_version"
SHODAN_API_KEY = "shodan_api_key"
VIRUSTOTAL_API_KEY = "virustotal_api_key"

DATABASE_NAME = "thehive"


DATABASE_FILE_NAME = "hive_database.sqlite3"
DATABASE_PATH = DATABASE_FILE_NAME

# Default charset 
DEFAULT_CHARSET = "utf-8"


# default log file
DEFAULT_LOG_FILE_NAME = "hive_logs.txt"


# default app root dir
DEFAULT_ROOT_DIR_NAME = "data"
DEFAULT_TEMP_DIR ="tmp"


# DEFAULT LOGO PATH
DEFAULT_LOGO_PATH = f"iconfiles{os.path.sep}logo.png"