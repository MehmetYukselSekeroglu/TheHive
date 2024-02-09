import hashlib
from hivelibrary.env import DB_FACE_RECOGNITION_TABLE
import psycopg2



# for postgresql


def get_image_from_id(db_cursor,db_id:int) -> dict:
    try:
        
        STATIC_SQL_COMMAND = f"SELECT * FROM {DB_FACE_RECOGNITION_TABLE} WHERE id=%s"
        STATIC_DATA_TUPLE = (db_id,)
        
        db_cursor.execute(STATIC_SQL_COMMAND,STATIC_DATA_TUPLE)
        results = db_cursor.fetchall()
        
        if len(results) < 1:
            return { "success":False , "data":"No results" }
        
        return { "success":True, "data":results[0][1] }
        
    
    except Exception as err:
        return { "success":False, "data":f"Failed to get data, {err}" }


class recognitionDbTools():
    
    def __init__(self, db_curosr, db_cnn) -> None:
        
        self.databaseConnections = db_cnn
        self.databaseCursor = db_curosr
        

    def calculateImageHashFromCv2Data(self, cv2_image_data):
        image_hash = hashlib.sha1(cv2_image_data.tobytes())
        image_hash = image_hash.hexdigest()
        return image_hash
        
        
    def check_hash_is_exists(self, image_hash)-> bool:
        
        STATIC_SQL_COMMAND = f"SELECT EXISTS(SELECT 1 FROM {DB_FACE_RECOGNITION_TABLE} WHERE picture_sha1_hash=%s);"
        STATIC_DATA_TUPLE = (str(image_hash),)
        
        self.databaseCursor.execute(STATIC_SQL_COMMAND,STATIC_DATA_TUPLE)
        results = self.databaseCursor.fetchall()[0][0]
        
        if results == False:
            return False
        
        return True
        
    
    def check_name_is_exists(self, face_name) -> bool:
        STATIC_SQL_COMMAND = f"SELECT EXISTS(SELECT 1 FROM {DB_FACE_RECOGNITION_TABLE} WHERE face_name=%s);"
        STATIC_DATA_TUPLE = (str(face_name),)
        
        self.databaseCursor.execute(STATIC_SQL_COMMAND,STATIC_DATA_TUPLE)
        results = self.databaseCursor.fetchall()[0][0]
        
        if results == False:
            return False
        
        return True
        
        
            
    
    
    
    def insertImageFromDB(self,cv2_image_data, image_binary_data, face_name:str, insightface_face_analyser_ojb:object):
        try:
            cv2_image_hash = self.calculateImageHashFromCv2Data(cv2_image_data=cv2_image_data)
            
            if self.check_hash_is_exists(cv2_image_hash) == True:
                return {"success":False, "data":"İlgili resim zaten veritabanı içerisinde mevcuttur bu nedenle ekleme iptal edildi."}

            face_name = face_name

            if self.check_name_is_exists(face_name=face_name) == True:
                return {"success":False, "data":"İlgili isim veritabanında zaten mevcut tekrar kullanılamaz, işlem iptal edildi"}
  
                
            blobl_image_data = image_binary_data


            analysedSourceImage = insightface_face_analyser_ojb.get(cv2_image_data)
        
            if len(analysedSourceImage) > 1:
                return { "success":False, "data":"Kaynak resimde 1 den fazla yüz kabul edilemez, işlem iptal edili" }

            if len(analysedSourceImage) == 0:
                return {"success":False, "data":"Kaynak resimde herhangi bir yüz bulunamadı, işlem iptal edildi."}
            
            face_embedding_sourceFile = analysedSourceImage[0]["embedding"]
            landmark_2d = analysedSourceImage[0]["landmark_2d_106"]
            face_box = analysedSourceImage[0]["bbox"]
            
            
            
            STATIC_SQL_COMMAND = f"""INSERT INTO {DB_FACE_RECOGNITION_TABLE} (
                face_picture_blob, picture_sha1_hash, face_embedding_data, landmarks_2d, face_box, face_name)
                VALUES (%s, %s, %s, %s, %s,%s )"""
            STATIC_DATA_TUPLE = (blobl_image_data, str(cv2_image_hash), psycopg2.Binary(face_embedding_sourceFile), psycopg2.Binary(landmark_2d),psycopg2.Binary(face_box) ,str(face_name))
            
            self.databaseCursor.execute(STATIC_SQL_COMMAND, STATIC_DATA_TUPLE)
            self.databaseConnections.commit()
            return { "success":True, "data":"Resim başarıyla veritabanına eklendi." }
        
        
        except Exception as err:
            return { "success":False, "data":f"Yüz ekleme işlemi esnasında hata gerçekleşti işlem iptal edildi, {err}" }

    
    
    