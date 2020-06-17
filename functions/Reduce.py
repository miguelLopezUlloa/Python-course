from functools import reduce

def sumaClassic(valores):

    suma = 0

    for val in valores:
        suma += val

    print(suma)

def sumaLambda(valores):
    return print(reduce(lambda x, y: x + y , valores))

valores = [2, 4, 6, 5, 4]
sumaClassic(valores)
print("*" *60)
sumaLambda(valores)
