lista=['21 ']
palabra = lista[0]
#texto = "21 "


"""
for x in range(len(characters)):
    texto = texto.replace(characters[x],"")

print(len(texto), texto)
"""


def eliminarCaracter(TEXTO,CARACTERES):
    for x in range(len(CARACTERES)):
        texto = TEXTO.replace(CARACTERES[x],"")
    return texto

texto= eliminarCaracter(palabra, " ")
print(texto,len(texto))

numero=int(palabra)

print(numero,type(numero))