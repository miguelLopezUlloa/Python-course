# Program to show the use of lambda functions
double = lambda x: x * 2

print(double(5))

print("*" *60)


# filter out only the even items from a list
# items for which the function evaluates to True.
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print("The new list is:",new_list)
print("*" *60)

# function to makes double all the items in a list.
# which contains items returned by that function for each item.
double_list = list(map(lambda x: x * 2 , my_list))
print("The double list is:", double_list)
