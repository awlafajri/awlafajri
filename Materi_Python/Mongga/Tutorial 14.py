import cv2
import numpy as np

img = cv2.imread("depresiface.jpg")



img=cv2.resize(img,(640,480))

#cv2.imshow("Gambar 1",img)
#cv2.imshow("Gambar 2",imgresized)
#cv2.waitKey(0)

#imggray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#imgblur1 = cv2.GaussianBlur(img,(1,1),10)
#imgblur5 = cv2.GaussianBlur(img,(5,5),10)
imgcanny = cv2.Canny(img,10,50)

kernel=np.ones((5,5),np.uint8)
imgDilation= cv2.dilate(imgcanny,kernel,iterations=1)
imgEroded=cv2.erode(imgcanny,kernel,iterations=1)
imgEroded2=cv2.erode(img,kernel,iterations=1)


#cv2.imshow("blur1",imgblur1)
#cv2.imshow("blur10",imgblur10)
#cv2.imshow("blur5",imgblur5)
#cv2.imshow("img",img)
#cv2.imshow("imgcanny",imgcanny)
#cv2.imshow("imgdil",imgDilation)
#cv2.imshow("imge",imgEroded)
#cv2.imshow("imge2",imgEroded2)

imgcropped=img[0:100,0:200]
cv2.imshow("img",img)
cv2.imshow("crop",imgcropped)

cv2.waitKey(0)

