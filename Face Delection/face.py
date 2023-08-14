import cv2
face_cap=cv2.CascadeClassifier('face.xml')

video_cap=cv2.VideoCapture(0)
while True:
    ret, video_data=video_cap.read()
    col=cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
    faces=face_cap.detectMultiScale(col,1.1,4)
    for(x,y,w,h) in faces:
     cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Face_Detection_Project",video_data)
    if cv2.waitKey(10)==ord(" "):
        break
video_cap.release()