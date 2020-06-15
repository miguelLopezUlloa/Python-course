
from database.commons.LoggerBase import logger
import psycopg2 as db
import sys

class ConnectionDB:
    __DATABASE = "TestDB"
    __USERNAME = "postgres"
    __PASSWORD = "admin"
    __DBPORT = "5432"
    __HOST = ""
    __connection = None
    __cursor = None

    @classmethod
    def getConnection(cls):
        if cls.__connection is None:
            try:
                cls.__connection = db.connect(host=cls.__HOST,
                                            user=cls.__USERNAME,
                                            password=cls.__PASSWORD,
                                            port= cls.__DBPORT,
                                            database= cls.__DATABASE)
                logger.debug(f"Conexion exitosa: {cls.__connection}")
                return cls.__connection
                sys.exit()

            except Exception as e:
                logger.error(f"Error al conectar a la BD:[{e}]")
        else:
            return cls.__connection

    @classmethod
    def getCursor(cls):
        if cls.__cursor is None:
            try:
                cls.__cursor = cls.getConnection().cursor()
                logger.debug(f"Se abrio el cursor con exito: { cls.__cursor }")
                return cls.__cursor
            except Exception as e:
                logger.error(f"Error al obtener cursor: {e}")
                sys.exit()

    @classmethod
    def closeConnection(cls):
        if cls.__cursor is not None:
            try:
                cls.__cursor.close()
            except Exception as e:
                logger.error(f"Error al cerrar Cursor: { e }")
        if cls.__connection is not None:
            try:
                cls.__connection.close()
            except Exception as e:
                logger.error(f'Error al cerrar la conexion: { e }')
        logger.debug("Se han cerrado los objetos de conexion y cursor")




if __name__ == '__main__':
    #logger.info(ConnectionDB.getConnection())
    logger.info(ConnectionDB.getCursor())
    ConnectionDB.closeConnection()