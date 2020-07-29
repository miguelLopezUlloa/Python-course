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

    def my_generator(self, num):

        for i in range(num,(num+num)+1):
            if num % 2 == 0:
                #print(i)
                num += 2
                yield num
            #else:
                #yield i



exercise = EpamModule61()
print(exercise.createListCompress())

print("*" *60)
print(exercise.createDictCompress())

print("*" *60)
print(exercise.createSetCompress())

print("*" *60)
my_gen = exercise.my_generator(10)

print(next(my_gen))
print(next(my_gen))