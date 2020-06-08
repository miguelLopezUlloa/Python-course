class Product:
    
    counter_products = 0
    
    def __init__(self, name, price):
        Product.counter_products += 1
        self.__id_product = "Prd_" + str(Product.counter_products)
        self.__name = name
        self.__price = price

    def getPrecio(self):
        return self.__price

    def __str__(self):
        return "Id Product=" + self.__id_product + ", Name=" + self.__name + ", Price=" + str(self.__price)
    
    