"""
funciones que escanea el texto del ocr

scanGenero()    --> genero <str>                            > 'FEMENINO'
scanDpi()       -->  numero de pi <str>                     > ['1727 07536 4242']
scanFecha()     --> [dia]<str>, [mes]<str>, [anio]<str>     > ['21','MAY','2020' ]

"""
#import main

import os
from posixpath import dirname
import re
from typing import AsyncIterator, MutableSequence

from cv2 import DIST_FAIR


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#__________elimar espacios____________
def eliminarCaracter(TEXTO,CARACTERES):
    for x in range(len(CARACTERES)):
        texto = TEXTO.replace(CARACTERES[x],"")
    return texto

# _________mesANumero("JUL")-->'07'______       
def mesANumeroInt(mes): 
    m = {
        'ENE': "01",
        'FEB': "02",
        'MAR': "03",
        'ABR': "04",
        'MAY': "05",
        'JUN': "06",
        'JUL': "07",
        'AGO': "08",
        'SEP': "09",
        'OCT': "10",
        'NOV': "11",
        'DIC': "12"
        }


    out = str(m[mes])
    return int(out) 

def mesANumeroStr(mes): 
    m = {
        'ENE': "01",
        'FEB': "02",
        'MAR': "03",
        'ABR': "04",
        'MAY': "05",
        'JUN': "06",
        'JUL': "07",
        'AGO': "08",
        'SEP': "09",
        'OCT': "10",
        'NOV': "11",
        'DIC': "12"
        }


    out = str(m[mes])
    return out

# Datos de una lista, 0, 1 ,2, ...  ----------------------------
def DatosEnLista(lista):
    return len(lista)

#__________fechas_scan_________________
#para fecha #21MAY1990              ----------------------------
def scanfecha1(Texto):  
    fecha= re.findall(r'\d{2}\D{3}\d{4}', Texto, re.M)#21MAY1990
    if (DatosEnLista(fecha)>0):
        DIA = re.findall(r'^\d{2}', fecha[0], re.M)
        MES =re.findall(r'\D{3}', fecha[0], re.M)
        ANIO =re.findall(r'\d{4}', fecha[0], re.M)
        return DIA, MES, ANIO
    else:
        return scanfecha2(Texto)
#para fecha #21MAY 1990             ----------------------------
def scanfecha2(Texto):  
    fecha= re.findall(r'\d{2}\D{3}\s+\d{4}', Texto, re.M)#21MAY 1990
    if (DatosEnLista(fecha)!=0):
        DIA= re.findall(r'^\d{2}', fecha[0], re.M)
        MES= re.findall(r'\D{3}\s', fecha[0], re.M)
        ANIO= re.findall(r'\d{4}', fecha[0], re.M)
        return DIA,MES , ANIO
    else:
        return scanfecha3(Texto)
#para fecha3 #21 MAY1990             ---------------------------- 
def scanfecha3(Texto):  
    fecha= re.findall(r'\d{2}\s+\D{3}\d{4}', Texto, re.M)#21 MAY1990
    if (DatosEnLista(fecha)!=0):
        DIA = re.findall(r'\d{2}\s', fecha[0], re.M)
        MES =re.findall(r'\D{3}', fecha[0], re.M)
        ANIO =re.findall(r'\d{4}', fecha[0], re.M)
        return DIA,MES , ANIO
    else:
        return scanfecha4(Texto)
#para fecha4 #21 MAY 1990            ----------------------------  
def scanfecha4(Texto):  
    fecha= re.findall(r'\d{2}\s+\D{3}\s+\d{4}', Texto, re.M)#21 MAY 1990
    if (DatosEnLista(fecha)!=0):
        DIA =re.findall(r'\d{2}\s', fecha[0], re.M)
        MES =re.findall(r'\s+\D{3}\s', fecha[0], re.M)
        ANIO =re.findall(r'\d{4}', fecha[0], re.M)
        return DIA, MES, ANIO
        #DIA=int(DIA[0])   
        #MES=eliminarCaracter(MES[0]," ")
        #MES=mesANumero(MES)
        #ANIO = int(ANIO[0])
    else:
        return scanfecha5(Texto)  
def scanfecha5(Texto):
    fecha= re.findall(r'\d\D{3}\s+\d{4}', Texto, re.M)#OS5DIC 1992
    #print(fecha)
    if (DatosEnLista(fecha)!=0):
        DIA = re.findall(r'^\d', fecha[0], re.M)
        MES = re.findall(r'\D{3}\s', fecha[0], re.M)
        ANIO = re.findall(r'\d{4}', fecha[0], re.M)
        return DIA,MES,ANIO
    else:    
        return fecha
    
    
def scanFecha(textoCon_fecha):
    texto=textoCon_fecha
    return scanfecha1(texto)


#_________generos_____________    
def generoMasculino(textoCon_Masculino):
    content=textoCon_Masculino
    GENERO='MASCULINO'
    genero= re.findall(r'..SCU.IN.', content, re.M)#MASCULINO
    if(DatosEnLista(genero)!=0):#si genero hizo match
        return GENERO
    
    genero= re.findall(r'CU.IN.', content, re.M)#MASCULINO
    if(DatosEnLista(genero)!=0):#si genero hizo match
        return GENERO
    
    genero= re.findall(r'CU.IN.', content, re.M)#MASCULINO
    if(DatosEnLista(genero)!=0):#si genero hizo match
        return GENERO

    genero= re.findall(r'CU..N.', content, re.M)#MASCULINO
    if(DatosEnLista(genero)!=0):#si genero hizo match
        return GENERO
    
    genero= re.findall(r'MASC', content, re.M)#MASCULINO
    if(DatosEnLista(genero)!=0):#si genero hizo match
        return GENERO
    else:
        return ''   
    
def scanMasculino1(content):
    genero= re.findall(r'..SCU.IN.', content, re.M)#MASCULINO
    if(DatosEnLista(genero)!=0):#si hizo match
        return genero
    
def scanMasculino1(content):
    genero= re.findall(r'CU.IN.', content, re.M)#MASCULINO
    if(DatosEnLista(genero)!=0):#si hizo match
        return genero




def generoFemenino(texto):
    content=texto
    GENERO='FEMENINO'
    genero= re.findall(r'F.M.N', content, re.M)#FEMENINO
    if(DatosEnLista(genero)>0):#si genero hizo match
        return GENERO
    
    genero= re.findall(r'EME..N.', content, re.M)#FEMENINO
    if(DatosEnLista(genero)>0):#si genero hizo match
        return GENERO
    
    genero= re.findall(r'.M.N.N.', content, re.M)#FEMENINO
    if(DatosEnLista(genero)>0):#si genero hizo match
        return GENERO

    genero= re.findall(r'M.N.N.', content, re.M)#FEMENINO
    if(DatosEnLista(genero)>0):#si genero hizo match
        return GENERO
    
    
    genero= re.findall(r'FEME', content, re.M)#FEMENINO
    if(DatosEnLista(genero)>0):#si genero hizo match
        return GENERO
    
    genero= re.findall(r'F.M.N.N.', content, re.M)#FEMENINO
    if(DatosEnLista(genero)>0):#si genero hizo match
        return GENERO
    
    else:
        return ''

def scanGenero(texto):

    if(DatosEnLista(generoFemenino(texto))!=0):
        return generoFemenino(texto)
    else:
        if(DatosEnLista(generoMasculino(texto))!=0):
            return generoMasculino(texto)
        else:
            return 'indefinido'
#__________dpi___________
def scanDpi(textoCon_dpi):
    content=textoCon_dpi
    dpis = re.findall(r'\d+\s\d+\s\d{4}', content, re.M) # scan dpi------
    return dpis


#________________________________Ejecucion regex_________________________________




if __name__ == '__main__':
    with open(os.path.join(BASE_DIR, 'dpi_info.txt'), 'r') as f1:
        content = f1.read()

    """   
    print(content)
    #scan DPI------------
    dpi= scanDpi(content)
    #print(dpis)
    print("\n")
    print(dpi)
    
    
    
    #scan fechas----------
    fecha= scanFecha(content)#OS5DIC 1992
    print(len(fecha))
    
    genero=scanGenero(content)#
    print(genero)
    """
    
    
"""    
    try:
        
        dia, mes, anio = scanFecha(content) 
        
        print(dia)
        print(mes)
        print(anio)
        
    except:
        fecha=scanFecha(content)
        print(fecha)

    genero=scanGenero(content)
    print(genero)
    




           

with open(os.path.join(BASE_DIR, 'texto_mayor.txt'), 'r') as f1:
        texto_mayor = f1.read()
dpi=scanDpi(texto_mayor)
print(dpi)

""" 