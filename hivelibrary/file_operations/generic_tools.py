

def binaryData(file_path:str) -> bytes:
    with open(file_path, "rb") as target:
        return target.read()