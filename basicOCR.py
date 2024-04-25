import pytesseract
from PIL import Image
resim = "C:\\Users\\kaan\\Downloads\\images.png"
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
gorsel = Image.open(resim)

text = pytesseract.image_to_string(gorsel)
print(text)