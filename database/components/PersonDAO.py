from database.components.Person import Persona
from database.model.ConnectionDB import ConnectionDB
from database.commons.LoggerBase import logger

class PersonDAO:
    ''' DAO (Data Access Object)'''

    __SELECCIONAR = "SELECT * FROM persona ORDER BY idpersona"
    __INSERTAR = "INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)"
    __ACTUALIZAR = "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE idpersona=%s"
    __ELIMINAR = "DELETE FROM persona WHERE idPersona=%s"


    @classmethod
    def seleccionar(cls):
        cursor = ConnectionDB.getCursor()
        # Manda a consola el Select validandolo previamente
        logger.debug(cursor.mogrify(cls.__SELECCIONAR))
        cursor.execute(cls.__SELECCIONAR)
        records = cursor.fetchall()
        persons = list()

        for row in records:
            persona = Persona(row[0], row[1], row[2], row[3])
            persons.append(persona)

        ConnectionDB.closeConnection()

        return persons

    @classmethod
    def insertar(cls, person):
        #Se necesita crear una transacción
        try:
            connection = ConnectionDB.getConnection()
            cursor = ConnectionDB.getCursor()

            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f"Persona a insertar: { person}")
            values = (person.getNombre(), person.getApellido(), person.getEmail())

            cursor.execute(cls.__INSERTAR, values)
            connection.commit()

            return cursor.rowcount
        except Exception as e:
            connection.rollback()
            logger.error(f"Exception in insert operation using Person object: { e }")
        finally:
            ConnectionDB.closeConnection()

    @classmethod
    def actualizar(cls, persona):
        try:
            connection = ConnectionDB.getConnection()
            cursor = ConnectionDB.getCursor()

            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f"Persona a actualizar: {person}")
            values = (person.getNombre(), person.getApellido(), person.getEmail(), person.getIdPersona())

            cursor.execute(cls.__ACTUALIZAR, values)
            connection.commit()
            return cursor.rowcount

        except Exception as e:
            connection.rollback()
            logger.error(f"Exception in Update operation using Person object: {e}")
        finally:
            ConnectionDB.closeConnection()

    @classmethod
    def borrar(cls, persona):
        try:
            connection = ConnectionDB.getConnection()
            cursor = ConnectionDB.getCursor()

            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f"Persona a Eliminar: {person}")
            values = (person.getIdPersona())

            cursor.execute(cls.__ELIMINAR, values)
            connection.commit()
            return cursor.rowcount

        except Exception as e:
            connection.rollback()
            logger.error(f"Exception in Delete operation using Person object: {e}")
        finally:
            ConnectionDB.closeConnection()



if __name__ == "__main__":

    #Operacion de Select
    persons = PersonDAO.seleccionar()

    for person in persons:
        logger.debug(person)

    # Operacion de Insert

    persons2 = Persona(nombre="Peter", apellido="Pan", email="peterpan@mail.com")
    personsInserted = PersonDAO.insertar(persons2)
    logger.debug(f"Personas Insertadas: { personsInserted }")

    '''
    persons3 = Persona(1, "Peter", "Parker","parkers@mail.com")
    personsUpdated = PersonDAO.actualizar(persons3)

    persons4 = Persona(idPersona=7)
    personsDeleted = PersonDAO.borrar(persons4)
    logger.debug(f"Persona eliminada es: { personsDeleted }")
    '''



