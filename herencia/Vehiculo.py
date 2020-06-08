class Vehiculo:
    
    def __init__(self, color, modelo, ruedas):
        self.color = color
        self.modelo = modelo
        self.ruedas = ruedas
    
    def __str__(self):
        return "Color:" + self.color + ", Modelo:" + self.modelo + ", Ruedas:" + str(self.ruedas)
        

class Coche(Vehiculo):
    
    def __init__(self, color, modelo, ruedas, velocidad):
        super().__init__(color, modelo, ruedas)
        self.velocidad = velocidad
        
    def __str__(self):
        return super().__str__() + ", Velocidad:" + str(self.velocidad)
    
class Bicicleta(Vehiculo):
    
    def __init__(self, color, modelo, ruedas, tipo):
        super().__init__(color, modelo, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return super().__str__() + ", Tipo:" + str(self.tipo)
    

vehiculo = Vehiculo("Rojo", "SUV", 4)
print(vehiculo)

auto = Coche("Amarillo", "Sedan", 4, 100)
print(auto)

bici = Bicicleta("Verde", "Scott Spark", 2, "MTB")
print(bici)
        
    
        
    
        