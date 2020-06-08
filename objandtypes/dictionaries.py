# Diccionarios - Dictionaries

product = {
    "nameProduct": "book",
    "quantity": 3,
    "price": 10.99
}

person = {
    "name": "Bob",
    "last_name": "Marley"
}

#Imprime las llaves 
print(product.keys())
#Imprime los elementos que tienen
print(product.items())

print("El valor de name es:", person.get("name"))

# Borra el objeto person
#del person

# Limpia el diccionario. Quita sus elementos
person.clear()
print(person)

person["Direccion"] = "Desconocida"
person["Otros"] = "Extraterrestre"
print("Person esta con:", person.keys())

person.pop("Direccion")
print("Se quedo con:", person.keys())

print("*****************************************************")
# Una lista con dos diccionarios en su interior
newProducts = [
    { "prodName" : "Mouse", "price": 10.99},
    {"productName": "Laptop", "price": 899.99}
]

print("La longitud del diccionario es:", len(newProducts))
print(newProducts)

for llaves in product:
    print("Las llaves son:", llaves)
    
for termino in product:
    print("The values is", product[termino])
    
    
print("Mouse" in product)


print("*" *60)




