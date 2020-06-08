class Order:
    
    orderCounter = 0
    
    def __init__(self, products):
        Order.orderCounter += 1

        self.__id_orden = "Ord_" + str(Order.orderCounter)
        self.__products = products

    def __str__(self):
        producto_str = ""
        for producto in self.__products:
            producto_str += producto.__str__() + " | "

        return "Orden=" + str(self.__id_orden) + ", Productos=" + producto_str

    def agregarProducto(self, product):
        return self.__products.append(product)

    def calcularTotal(self):
        total = 0

        for product in self.__products:
            total += product.getPrecio()

        return total





        