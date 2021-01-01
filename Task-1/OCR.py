import numpy as np
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
img=cv2.imread("Capture1.PNG",1)

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img))
#Detecting the Character
#print(pytesseract.image_to_boxes(img))
#config="--psm 3"
config="--oem 3 --psm 6 outputbased digits "
Height,Width,_=img.shape
boxes=pytesseract.image_to_boxes(img,config=config)
for i in boxes.splitlines():
    #print(i)
    i=i.split(' ')
    #print(i)
    x,y,w,h=int(i[1]),int(i[2]),int(i[3]),int(i[4])
    cv2.rectangle(img,(x,Height-y),(w,Height-h),(0,0,255),1)

cv2.imshow('Task',img)
cv2.waitKey(5000)
cv2.destroyAllWindows()