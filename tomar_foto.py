
import cv2


"""
	En este caso, 0 quiere decir que queremos acceder a la cámara 0.
	 Si hay más cámaras, puedes ir probando con 1, 2, 3...	
"""
cap = cv2.VideoCapture(1)


"""  
#resolucion de mi webCam  Resolución: 1 080p (1 920 x 1 080)
#Establezca la resolución de la cámara, 3 es alta, 4 es ancha,
"""
cap.set(3, 1920)     
cap.set (4, 1080) 



print(" >> tomando foto.......")
leido, frame = cap.read()



if leido == True:
	cv2.imwrite("foto.png", frame)
	print("\n Foto tomada correctamente\n")
else:
	print("Error al acceder a la cámara")

"""
	Finalmente liberamos o soltamos la cámara
"""
cap.release()