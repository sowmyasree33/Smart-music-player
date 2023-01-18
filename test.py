import cv2
from fer import FER

def take_input(count):
    video = cv2.VideoCapture(0) 
    
    while True:
        check, frame = video.read()
        if(check):
            if frame is not None:  
                cv2.imshow('cap', frame)
                key = cv2.waitKey(1)
                if key == 13:
                    break
        
    emotion_detector = FER(mtcnn=True)
    
    showPic = cv2.imwrite("photo.png",frame)
    print(showPic)
    test_img_low_quality = cv2.imread('photo.png')
    analysis = emotion_detector.detect_emotions(test_img_low_quality)
    #print(analysis)
    dominant_emotion, emotion_score = emotion_detector.top_emotion(test_img_low_quality)
    print(dominant_emotion, emotion_score)
    print("inside test.py")
    if (dominant_emotion==None) and (count<3):
        count+=1
        print(count)
        take_input(count)
    video.release()
    cv2.destroyAllWindows()
