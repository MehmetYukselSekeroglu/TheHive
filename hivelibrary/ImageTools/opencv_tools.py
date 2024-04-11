import cv2
import numpy



def landmarks_rectangle(cv2_image:numpy.ndarray, data_list:list) -> numpy.ndarray:
    left, top, right, bottom = map(int, data_list)
    cv2.rectangle(cv2_image, (left, top), (right, bottom), (0, 255, 0), 3)
    return cv2_image


def landmarks_rectangle_2d(cv2_image:numpy.ndarray, data_list:list) -> numpy.ndarray:
    for landmark_point in data_list:
        x,y = map(int, landmark_point)
        cv2.circle(cv2_image, (x,y),1, (0,255,0), -1)
        
    return cv2_image



def draw_face_name(cv2_image:numpy.ndarray, face_name:str, data_list:list) -> numpy.ndarray:
    left, top, right, bottom = map(int, data_list)
    cv2.putText(cv2_image,face_name,(left, top - 15),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)

    pass