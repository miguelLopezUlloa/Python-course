from classes.Constants import MY_CONSTANT
from classes.Constants import ConstantApply as mate

print(MY_CONSTANT)
print("El valor de mi PI es:", mate.PI)

""" PERO ES UNA SIMULACION LA CTE
POR QUE SI SE PUEDE CAMBIAR """
MY_CONSTANT = "CONTANT CHANGE IN REAL TIME"
mate.PI_OWN = 3.14

print("Nuevo valor para la pseudo Constant:", MY_CONSTANT)
print("Nuevo valor para Mi propio PI es:", mate.PI_OWN)

