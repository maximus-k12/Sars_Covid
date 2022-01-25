import mysql.connector

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="root", 
                                  database="labcom4")
cursor1=conexion1.cursor()

sql="insert into datos_vacunacion(DPI, GENERO, FECHA_FACUNACION, DOSIS) values (%s,%s,%s,%s)"

datos=("DPI", "1234 12345 1234")
cursor1.execute(sql, datos)
datos=("GENERO", "MASCULINO")
cursor1.execute(sql, datos)
datos=("FECHA_VACUNACION", "2021 10 28")
cursor1.execute(sql, datos)
datos=("DOSIS", "SEGUNDA")

cursor1.execute(sql, datos)
conexion1.commit()
conexion1.close() 