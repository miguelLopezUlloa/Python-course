
from database.commons.LoggerBase import logger
import psycopg2 as pool
import sys

class ConnectionDB:
    __DATABASE = "TestDB"
    __USERNAME = "postgres"
    __PASSWORD = "admin"
    __DBPORT = "5432"
    __HOST = "192.168.1.69"
    __MIN_CON = 1
    __MAX_COM = 5
    __pool = None

    @classmethod
    def getPool(cls):
        if cls.__pool is None:
            try:
                cls.__pool = pool.SimpleConnection(
                    cls.__MIN_CON,
                    cls.__MAX_COM,
                    host=cls.__HOST,
                    user=cls.__USERNAME,
                    password=cls.__PASSWORD,
                    port=cls.__DBPORT,
                    database=cls.__DATABASE)
                logger.debug(f"Pool Conexion exitosa: {cls.__connection}")
                return cls.__pool
            except Exception as e:
                logger.error(f"Error al crear el Pool de Conecciones {e}")
                sys.exit()
        return cls.__pool


    @classmethod
    def getConnection(cls):
       #Obtener conexion
       connection = cls.getPool().getconn()
       logger.debug(f"Coneccion obtenida del Pool { connection }")

       return connection


    @classmethod
    def freeConnections(cls, conexion):
        cls.getPool().putconn(conexion)
        logger.debug(f"Regrese la connection al Pool { conexion }")
        logger.debug(f"Estado del Pool { cls.__pool }")

    @classmethod
    def closeConnections(cls):
        #Cerrar el Pool de conexiones
        cls.getConnection().closeall()


if __name__ == '__main__':
    #Obtener una conexion a partir del Pool
    conexion1 = ConnectionDB.getConnection()