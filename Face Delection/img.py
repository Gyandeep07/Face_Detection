import cv2
face_casecade=cv2.CascadeClassifier('face.xml')
img=cv2.imread('img1.jpg')
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_casecade.detectMultiScale(grey,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('img',img)
cv2.waitKey()