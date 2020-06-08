from herenciamulti import FiguraGeometrica
from herenciamulti import Color

class Cuadrado(FiguraGeometrica, Color):
    
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        #super.__init__(lado, lado)

        Color.__init__(self, color)
        
    def area(self):
        figGeo = self.
        
    
     
        
        