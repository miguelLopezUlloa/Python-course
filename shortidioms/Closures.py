
def outer_functions(x):
    y = 4

    def inner_function(z):
        print(f" x = { x }, y ={y}, z= { z }")

        return x + y + z

    return inner_function

def functionWithClosures():
    numbers = [1,2,3,4]
    funcs = []

    # Take care...x = n is required to move the n value
    # to x
    for n in numbers:
        funcs.append(lambda x=n: print(x))

    # The for loop use the funcs list to
    # invoke f like a function name f()
    for f in funcs:
        f()

def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    printer()

"""
function print_msg_CaseTwo() returned the printer() function instead of calling it
"""
def print_msg_CaseTwo(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    return printer  # returns the nested function


"""
 In this case the closure are starting from the closurences method
 and back to the outer_functions
"""
print("*" *60)
closurences = outer_functions(10)
closurences(6)

print("*" *60)
functionWithClosures()

print("*" *60)
print_msg("Hello world using closures")

print("*" *60)
another = print_msg_CaseTwo("Hello Case Two")
another()

