class EpamHomework:

    def __init__(self):
        print("Starting Python Epam Course - Homework...")

    def odd_even_indexes4(self,list1, list2):
        list1[1::2], list2[0::2]
        lst5 = list1[1::2] + list2[0::2]
        print(lst5)

    def move_element(self, input_list, index1, index2):
        try:
            input_list[index1], input_list[index2] = input_list[index2], input_list[index1]
            return input_list
        except:
            return input_list

mixLists = EpamHomework()

lst1 = [1,3, 5,7]
lst2 = [8,2,7,4]

print("*" *60)
mixLists.odd_even_indexes4(lst1,lst2)

print("*" *60)

list3 = [1, 2, 3, 4, 5]

list4 = mixLists.move_element(list3, 2, 3)
print(list4)