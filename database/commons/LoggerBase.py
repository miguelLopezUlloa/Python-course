import logging

#Esta es la variable que se va a utiilizar
logger = logging

logger.basicConfig(level=logging.DEBUG,
                   format = '%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] --> %(message)s',
                   datefmt='%m/%d/%Y %I:%M:%S %p',
                   handlers = [logging.FileHandler('dataLogs.log'),
                               logging.StreamHandler()
                   ])
#Propiedad de un archivo si se esta ejecutando desde este archivo
# Es decir desde donde se esta ejecuntando al momento de la ejecución
if __name__ == '__main__':
    logging.warning("Mensaje a nivel warning")
    logging.info("Mensaje a nivel Info")
    logging.debug("Mensaje a nivel Debugg")
    logging.error("Ocurrio un error en la base de datos")
    logging.debug("Se realizo la conexion a la base de datos con exito")