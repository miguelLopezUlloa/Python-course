
# First operators

a = 3
b = 2

result = a != b
print("Comparing two values and are different:",result)

# Decisitions 
if a % 2 == 0:
    print("Is Odd")
else:
    print("Is not Odd")

color = "White"

if color == "Red":
    print("The color is red")
elif color == "White":
    print("The color is White")
else:
    print("Any color")


price = 23.39


if price > 50:
    print("Is expensive")
else:
    print("Is to cheaper")

print("***********************************")

name = "Ryan"
lastName ="Reynolds"

if name == "John":
    if lastName == "Tiny":
        print("You are not Ryan Reynolds")
    else:
        print("You are not Ryan Reynolds")
else:
    print("You are not John")

print("***********************************")

#Using a Ternary Operator
print("You are John") if name else print("You are not Ryan Reynolds")

print("***********************************")

#Logic operator
xNum = 10

# The other <= , or , not
if xNum > 2 and xNum <= 20:
    print("The number is greater than 2 and less than 20 or minor")

y= 2
if(not(xNum == y)): 
 print("Not equals than other")

 






