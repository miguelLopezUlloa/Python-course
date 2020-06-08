# ALCANCE GLOBAL SIN DECLARACION

#c = 1 # global variable
    
#def add():
#    c = c + 2 # increment c by 2
#    print(c)

#add()
# LANZA --> UnboundLocalError: local variable 'c' referenced before assignment


# ESTE ES LA MANERA CORRECTA
c = 0 # global variable

def add():
    global c
    c = c + 2 # increment by 2
    print("Inside add():", c)

add()
print("In main:", c)
print("*" *60)

""" This method is working with other inner and with global scope
but for the inner functions
"""
def foo():
    x = 20

    def bar():
        global x
        x = 25
    
    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)

foo()
print("x in main: ", x)
