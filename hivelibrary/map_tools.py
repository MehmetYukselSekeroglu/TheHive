import io
import folium



def drawNewMap(cordinate_array_or_tuple, note_text:str=None,zoom_start:int=6) -> bytes:
    MemStorage = io.BytesIO()
    cordinate_array_or_tuple = tuple(cordinate_array_or_tuple)
    newMap = folium.Map(location=cordinate_array_or_tuple, zoom_start=zoom_start)
    
    if note_text is not None:
        folium.Marker(location=cordinate_array_or_tuple, popup=note_text).add_to(newMap)
        
    newMap.save(outfile=MemStorage,close_file=False)
    return MemStorage.getvalue().decode()
    