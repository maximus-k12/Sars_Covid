
import mysql.connector

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="root", 
                                  database="labcom4")
cursor1=conexion1.cursor()
cursor1.execute("select DPI, GENERO, FECHA_VACUNACION, DOSIS from datos_vacunacion")
for fila in cursor1:
    print(fila)
conexion1.close()  