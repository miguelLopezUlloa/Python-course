
#No cambian, son inmutables
# Son mas rapidas, seguridad de codigo

topol = (5,9,12,90,100)

print(topol)

print(type(topol))

meses = ("January", "February", "March")
print(meses)

print("La longitud de la tuplae es:", len(meses))

print("El elemento 2 de la tupla es:", meses[1])

# Se crea la tupla usando un constructor
letople= tuple((3.141516, 9.999, 777.777))
print(letople)

print(type(letople))

#Imprime los metodos de una tupla
#print(dir(letople))

# Tener una tupla de un solo valor (esta manera es incorrecta)
#tpl = (1)

#print(tpl)
#print(type(tpl))

#Lo correcto si se necesita una tupla de un solo valor es:
tpl= (1,)

print(type(tpl))
print(tpl)

#Con diccionarios
locations = {
    (25.83, 837.93): "China",
    (134.99, 256.98): "Rusia"
}

print(locations)

#Convirtiendo una Tupla a una lista

mesesExpand = list(meses)
mesesExpand.append("April ")
meses = tuple(mesesExpand)
print("Other Tuple is:", meses)

for month in meses:
    #print("Salida arreglada es:", meses, end="-")
    print("Salida arreglada es:", meses)
    
    # del meses  --> Borra la variable y la tupa 
    
    
jumpTupla = (13, 1, 8, 3, 2, 5, 8)
lstNewNumbers = []

for value in jumpTupla:
    if(value < 5):
        lstNewNumbers.append(value)
        
print("The list values:", lstNewNumbers)
    



