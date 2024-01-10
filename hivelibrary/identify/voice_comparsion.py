import os
import numpy as np
from resemblyzer import preprocess_wav, VoiceEncoder


def CompareSounds(sound_1_path:str, sound_2_path:str) -> dict:
    if not os.path.exists(sound_1_path) or not os.path.exists(sound_2_path):
        return { "success":False, "code":"file not found" }
    
    sound_encoder = VoiceEncoder(verbose=False)
    file_1 = preprocess_wav(sound_1_path)
    file_2 = preprocess_wav(sound_2_path)

    encoded_sound1 = sound_encoder.embed_utterance(file_1)
    encoded_sound2 = sound_encoder.embed_utterance(file_2)

    dot_product_size = np.dot(encoded_sound1, encoded_sound2)
    norm_sound1 = np.linalg.norm(encoded_sound1)
    norm_sound2 = np.linalg.norm(encoded_sound2)

    # kosinus benzerliğini hesaplama 
    GetSimilarity = dot_product_size / (norm_sound1 * norm_sound2)
    GetSimilarity = GetSimilarity * 100
    GetSimilarity = int(GetSimilarity)
    return { "success":True ,"similarity":str(GetSimilarity) }