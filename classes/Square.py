from classes.GeoAbstract import area

class Square(GeoAbstract):
    
    def __init__(self, ancho, alto):
        GeoAbstract.__init__(self, ancho, ancho)
        
    def area(self):
        return self.alto * self.ancho
        

square = Square(4, 6)
print("El area es:", square.area())
        
        
            
    
    