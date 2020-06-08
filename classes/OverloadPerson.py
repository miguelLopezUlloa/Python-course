class Person:

    def __init__(self, name):
        self.__name = name

    # Se esta sobre escribiendo de la clase padre object
    # en su metodo __add__
    def __add__(self, other):
        return self.__name + " " + other.__name

    # Se sobre escribio __sub__ y con el mensaje
    # para indicar que no se soporta la operacion
    def __sub__(self, other):
        return "Operacion no soportada"


p1 = Person("Juan")
p2 = Person("Paul")

# A este nivel no es posible concantenar los dos
# objetos. Aunque lo que se esta buscando es concatenar
# en su atributo name
# y automaticamente se usa __add__()
print( p1 + p2)

print(p1 - p2)

"""
    Se tienen tablas para saber que metodos se pueden sobre cargar
    para cada operador
"""
