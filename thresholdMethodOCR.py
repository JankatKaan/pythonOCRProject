import pytesseract
import cv2
image = cv2.imread("C:\\Users\\kaan\\Downloads\\3images.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 3)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

config = "--psm 6"

text = pytesseract.image_to_string(binary, config=config, lang='eng')
print(text)

cv2.imshow("Orjinal", image)
cv2.imshow("Binary", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
