from excepciones.NumberEqualsException import NumberEqualsException

class Exception1:

    def __init__(self):
        print("Manage exception are ready")

    def mngExceptionCase1(self):
        resultado = None
        a = "10"
        b = 0

        try:
            resultado = a/b
        # except ZeroDivisionError as e --> Esta manera solo atrapara Division / 0 y la de Typo NO
        except Exception as e:
            print("Ocurrio un error", e)
            print(type(e))

        print("Continua el procesamiento....")
        print("El resultado de la operacion es:",resultado)

    def mngExceptionCase2(self):
        resultado = None
        a = int(input("Introduce un número:"))
        b = int(input("Introduce otro número:"))

        try:
            resultado = a / b
        # except ZeroDivisionError as e --> Esta manera solo atrapara Division / 0 y la de Typo NO
        except ZeroDivisionError as e:
            print("Ocurrio un error atrapado por ZeroDivisionError", e)
            print(type(e))
        except TypeError as e:
            print("Ocurrio un error atrapado por Type Error", e)
            print(type(e))
        except ValueError as e:
            print("Ocurrio un error atrapado por Value Error", e)
            print(type(e))
        except Exception as e:
            print("Ocurrio un error atrapado por Exception Gral", e)
            print(type(e))
        else:
            print("No se presento ninguna exception")
        finally:
            print("Fin del manejo de Exceptions")

        print("Continua el procesamiento....")
        print("El resultado de la operacion es:", resultado)

    def mngExceptionCase3(self):
        resultado = None

        try:
            a = int(input("Introduce un número:"))
            b = int(input("Introduce otro número:"))

            if a == b:
                raise NumberEqualsException("Detectados Números Identicos en los valores introducidos..")

            resultado = a/b
        # except ZeroDivisionError as e --> Esta manera solo atrapara Division / 0 y la de Typo NO
        except Exception as e:
            print("Ocurrio un error.. +:", e)
            print(type(e))

        print("Continua el procesamiento....")
        print("El resultado de la operacion es:",resultado)

    def listAllExceptions(self):
        print(dir(locals()['__builtins__']))
        #print("Hola")

excpt = Exception1()
#excpt.mngExceptionCase1()
#excpt.mngExceptionCase2()
excpt.mngExceptionCase3()
print("*" *60)
#excpt.listAllExceptions()

