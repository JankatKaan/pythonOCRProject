import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
gorsel = cv2.imread("C:\\Users\\kaan\\Downloads\\images.png")
gorsel = cv2.cvtColor(gorsel, cv2.COLOR_BGR2RGB)

hImg, wImg,_ = gorsel.shape
boxes = pytesseract.image_to_boxes(gorsel)
a= []
for b in boxes.splitlines():
    print(b)
    b = b.split(' ')
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(gorsel, (x,hImg- y), (w,hImg- h), (50, 50, 255), 2)
    cv2.putText(gorsel,b[0],(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
    a.append(b[0])
print(a)

cv2.imshow('gorsel', gorsel)
cv2.waitKey(0)