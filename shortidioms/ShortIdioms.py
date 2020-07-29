class ShortIdioms:

    def __init__(self):
        print("Starting Short Idioms...")


    def shortList(self):
        upper_letters = []

        # Iteration
        for x in "hello there":
            # Append items to the list
            upper_letters.append(x.upper())

            # Printing the list
        print(upper_letters)

    def shortListV2(self):
        compress = [x.upper() for x in "hello there"]

        print(compress)

        return compress

    def shortCompressForms(self):
        # List comprehensions - positive even, negative odd
        my_list = [x if x % 2 == 0 else -x for x in range(20)]
        print("my_list:", my_list)

        # Set comprehensions - only numbers that end on 1
        my_set = {x for x in my_list if str(x)[-1] == "1"}
        print("my_set:", my_set)

        # Dict comprehensions - each letter with it's position
        my_dict = {i: char for i, char in enumerate("hello you!!!") if char != " "}
        print("my_dict:", my_dict)

        # Generator comprehensions - zipped pairs
        my_gen = ((x, y) for x, y in zip({'a', 'b', 'c'}, [1, 2, 2]))
        print('my_gen:', my_gen)
        print('my_gen_list:', list(my_gen))

    def multiplyTable(self):
       tblMulti =  [f"{i} x {j} = {i * j}" for i in range(1, 4) for j in range(10)]

       print(tblMulti)

    def swapNumbers(self):
        numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

        switched_numbers = {v: k for (k, v) in numbers.items()}

        print(switched_numbers)



short1 = ShortIdioms()

short1.shortList()
short1.shortListV2()
short1.shortCompressForms()
short1.multiplyTable()

short1.swapNumbers()

