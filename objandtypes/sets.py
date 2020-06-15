#Conjuntos 
# Se usa cuando se necesita un conjunto de datos sin q se necesite una posicion
# NO SE PUEDE MODIFICAR EL VALOR DE UN ELEMENTO DEL SET.  
# NO TIENE ORDEN.  
# NO ACEPTA REPETIDOS
# SE PUEDEN AGREGAR NUEVOS ELEMENTOS O BORRAR ALGUNO DE LOS ELEMENTOS PERO LOS VALORES NO


colors = {'Yellow','Black','White'}

print(colors)
print(type(colors))

#Verifica si existe el colo Red en el set Colors
print('Red' in colors)

#Agrega un elemento al set al inicio del mismo, por que no maneja un indice.
colors.add('Purple')
print(colors)

#Elimina un elemento, pero posiblemente arroja excepción, si no encuentra el elemento
colors.remove('Black')
print(colors)

# Tambien remueve un elemento, pero no arroja excepción, en caso de no encontrar el elemento
colors.discard("White")
print("Set con elementos:", colors)

print("*" *60)
# Limpia el set y lo deja vacio
colors.clear()
print(colors)

# del colors  --> Elimina el set colors
print("*" *60)

x = set(['foo', 'bar', 'baz', 'foo'])
print(x)

x = set(('foo', 'bar', 'baz', 'foo'))
print(x)

# Strings are also iterables
x = set('foo')
print(x)

print("*" *60)
print(" Other examples with Sets")

x = {'foo'}
print(x)

x = set('foo')
print(x)

# Es una tupla lo que pasa al método
x = set(('foo',))
print(x)
print("*" *60)

s3 = {
    42,
    'Ni!',
    3.14159,
    True,
    None,
    (
        'Eggs',
        'Bacon',
        'Spam'
    )
}

print(s3)









