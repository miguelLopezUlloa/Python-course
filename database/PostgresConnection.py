import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='192.168.1.69',
                            port='5432',
                            database='TestDB')

cursor = conexion.cursor()
#sentencia = 'SELECT * FROM persona ORDER BY id_persona'
#sentencia = 'SELECT * FROM persona WHERE id_persona=1 ORDER BY id_persona'
# Esta ultima sentencia esta sustituyen el valor de id_persona, con el valor de una variable
sentencia = 'SELECT * FROM persona WHERE idpersona=%s ORDER BY idpersona'

# Se tiene el id en la variable, y posteriomente se asigna a primaryKey
# que contien una tupla. De esta manera python lo toma con la coma al final.
id_persona=2
primaryKey = (id_persona,)

# En esta parte se usa la primary key para ser pasada en este execute
# antes para las instrucciones en comentario de arriba no se usaba
cursor.execute(sentencia, primaryKey)
#registros = cursor.fetchall()
registros = cursor.fetchone()

print(registros)

cursor.close()
conexion.close()