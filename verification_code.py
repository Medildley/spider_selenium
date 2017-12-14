import pytesseract 
from PIL import Image

img = Image.open('1.jpg')
str = pytesseract.image_to_string(img, lang='eng', config='-psm 7')
print(str)

img = Image.open('2.jpg')
str = pytesseract.image_to_string(img, lang='eng', config='-psm 7')
print(str)

img = Image.open('3.jpg')
str = pytesseract.image_to_string(img, lang='eng', config='-psm 7')
print(str)

img = Image.open('4.jpg')
str = pytesseract.image_to_string(img, lang='eng', config='-psm 7')
print(str)

#img.show()
#str = pytesseract.image_to_string(img, lang='chi_sim', config='-psm 7')
