class EpamModule61:

    def __init__(self):
        print("Starting")

    def createListCompress(self):
        squared_list = [x ** 2 for x in range(10) if x % 2 == 0]

        return squared_list

    def createDictCompress(self):
        sequence = range(10)
        squared_dict = {x: x ** 2 for x in range(10) if x % 2 == 1}

        return squared_dict

    def createSetCompress(self):
        #strList = "JWxdVL8hE8VRmU8vCUX8Y32tFmgn7hfm"
        #number_set = { int(chr) for chr in strList if chr.isdigit() }
        number_set = {int(chr) for chr in "JWxdVL8hE8VRmU8vCUX8Y32tFmgn7hfm" if chr.isdigit()}

        return number_set

    def swapNumbers(self):
        numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

        switched_numbers = {v: k for (k, v) in numbers.items()}

        return switched_numbers


    def my_generator(self, num):
        if num < 0:
            rngFin = abs(num)
        else:
            rngFin = num

        #Range from num to totRange
        totRange = (rngFin + rngFin)+ 1

        for i in range(rngFin, totRange):
            if num % 2 == 0:
                yield num
                num += 2
            else:
                yield num
                num += 1



# Start the call functions
exercise = EpamModule61()
print(exercise.createListCompress())

print("*" *60)
print(exercise.createDictCompress())

print("*" *60)
print(exercise.createSetCompress())

print("*" *60)
print(exercise.swapNumbers())

print("*" *60)
# Print only even numbers
my_gen = exercise.my_generator(10)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))

print("*" *60)
# Print next biggest even number
for i in exercise.my_generator(-3):
    print(i)
