listDemo = [1,"xx", 3.14151678, True]
colors = ["Black", "White", "Blue", "Pink"]

print("Solo un rango en la lista:", colors[0:2])

print("Testing other range:", colors[:3])

print("*" *50)

#Esta usando una tupla para crear una lista
numbersList = list((1,2,4,5,9))
print(type(listDemo))

r = list(range(1,100))

print(r)

print("*" *70)

print("Longitud de la lista:", len(listDemo))

print("*" *60)

#Recorrido inverso de una lista
print(colors[-2])
print(colors)

colors[3] = "Cyan"
print(colors)

# Agrega al final de la lista
colors.append("Orange")
print(colors)

# Extend y una lista, los agrega como elementos separados
colors.extend(["Gray","Purple"])
print(colors)

# Inserta en el indice seleccionado
colors.insert(4,"Aqua")
print(colors)

#Borra el color Aqua
colors.remove("Aqua")
print(colors)

print("*" *60)
colors.pop()
print("Removing the last position in the list")


if("Purple ") in colors:
    print("Purple exist inside the list")
else:
    print("The color is not present inside the list")
    
print("+" *60)

#Ordena la lista de manera descendente
colors.sort(reverse=True)
print(colors)

# Imprime la posicion del color que se le pase
print(colors.index("Black"))

print(colors.count("Grey"))

del colors[1]
print("List:", colors)

#Borra el contenido de la lista
colors.clear
print(colors)

# Borra una lisa y tambien la variable que la alberga
#del colors 

print("*" *60)

# Imprimir el contenido de una lista usando un for
#listNumbers = [1,2,3,4,5,6,7,8,9,10]
for numer in range(10):
    if(numer % 3) == 0:
        print("Los número divisibles / 3 son:", numer)
        
        



