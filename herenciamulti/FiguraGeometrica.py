class FiguraGeometrica:
    
    def __init__(self, ancho, alto):
        self.__ancho = ancho
        self.__alto = alto
        
    def __str__(self):
        return "Color:" + self.getAncho(self.__ancho) + ", Ancho:" + self.getAlto(self.__alto)
    
    def getAncho(self, ancho):
        return self.__ancho
    
    def setAncho(self, ancho):
        self.__ancho = ancho
        
    def getAlto(self, alto):
        return self.__alto
    
    def setAlto(self, alto):
        self.__alto = alto
