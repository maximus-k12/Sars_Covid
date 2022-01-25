import time
import os
from posixpath import dirname
import re
from typing import AsyncIterator, MutableSequence


import camara
import testOcr
import regex

def ocr():
    
    #TOMAMOS FOTOS en alta y baja resolucion y ESCANEAMOS sus caracteres ____________

    camara.foto_mayor()#toma 'foto_M.png' y devuelve 'True'
    texto_mayor=testOcr.ocr('foto_mayor.png')#ocr escanea 'foto_M.png'
    #print(texto_M)
    f = open ('texto_mayor.txt','w')
    f.write(texto_mayor)
    f.close()

    #time.sleep(2)

    camara.foto_menor()
    texto_menor=testOcr.ocr('foto_menor.png')
    #print(texto_m)
    f = open ('texto_menor.txt','w')
    f.write(texto_menor)
    f.close()

    """  
    #ejecutamos RECONOCIMIENTO CARACTERES ___________________
        #texto_mayor
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(BASE_DIR, 'texto_mayor.txt'), 'r') as f1:
            _texto_mayor = f1.read()
        #texto menor
    with open(os.path.join(BASE_DIR, 'texto_menor.txt'), 'r') as f1:
            _texto_menor = f1.read()
    """

    #sacan dpi____
    dpi1 = regex.scanDpi(texto_mayor)
    if (len(dpi1)!=0):
        dpi=regex.scanDpi(texto_mayor)
    else:
        dpi=regex.scanDpi(texto_menor)


    #scan fecha___
    fecha1=regex.scanFecha(texto_mayor)
        #print(len(fecha1))
    if (len(fecha1)!=0):
        fecha=regex.scanFecha(texto_mayor)
    else:
        fecha=regex.scanFecha(texto_menor)


    #scan genero___
    genero=regex.scanGenero(texto_mayor)

    return dpi, fecha, genero

'''
dpi,fecha,genero =ocr()
print(dpi)
print(fecha)    
print(genero)
'''  


