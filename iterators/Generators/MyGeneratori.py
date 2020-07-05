
class MyGenerator:

    def __init__(self, num):
        self.num = num
        self.counter = -1

    # Called when next(MyGenerator(3)) is executed
    def __next__(self):
        self.counter += 1

        if self.counter < self.num:
            return self.counter
        else:
            raise StopIteration()

    # Used in `for x in MyGenerator(3)`
    def __iter__(self):
        return self

myGen = MyGenerator(3)

print(next(myGen))
print(next(myGen))
print(next(myGen))
#print(next(myGen))


