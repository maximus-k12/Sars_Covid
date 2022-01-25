"""
funciones:

tomar_M()    --> foto_M.png, True<boolen>[True si tomo la foto]       > True, > False
tomar_m()    --> foto_m.png, ... 
"""

import cv2


"""
	En este caso, 0 quiere decir que queremos acceder
	a la cámara 0. Si hay más cámaras, puedes ir probando
	con 1, 2, 3...
"""
def foto_menor():
    
	cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)

	leido, frame1 = cap.read()

	if leido == True:
		cv2.imwrite("foto_menor.png", frame1)
		print("foto_menor.png tomada correctamente")
	else:
		print("Error al acceder a la cámara")

	"""
		Finalmente liberamos o soltamos la cámara
	"""
	cap.release()
	return print('foto guardada')


def foto_mayor():
    
	cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)
	cap.set(3, 1920)     
	cap.set (4, 1080) 
	leido, frame = cap.read()

	if leido == True:
		cv2.imwrite("foto_mayor.png", frame)
		print("foto_mayor.png tomada correctamente")
	else:
		print("Error al acceder a la cámara")

	"""
		Finalmente liberamos o soltamos la cámara
	"""
	cap.release()
	return print('foto guardada')

#foto_M()








