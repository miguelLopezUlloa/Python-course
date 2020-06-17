import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='192.168.1.69',
                            port='5432',
                            database='TestDB')

cursor = conexion.cursor()

sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE idpersona=%s'

# Se necesita crear una Tupla de Tuplas para contener varios registros
valores = ('Jesus Nahum', 'Motolinia', 'jnmotolinia@mail.com',5)

# Se usa execute para actualizar un registro
cursor.execute(sentencia, valores)

# Se guarda la información en la base de datos hasta que se de commit
conexion.commit()

registrosUpdated = cursor.rowcount
print(f"Registros Actualizados: {registrosUpdated}")

cursor.close()
conexion.close()