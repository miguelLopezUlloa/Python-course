class FileReader:

    def __init__(self):
        print("Starting Read process")


    def readBasic(self):
        try:
            #Para cuando se tiene que leer en un ubicación diferente el archivo a leer
            #archivo = open("C:\\Users\\Miguel_Ulloa\\Documents\\Devs\\Python\python\\archivos\\prueba.txt")
            archivo = open("prueba.txt")
            print(archivo.read())
        finally:
            archivo.close()

    def readSomeChars(self):
        try:
            archivo = open("prueba.txt")

            print(archivo.read(5))
            print(archivo.read(3))
        finally:
            archivo.close()


    def readLines(self):
        try:
            archivo = open("prueba.txt")

            print(archivo.readline())
            print(archivo.readline())
        finally:
            archivo.close()


    def readLoopLines(self):
        try:
            archivo = open("prueba.txt")

            for linea in archivo:
                print(linea)
        finally:
            archivo.close()


    def readAllLinesList(self):
        try:
           archivo = open("prueba.txt")

           print(archivo.readlines())

            # Lee el archivo, usando la posicion de la lista que regresa
            # readlines()
            #print(archivo.readlines()[1])
        finally:
            archivo.close()


    def copyFile(self):
        try:
           archivo = open("prueba.txt")

            #Usando  a en el segundo parametro.
           # Si ya existe el file no lo borra, y le agrega
           # el contenido al final.
           # COn w se crea el archivo.
           archivo2 = open("copia.txt", "w")
           archivo2.write(archivo.read())

        finally:
            archivo.close()
            archivo2.close()




read1 = FileReader()
# Lee todo el archivo de un solo paso
#read1.readBasic()

# Lee solo algunos caracteres del archivo. Los que se necesiten
#read1.readSomeChars()

# Lee linea por linea un archivo
#read1.readLines()

# Lee el archivo en un ciclo linea por linea
read1.readLoopLines()

#read1.readAllLinesList()

#read1.copyFile()



