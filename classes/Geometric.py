class Geometric:
    
    def __init__(self, base, hightR):
        self.base = base
        self.hightR = hightR
        
    
    def area(self):
        return self.base * self.hightR
    
    
# Ask for values to the user
base = int(input("Introduce the base:"))
hightR= int(input("Introduce the Hight:"))
recta = Geometric(base,hightR)

print("The area for Rectangule is:", recta.area())
        
