from PIL import Image
from pytesseract import pytesseract

path_to_tesseract = '/opt/homebrew/bin/tesseract'

image_path = "/Users/ananya/Downloads/img.jpg"

img = Image.open(image_path)

pytesseract.tesseract_cmd = path_to_tesseract

text = pytesseract.image_to_string(img)

print(text[:-1])
