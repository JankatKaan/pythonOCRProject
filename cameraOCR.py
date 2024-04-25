import pytesseract
import cv2
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
while True:
    _, frame = cap.read()
    imgH, imgW, _ = frame.shape
    x1, y1, w1, h1 = 0, 0, imgH, imgW
    text = pytesseract.image_to_string(Image.fromarray(frame))
    print(text)
    cv2.putText(frame, text, (x1 + int(w1 / 50), y1 + int(h1 / 50)), font, 1.5, (0, 0, 0), 2)
    cv2.imshow("Resim", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
print(text)
