import cv2

#img = cv2.imread("gambar.png")

#cv2.imshow("Gambar 1",img)
#cv2.waitKey(0)

cap = cv2.VideoCapture(0)
cap.set(3,640) #atur dimensi lebar
cap.set(4,480) #atur dimensi tinggi
cap.set(10,1000) #ini atur brightness

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break