# Importamos la libreria Pillow
from PIL import Image

# Importamos Pytesseract
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# Abrimos la imagen
im = Image.open("foto_test2.png")

# Utilizamos el método "image_to_string"
# Le pasamos como argumento la imagen abierta con Pillow
texto = pytesseract.image_to_string(im)

# Mostramos el resultado
print(texto)# -*- coding: utf-8 -*-

