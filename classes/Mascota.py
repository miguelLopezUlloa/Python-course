class Mascota:

    #Constructor con auto inicializacion
    """ def __init__(self):
        self.name = "Terry"
        self.age = 0
        self.size = 0 """

    #Constructor con parametros
    def __init__(self, name, age, size):
        self.name = name
        self.age = age
        self.size = size

    def run(self):
        return "The pupy is running"

    def getName(self):
        return self.name

dog = Mascota("Chiquitin", 2, 12)

print(dog.getName())
print(dog.run())

print("********************************")



