import hashlib
from hivelibrary.env import DEFAULT_CHARSET





def string_to_hash(hash_strings="NULL", hash_algorithm="sha512") -> dict:
    if hash_strings == "NULL" or hash_strings == "":
        return {
            "success" : "false",
            "message" : "HASH STRING IS NULL!"
        }
    
    if hash_algorithm == "sha1":
        hasher = hashlib.sha1()
    elif hash_algorithm == "sha256":
        hasher = hashlib.sha256()
    elif hash_algorithm == "sha512":
        hasher = hashlib.sha512()
    elif hash_algorithm == "md5":
        hasher = hashlib.md5()
    elif hash_algorithm == "sha224":
        hasher = hashlib.sha224()
    else:
        return {
            "success" : "false",
            "message" : "NOT SUPPORTED HASH ALGORITHM!"
        }
    
    hasher.update(hash_strings.encode("utf-8"))
    hashed_data = str(hasher.hexdigest())
    return {
        "success" : "true",
        "data" : hashed_data
    }



def sha512hasher(text:str) -> str:
    hasher = hashlib.sha512()
    hasher.update(text.encode(DEFAULT_CHARSET))
    return str(hasher.hexdigest())

def loginCreditHhasher(text:str) -> str:
    text = sha512hasher(text=text)
    text = sha512hasher(text=text)
    return text






