from Polymorph.Empleado import Empleado
from Polymorph.Gerente import Gerente

def imprimirDetalles(objElement):
    print(objElement)
    print(type(objElement), end="\n\n")

    # Recuerda que isistance permite checar si el objeto
    # pertenece algun tipo
    if isinstance(objElement, Gerente):
        print(objElement)
        print(objElement.departamento)
    else: print("Tipo Desconocido")

empleado = Empleado("Juan", 1000.00)
imprimirDetalles(empleado)

# De acuerdo al tipo de objeto se cambia el comportamiento para acceder
# al tipo de objeto determinado
empleado = Gerente("Mikauran", 4500.09, "Sistemas")
imprimirDetalles(empleado)

