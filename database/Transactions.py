import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='192.168.1.69',
                            port='5432',
                            database='TestDb')
try:
    # conexion.autocommit = True

    cursor = conexion.cursor()

    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'

    # Se necesita crear una Tupla de Tuplas para contener varios registros
    valores = (
        ('Ramiro', 'Gamboa', 'tioGamboin@mail.com'),
        ('Gaspar', 'Henaine', 'gasHenaine@mail.com'),
    )

    sentenciaUpdate = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'

    # Se necesita crear una Tupla de Tuplas para contener varios registros
    valorUpdate = ('Jesus Nahum', 'Motolinia', 'jnmotolinia@mail.com', 5)

    # Se usa executemany para insertar varios registros
    cursor.executemany(sentencia, valores)

    # Se guarda la información en la base de datos hasta que se de commit
    conexion.commit()

except Exception as e:
    conexion.rollback()
    print("Ocurrio un error en la transaccion:", e)
finally:
    cursor.close()
    conexion.close()