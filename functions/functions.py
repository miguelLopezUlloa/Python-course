#En esta funcion se puede notar ="Human" es como si 
# usaras un constructor 

# En este caso esta tomando un valor por default y puedes invocar la
# funcion sin parametros en el llamado y no marca error
def hello(name="Human"):
    print("Hello World " + name)

hello("Mikauran")
hello()

print("*********************************")

def add(x, y):
    return x + y

print(add(10,30))
print("*********************************")

x = "global "

def foo():
    global x
    y = "local"
    
    # Operator overload: Is not a sum. Is a duplicate operation ( global global)
    x = x * 2
    print(x)
    print(y)

foo()
print("*********************************")

# Funcion lambda  Parametros : acciones de la funcion
newAdd = lambda numberOne,numberTwo: numberOne * numberTwo

print(newAdd(10,10))

print("*********************************")

# Default values for arguments can have default values in Python.
def greet(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """
    print("Hello", name + ', ' + msg)
    #print(greet,__doc__)
    

greet("Kate")
greet("Bruce", "How do you do?")

print("*********************************")

def greetTwo(*names):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)
        
greetTwo("Monica", "Luke", "Steve", "John")


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)

print("*********************************")
outer()
print("*********************************")