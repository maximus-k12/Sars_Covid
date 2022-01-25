#librerias de imagen y texto

import reconocimientoImagen2
import regex
import mes_numero

#librerias Audio y voz
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import time
import os
import sys
#____________________________
from typing import Text, TextIO



#sugerir revise su DPI o introduzca nuevamente
def dpi_repetir():
    var_intro = "revise su DPI o introduzca nuevamente por favor"
    peticion = gTTS(var_intro,lang='es-ES')   
    peticion.save('metro4.mp3')
    peticion_var = 'metro4.mp3'
    playsound(peticion_var)
    
def hablar(var_intro):
    #var_intro = "revise su DPI o introduzca nuevamente por favor"
    peticion = gTTS(var_intro,lang='es-ES')   
    peticion.save('hablando.mp3')
    peticion_var = 'hablando.mp3'
    playsound(peticion_var)




#===============================Introduccion, opencv============================

var_intro = "Bienvenido. Introduzca su documento por favor"
tts = gTTS(var_intro,lang='es-ES')   
tts.save('metro.mp3')
intro_var1 = 'metro.mp3'
playsound(intro_var1)
#-------------------------------------------Bucle opencv
#time.sleep(4)
""" ----------->>> Eliminar estas comillas y meter tu codigo dentro del bucle Betuel."""

while True:
    #Code here...
    try:
        
        dpi,fecha,genero =reconocimientoImagen2.ocr()#dpi['1234 12345 1234'], fecha<['dia','mes','anio']>, genero<['FEMENINO']>
        print('Sus datos escaneados >>>:')
        print(dpi,fecha,genero)
        
        if(len(dpi)!=0 and len(fecha)!=0 and len(genero)!=0 ):
            diaNacimiento=fecha[0]
            mesNacimiento=fecha[1]
            anioNacimiento=fecha[2]
            print(diaNacimiento)
            print(mesNacimiento)
            print(anioNacimiento)
            
            break
        
        
        
        #if(len(dpi)!=0 and len(fecha)!=0 and len(genero)!=0 ):
        #    break
        
    except IndexError:
        print('excepcion 1 <<<<')
        dpi,fecha,genero =reconocimientoImagen2.ocr()#dpi['1234 12345 1234'], fecha<['dia','mes','anio']>, genero<['FEMENINO']>
        print(dpi,fecha,genero)
        
        diaNacimiento=fecha[0]
        mesNacimiento=fecha[1]
        anioNacimiento=fecha[2]
        
        
        print(diaNacimiento)
        print(mesNacimiento)
        print(anioNacimiento)
        break


        
#hablar('usted nacio el'+str(diaNacimiento)+'de'+ str(mesNacimiento)+ 'del anyo'+'{}, '.format(anioNacimiento) )
#time.sleep(1)
#hablar("su genero es"+genero)
#time.sleep(1)
#hablar("su DPI es "+DPI)



print(diaNacimiento)
print(mesNacimiento)
print(type(anioNacimiento))



#-------------------------------------------Final bucle
var_final = "Puede retirar su documento"
tts = gTTS(var_final,lang='es-ES')
tts.save('dexter.mp3')
final_var1 = 'dexter.mp3'
playsound(final_var1)
#===============================Final codigo, opencv============================
new_mess = "¿Usted está buscando primera o segunda dosis?"
tts = gTTS(new_mess,lang='es-ES')           ####  Meter todo esto dentro de una funcion. 
tts.save('dimto.mp3')

old_var = 'dimto.mp3'
playsound(old_var)
#__________________________________________________________________

r = sr.Recognizer()

with sr.Microphone() as source:
    #r.adjust_for_ambient_noise(source, duration=0.2) #Filtro de ruido 1
    print("Diga su dosis...")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='es-ES')
        print("What did you say: {}".format(text))
    except:
        print("I am sorry! I can not understand!")

#---------------------------------------------------------
#time.sleep(1)
nou = text
tts = gTTS(nou,lang='es-ES')
tts.save('miel.mp3')

shtn = "miel.mp3"
playsound(shtn)
#playsound('miel.mp3')

#---------------------------------------------------------
var_xyz = text

if var_xyz == 'primera':
    var1 = "¿Qué vacuna está buscando?"
    tts = gTTS(var1,lang='es-ES')
    tts.save('nilsa.mp3')
    vera = 'nilsa.mp3'
    playsound(vera)

    def first_vaccine():
    
        r = sr.Recognizer()

        with sr.Microphone() as source:
            #r.adjust_for_ambient_noise(source, duration=0.5) #Filtro de ruido 2
            print("Diga su vacuna...")
            audio = r.listen(source)

            try:
                texto = r.recognize_google(audio, language='es-ES')
                print("What did you say: {}".format(texto))
            except:
                print("I am sorry! I can not understand!")
            

        if texto == 'moderna':                  #Aca va el codigo para repetir vacuna
            var15 = "Por favor, diríjase a la fila uno"
            tts = gTTS(var15,lang='es-ES')
            tts.save('pfila.mp3')
            fila1 = 'pfila.mp3'
            playsound(fila1)

        elif texto == 'sputnik':
            var25 = "Por favor, diríjase a la fila dos"
            tts = gTTS(var25,lang='es-ES')
            tts.save('sfila.mp3')
            fila2 = 'sfila.mp3'
            playsound(fila2)

        elif texto == 'pfizer':
            var35 = "Por favor, diríjase a la fila tres"
            tts = gTTS(var35,lang='es-ES')
            tts.save('tfila.mp3')
            fila3 = 'tfila.mp3'
            playsound(fila3)

        elif texto == 'astrazeneca':
            var45 = "Por favor, diríjase a la fila cuatro"
            tts = gTTS(var45,lang='es-ES')
            tts.save('cfila.mp3')
            fila4 = 'cfila.mp3'
            playsound(fila4)

        else:
            print("Intentelo de nuevo.")
            prim_int = "Inténtelo de nuevo por favor"
            tts = gTTS(prim_int,lang='es-ES')        
            tts.save('second.mp3')
            reptr0 = 'second.mp3'
            playsound(reptr0)

            return first_vaccine()
    first_vaccine()

#***************************************************************

elif var_xyz =='segunda':
    var2 = "¿Qué vacuna está buscando?"
    tts = gTTS(var2,lang='es-ES')
    tts.save('julia.mp3')
    
    verso = 'julia.mp3'
    playsound(verso)

    def second_vaccine():

        r = sr.Recognizer()

        with sr.Microphone() as source:
            #r.adjust_for_ambient_noise(source, duration=0.5) #Filtro ruido 3
            print("Diga su vacuna...")
            audio = r.listen(source)

            try:
                texto2 = r.recognize_google(audio, language='es-ES')
                print("What did you say: {}".format(texto2))
            except:
                print("I am sorry! I can not understand!")

    
        if texto2 == 'moderna':
            var55 = "Por favor, diríjase a la fila cinco"
            tts = gTTS(var55,lang='es-ES')
            tts.save('qfila.mp3')
            fila5 = 'qfila.mp3'
            playsound(fila5)

        elif texto2 == 'sputnik':
            var65 = "Por favor, diríjase a la fila seis"
            tts = gTTS(var65,lang='es-ES')
            tts.save('sfila.mp3')
            fila6 = 'sfila.mp3'
            playsound(fila6)

        elif texto2 == 'pfizer':
            var75 = "Por favor, diríjase a la fila siete"
            tts = gTTS(var75,lang='es-ES')
            tts.save('setfila.mp3')
            fila7 = 'setfila.mp3'
            playsound(fila7)

        elif texto2 == 'astrazeneca':
            var85 = "Por favor, diríjase a la fila ocho"
            tts = gTTS(var85,lang='es-ES')
            tts.save('ofila.mp3')
            fila8 = 'ofila.mp3'
            playsound(fila8)

        else:
            print("Intentelo de nuevo.")
            sec_int = "Inténtelo de nuevo por favor"
            tts = gTTS(sec_int,lang='es-ES')        
            tts.save('nuevam.mp3')

            reptr1 = 'nuevam.mp3'
            playsound(reptr1)

            return second_vaccine()
    second_vaccine()

#***************************************************************
else:
    print("Repita su dosis")

