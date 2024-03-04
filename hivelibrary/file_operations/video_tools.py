import cv2 
import os


SUPPORTED_VIDEO_FORMATS = ["avi","mp4","mkv","mov","flv","wmv","webm","mpeg","mpg"]


def preparedVideoForCV2(video_path:str) -> dict:
    if not os.path.exists(video_path) or os.path.isdir(video_path):
        return { "success":False, "data":"invalid file path" }
    try:
        TargetVideo = cv2.VideoCapture(video_path)
    except Exception as err:
        return {"success":False, "data":err }

    return {"success":True, "data":TargetVideo}


def releaseVideoForCV2(preparedVideo:cv2.VideoCapture) -> dict:
    preparedVideo.release()

def getFrameCountOnVideo(preparedVideo:cv2.VideoCapture, counter:int) -> dict:
    while(True):
        is_succes, now_frame = preparedVideo.read()
        if is_succes:
            cv2.imwrite(f"tmp{os.sep}cv2output{os.sep}frame_{FrameNumber}.jpg", now_frame)
        else:
            break

    FrameNumber = FrameNumber + 1
    print("\n[+] Finished...")
    preparedVideo.release()
    


def frame_sharpening(frame) -> object:
    converGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    konstrat_arttir = cv2.adaptiveThreshold(converGray,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11,2)
    clear_noise = cv2.bilateralFilter(frame,9,75,75)
    finaly_image = cv2.addWeighted(clear_noise, 1.5,konstrat_arttir,-0.5,0)
    return finaly_image