class Product:
    
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        
    def get_name(self):
        return self.__name;
    
    def set_name(self, name):
        self._name = name;
        
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        self.__price = price


prod1 = Product("Book", 45)
print("Name =",prod1.get_name())
print("Price = ", prod1.get_price())
print("**************************************")

prod2 = Product("Table", 29.99)
#prod2.set_price(250)
print("Name =",prod2.get_name())
print("Price = ",prod2.get_price())

print("**************************************")
prod2.set_name("Chair")
print("The new names=", prod2.get_name())
print("The new Price = ", prod2.get_price())

    
        