import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='192.168.1.69',
                            port='5432',
                            database='TestDb')

cursor = conexion.cursor()

sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'

# Se necesita crear una Tupla de Tuplas para contener varios registros
valores = (
    ('Jesus', 'Motolinia', 'jmotolinia@mail.com'),
    ('Martha','Sanchez','msanchez@mail.com'),
    ('Pablo', 'Picasso', 'pabpicasso@mail.com')
)

# Se usa executemany para insertar varios registros
cursor.executemany(sentencia, valores)

# Se guarda la información en la base de datos hasta que se de commit
conexion.commit()

registrosInsertados = cursor.rowcount
print(f"Registros insertados: {registrosInsertados}")

cursor.close()
conexion.close()