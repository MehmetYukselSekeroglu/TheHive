import rsa
import os
DEFAULT_CHARSET_ENCODINGS = "utf-8"
SUPPORTED_KEY_SIZES = [1024,2048,4096]

def generateNewKeyAndSave(keysize:int, key_name:str, save_dir:str) -> dict:
    if keysize not in SUPPORTED_KEY_SIZES:
        return {"success":False, "message":"Not supported keysize", "private_path":None, "public_path":None, "code":"invalid_ksize"}
    
    if os.name == "nt":
        check_digit = str(save_dir[-2:])
        if not str(os.path.sep) in check_digit:
            save_dir = str(save_dir) + str(os.path.sep)
    else:
        check_digit = str(save_dir[-1])
        if not str(os.path.sep) in check_digit:
            save_dir = str(save_dir) + str(os.path.sep)
            
                    
    PRIVATE_KEY_PATH = save_dir + key_name + ".priv"
    PUBLIC_KEY_PATH = save_dir + key_name + ".pub"
    
    if os.path.exists(PRIVATE_KEY_PATH) or os.path.exists(PUBLIC_KEY_PATH):
        return { "success":False, "message":"Key files alredy exists proccess stopped", "private_path":None, "public_path":None, "code":"keyfiles_exists"  }
    
    
    public_key, private_key = rsa.newkeys(keysize)
    
    with open(PUBLIC_KEY_PATH, "wb") as public_key_file:
        public_key_file.write(public_key.save_pkcs1())
    
    
    with open(PRIVATE_KEY_PATH, "wb") as private_key_file:
        private_key_file.write(private_key.save_pkcs1())
        
        
    return {"success":True,"message":"RSA new keys successfully generated","private_path": PRIVATE_KEY_PATH,
        "public_path":  PUBLIC_KEY_PATH,
        "code":"success"}
    



def loadPrivateKey(private_key_file_path:str) -> dict:
    if not os.path.exists(private_key_file_path):
        return {"success": "false","message": f"{private_key_file_path} not found"}
        
    with open(private_key_file_path, "rb") as private_key_file:
        key_data = private_key_file.read()
        key_data = rsa.PrivateKey.load_pkcs1(key_data)
        return {"success":"true","data": key_data}
        

def loadPublicKey(public_key_file_path:str) -> dict:
    if not os.path.exists(public_key_file_path):
        return {"success" : False,"message" : f"{public_key_file_path} not found"}
    
    with open(public_key_file_path, "rb") as public_key_file:
        key_data = public_key_file.read()
        key_data = rsa.PublicKey.load_pkcs1(key_data)
        return {"success" : True,"data": key_data}





def encrypte_string(public_key, target_string:str) -> str:
    target_string = str(target_string)
    return rsa.encrypt(target_string.encode(DEFAULT_CHARSET_ENCODINGS),pub_key=public_key)

def decrypte_string(private_key, target_string) -> str:
    return rsa.decrypt(target_string,priv_key=private_key).decode(DEFAULT_CHARSET_ENCODINGS) 