from stores.Product import Product
from stores.Order import Order

producto1 = Product("Camisa", 100.99)
producto2 = Product("Pantalon", 200.89)
producto3 = Product("Calcetines", 50.00)

productos = [producto1,producto2]

orden1 = Order(productos)
print("La orden a enviar contiene:", orden1)
print("El total a pagar de la orden 1 es:", orden1.calcularTotal())
print("*" *65)

#productos.append(producto3)

orden2 = Order(productos)
orden2.agregarProducto(producto3)
print(orden2)
print("*" *65)
print("El total a pagar de la orde 2 es:", orden2.calcularTotal())