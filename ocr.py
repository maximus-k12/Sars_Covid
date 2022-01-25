import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def fotoM_textoM():
    """  
    image = cv2.imread('d1.jpg')
    image = cv2.imread('d2.png')

    """
    image = cv2.imread('foto_M.png')

    texto = pytesseract.image_to_string(image)
    #print('Texto: ',texto)
        
    #cv2.imshow('Image',image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    return texto
