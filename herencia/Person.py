# import Human
from component.Human import Human

class Person(Human):
    pass


yo = Person()

print(id(Person))
print(Human.name)

tu = Person()
tu.name = "Diana"

print(tu.name)
