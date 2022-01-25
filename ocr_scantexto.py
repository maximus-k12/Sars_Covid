import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

"""  
image = cv2.imread('d1.jpg')
image = cv2.imread('d2.png')
image = cv2.imread('foto.png')
"""
image = cv2.imread('foto2.png')

texto = pytesseract.image_to_string(image)
print('Texto: ',texto)
      
#cv2.imshow('Image',image)
#cv2.waitKey(0)
cv2.destroyAllWindows()


destFile = r"dpi_info.txt"
with open(destFile, 'a') as f:
    f.write(texto)

text2='------------------------------------------------'
destFile = r"dpi_info.txt"
with open(destFile, 'a') as f:
    f.write(text2)

