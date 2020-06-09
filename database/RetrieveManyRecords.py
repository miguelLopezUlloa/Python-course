import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='192.168.1.69',
                            port='5432',
                            database='TestDb')

cursor = conexion.cursor()

sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
entrada = input("Proporciona las pk a buscar (separado por comas):")
tupla = tuple(entrada.split(','))
print(tupla)

primaryKeys = (tupla,)

# En esta parte se usa la primary key para ser pasada en este execute
# antes para las instrucciones en comentario de arriba no se usaba
cursor.execute(sentencia, primaryKeys)
registros = cursor.fetchall()

for registro in registros:
    print(registro)
#print(registros)

cursor.close()
conexion.close()