from primeexternal.instagram_parser.instagram_db_tools import instagramStorageDatabaseTools
import sqlite3

            
if __name__ == "__main__":
    db = sqlite3.Connection("hive_database.sqlite3")
    db_curosr = db.cursor()
    app = instagramStorageDatabaseTools(db_cnn=db, db_curosr=db_curosr)
    print(app.execute_database_schema())
    print(app.get_total_record_in_db())