from database.commons.LoggerBase import logger

class Persona:

    def __init__(self,idPersona=None, nombre=None, apellido=None, email=None):
        self.__idPersona = idPersona
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email

    def __str__(self):
        return (f"Id Persona: { self.__idPersona}"
                f", Nombre: { self.__nombre}"
                f", Apellido: { self.__apellido}"
                f", e-mail: { self.__email}"
                )

    def getIdPersona(self):
        return self.__idPersona

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getApellido(self):
        return self.__apellido

    def setApellido(self, apellido):
        self.__apellido = apellido

    def getEmail(self):
        return self.__email

    def setEmail(self,email):
        self.__email = email

if __name__ == "__main__":
    persona1 = Persona(1,"Yo","Mero","yomero@email.com")
    logger.debug(persona1)

    #De esta manera se crea el objeto sin definir el idPersona, de lo contrario se puede poner None,
    # pero este valor no es tan util usarlo de esa manera
    persona2 = Persona(nombre="Paola", apellido="Gonzalez", email="paogonz@mail.com")
    logger.debug(persona2)

    #Simula el caso de eliminar un objeto de tipo persona
    persona3 = Persona(idPersona=3)
    logger.debug(persona3)



