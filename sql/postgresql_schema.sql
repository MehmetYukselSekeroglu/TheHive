CREATE TABLE IF NOT EXISTS {"system_core"} (
     id SERIAL PRIMARY KEY,
     unique_key VARCHAR(100) NOT NULL UNIQUE,
     value VARCHAR(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS {"blob_storage"} (
    id SERIAL PRIMARY KEY,
    unique_blob_key TEXT NOT NULL UNIQUE,
    key_value BYTEA NOT NULL,
    data_type TEXT NOT NULL DEFAULT 'user',
    information_notes TEXT DEFAULT NULL
);
CREATE TABLE IF NOT EXISTS {"authentication"} (
    id SERIAL PRIMARY KEY,
    username VARCHAR(128) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL
);
CREATE TABLE IF NOT EXISTS {"face_recognition_standart"} (
    id SERIAL PRIMARY KEY,
    face_picture_blob BYTEA NOT NULL, 
    picture_sha1_hash TEXT NOT NULL UNIQUE,
    face_embedding_data BYTEA NOT NULL,
    landmarks_2d BYTEA NOT NULL,
    face_box BYTEA NOT NULL,
    face_name TEXT NOT NULL,
    add_date TIMESTAMP DEFAULT NOW()
);
