class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
     
     # Se sobre escribe str para poder mostrar los valores de los atributos   
    def __str__(self):
        return "Nombre:" + self.nombre + ", Edad:" + str(self.edad)
        #Se uso el metodo str para poder imprimir los valores 

class Empleado(Persona):
    
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
     
     #Se sobre escribio el metodo str   
    def __str__(self):
        return super().__str__() + ", Sueldo:" + str(self.sueldo)
    
    
        
persona = Persona("Mikauran", 28)
print(persona)

empleado = Empleado("Esperanzita", 26, 500)
print(empleado)
    
#Se cambiaron los valores de la clase padre e hija
empleado.nombre = "Espe"
empleado.sueldo = 1000.00
print(empleado)        