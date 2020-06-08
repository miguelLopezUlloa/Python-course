
foods = ["Cake","Spaguetty","Tortas","Tamales"]

for food in foods:
    if food == "Tortas":
        print("Yuumi, yummi, rica Torta")
        break
        #existe continue por si quieres que siga la impresion de la lista
    print(food)
print("**********************************************************")
for number in range(1,9):
    print(number)
    
print("**********************************************************")

# continue salta a la siguiente iteraction en el ciclo
for index in range(6):
    if(index % 2) != 0:
        continue
    print("Number is not odd:", index)
    

print("**********************************************************")
for letter in "Hello":
    print(letter)

print("**********************************************************")



