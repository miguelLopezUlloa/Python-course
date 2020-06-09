import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='192.168.1.69',
                            port='5432',
                            database='TestDb')

cursor = conexion.cursor()

sentencia = 'DELETE FROM persona WHERE id_persona=%s'

# Se necesita crear una Tupla de Tuplas para contener varios registros
#valores = (10,)
entrada = input("Proporcina la pk a eliminar:")
valores = (entrada,)

# Se usa execute para actualizar un registro
cursor.execute(sentencia, valores)

# Se guarda la información en la base de datos hasta que se de commit
conexion.commit()

registrosDeleted = cursor.rowcount
print(f"Registros Eliminados: {registrosDeleted}")

cursor.close()
conexion.close()