class Volumns:
    
    #El penulitmo parametro *v, significa que espera una tupla
    # y es opcional
    ''' Un diccionario al final tambien es opcional y se
    usan ** '''
    def __init__(self, base, large, hight, *v, **dicc):
        self.base = base
        self.large = large
        self.hight = hight
        self.tplValues= v
        self.dicc = dicc
    
    def calculateVolumn(self):
        return self.base * self.large * self.hight
    
    
    def showValuesBox(self):
        print("The Box elements are the next")
        print("Base=", self.base)
        print("Large=", self.large)
        print("Hight=", self.hight)
        print("Coordenates=[", self.tplValues)
        
    def showOperations(self):
        print("Other operations", self.dicc)
        
vol1 = Volumns(10,20, 20)
print(str(vol1.calculateVolumn()))
vol1.showValuesBox()
vol1.showOperations()
print("**********************************")

vol2 = Volumns(30,40,5, 8,6,10, a='Area', r='Radio', o='Others')
print(str(vol2.calculateVolumn()))
vol2.showOperations()

        
