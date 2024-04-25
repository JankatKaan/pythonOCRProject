import pytesseract
from pdf2image import convert_from_path
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

#Add path to pdf file which converted to image for OCR
dokuman = "C:\\Users\\kaan\\Downloads\\ocrDemoFile.pdf"
doc = convert_from_path(dokuman, poppler_path='C:\\Program Files\\poppler-24.02.0\\Library\\bin')

for i, image in enumerate(doc):
    gorsel = 'image'+str(i)+'.png'
    image.save(gorsel, "PNG")
    text = pytesseract.image_to_string(gorsel, lang="tur")
    print(text)
