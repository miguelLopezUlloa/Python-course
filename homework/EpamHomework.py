class EpamHomework:

    def __init__(self):
        print("Iniciando Tareas...")


    def odd_even_indexes(self,list1, list2):
        lst4 = []
        index = 0

        if len(list1) == len(list2):

            while index < len(list1):
                if (index % 2 != 0):
                    lst4.append(list1[index])

                index += 1

            index = 0
            while index < len(list2):
                if (index % 2 == 0):
                    lst4.append(list2[index])

                index += 1

        else:
            print("No se puede hacer la operacion con las listas, por que son de diferente tamaño..")

        print("La lista queda como:", lst4)

    def odd_even_indexes2(self, list1, list2):
        lst4 = []

        if len(list1) == len(list2):

            for index in range(len(list1)):
                if (index % 2) != 0:
                    lst4.append(list1[index])

            for index in range(len(list2)):
                if (index % 2) == 0:
                    lst4.append(list2[index])

        else:
            print("No se puede hacer la operacion con las listas, por que son de diferente tamaño..")

        print("La lista queda como:", lst4)


    def move_element(self, input_list, index1, index2):
        listIndex = len(input_list)

        if (index1 >= 0 and  index1 < listIndex) and (index2 >= 0 and  index2 < listIndex):
            val1 = input_list[index1]
            val2 = input_list[index2]

            #print("Hare el proceso")
            #print("En el indice 1 se encuentra el valor de:", input_list[index1])
            #print("En el indice 2 se encuentra el valor de:", input_list[index2])

            input_list[index2] = val1
            input_list[index1] = val2

            return input_list
        else:
            return input_list


    def count_elements(self,input_list):
        store = dict.fromkeys(input_list)
        #print(store)
        for llave in store:
            #print("La llave es:", llave)
            countKey = 0

            for index in range(len(input_list)):
                if input_list[index] == llave:
                    countKey += 1

            store[llave] = countKey

        print(store)

    def remove_intersection(self, set1, set2):

        finalSet = set1.difference(set2)

        print(f"La interseccion resultante es: {finalSet}")


    def delete_duplicates_to_tuple(self, input_list):

        tmpSet = set(input_list)
        finalTuple = tuple(tmpSet)
        print("Other Tuple is:", finalTuple)




lst1 = [1,3, 5,7]
lst2 = [8,2,7,4]

mixLists = EpamHomework()

#mixLists.odd_even_indexes(lst1,lst2)

#mixLists.odd_even_indexes2(lst1,lst2)

print("*" *60)

#print(dir(list))

"""
list3 = [1, 2, 3, 4, 5]
list4 = mixLists.move_element(list3, 2, 3)
print(list4)

print("*" *60)

food = ['spam', 'SPAM', 'spam', 'spam', 'bacon', 'SPAM']
mixLists.count_elements(food)

"""


print("*" *60)

mixLists.remove_intersection(set1={1, 2, 3, 4, 5}, set2={3, 4, 5, 6, 7})

print("*" *60)
mixLists.delete_duplicates_to_tuple(input_list=[2, 2, 3, 4, 5, 5, 5, 6, 7, 2])














