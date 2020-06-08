class Aritmetic:

    def __init__(self, oper1, oper2):
        self.oper1= oper1
        self.oper2= oper2
        
    """ Add method to add two values """ 
    def add(self):
        return self.oper1 + self.oper2
    

    def rest(self):
        return self.oper1 - self.oper2
    
    def multiply(self):
        return self.oper1 * self.oper2
    
    def division(self):
        return self.oper1 / self.oper2
    
    def module(self):
        return self.oper1 % self.oper2
    
    def exponentes(self):
        return self.oper1 ** self.oper2 


    #Object instace
aritmetic = Aritmetic(4,6)
print("The add result is:", aritmetic.add())

aritmetic = Aritmetic(100,40)
print("The rest result is: ", aritmetic.rest())

aritmetic = Aritmetic(200, 200)
print("The multiply result is:", aritmetic.multiply())

aritmetic = Aritmetic(400, 150)
print("The  / is:", aritmetic.division())

aritmetic = Aritmetic(3, 2)
print("The module result is:", aritmetic.module())

aritmetic2 = Aritmetic(4,4)
print("The exponent x(y) value is:", aritmetic2.exponentes())     
    
        