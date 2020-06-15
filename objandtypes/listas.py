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

# Extend y una lista, los agrega como elementos en la lista original
colors.extend(["Gray","Purple"])
print(f"Extendiendo la lista en elementos {colors}")

# Inserta en el indice seleccionado
colors.insert(4,"Aqua")
print(colors)

#Borra el color Aqua
colors.remove("Aqua")
print(colors)

print("*" *60)
colors.pop()
print("Removing the last position in the list")


if("Purple") in colors:
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
        
print("*" *60)

lst1 = [1,3, 5, 7]
lst2 = [8,2,7,4]

for element in lst1 + lst2:
    if (element % 2 == 0):
        print("Is Odd", element)
    else:
        print("Is not Odd", element)

print("*" *60)
new_list = list(filter(lambda x: (x%2 == 0) , lst1 + lst2))

print(new_list)

print("*" *60)
index=0
lst3 = list(lst1 + lst2)
print("Longitud lista es:", len(lst3) )
print(lst3)
lst4 = []

if len(lst1) == len(lst2):

    while index < len(lst1):
        if(index % 2 != 0):
            lst4.append(lst1[index])

        index +=1
    #else:
        #print("Nueva lista:", lst4)

    index = 0
    while index < len(lst2):
        if(index % 2 == 0):
            lst4.append(lst2[index])

        index +=1
    #else:
        #print("Nueva lista:", lst4)

else:
    print("No se puede hacer la operacion con las listas, por que son de diferente tamaño..")

print("Lista final queda:", lst4)

"""
while index < len(lst3):
    isPar=  index % 2 == 0

    if isPar :
        print(isPar)
        print("Posicion del indice es:",index)
        lst4.append(lst3[index])
        print(lst4)
    else:
        print("No voy hacer nada, por que el indice es impar")

    index += 1
else:
    print("Nueva lista:",lst4)
"""








        
        



