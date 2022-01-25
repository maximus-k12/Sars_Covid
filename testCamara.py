"""
activa camara para poder graduar el lente y la distancia de enfoque
cierra camara pulsando la tecla 'q'
"""

from typing import no_type_check
import cv2
import numpy as no_type_check

def tomarfoto_M():
    #iniciamos camara web
    cap = cv2.VideoCapture(1)
    """ """  
    cap.set(3, 1920)     
    cap.set (4, 1080) 
    

    while(True):
        #capturamos video frame a frame
        ret, frame = cap.read()

        #mostrar frame capturado
        cv2.imshow('Visor',frame)

        # presionar 'q' finalizamos prueba y guardamos 'foto_test.png'
        if cv2.waitKey(1):
            if ret == True:
                cv2.imwrite("foto_M.png", frame)
                print("\n >>> se tomo foto_M.png \n")
            else:
                print("---no se capturo foto de muestra :c ")
            break

    #finalizamos camara y cerramos ventana
    cap.release()
    cv2.destroyAllWindows()

def tomarfoto_m():
    #iniciamos camara web
    cap = cv2.VideoCapture(1)
    """  
    cap.set(3, 1920)     
    cap.set (4, 1080) 
    """ 

    while(True):
        #capturamos video frame a frame
        ret, frame = cap.read()

        #mostrar frame capturado
        cv2.imshow('Visor',frame)

        # presionar 'q' finalizamos prueba y guardamos 'foto_test.png'
        if cv2.waitKey(1):
            if ret == True:
                cv2.imwrite("foto_m.png", frame)
                print("\n >>> se tomo foto_m.png \n")
            else:
                print("---no se capturo foto de muestra :c ")
            break

    #finalizamos camara y cerramos ventana
    cap.release()
    cv2.destroyAllWindows()

#captura_M=tomarfoto_M()
captura_m=tomarfoto_m()

#testear el ocr
#import testOcr