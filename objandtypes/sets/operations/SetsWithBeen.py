class SetsWithBeen:

    x1 = {'foo', 'bar', 'baz'}
    x2 = {'baz', 'qux', 'quux'}

    def __init__(self):
        print ("Starting Instance Basic operations....")


    @staticmethod
    def unionExample():
        print(SetsWithBeen.x1 | SetsWithBeen.x2)
        print(SetsWithBeen.x1.union(SetsWithBeen.x2))
        print(SetsWithBeen.x2.union(SetsWithBeen.x1))

        print(SetsWithBeen.x1.union(('baz', 'qux', 'quux')))

        SetsWithBeen.x1 | {'baz', 'qux', 'quux'}

    def unionTwoExample(self):
        a = {1, 2, 3, 4, 5}
        b = {2, 3, 4, 5, 6}
        c = {3, 4, 5, 6, 7}
        d = {4, 5, 6, 7, 8}

        print(a.union(b, c, d))
        print(a | b | c | d)


    def intersections(self):
        a1 = {1, 2, 3, 4, 5}
        b = {2, 3, 4, 5, 6}
        c = {3, 4, 5, 6, 7}
        d = {4, 5, 6, 7, 8}

        print(a1.intersection(b, c, d))
        print(a1 & b & c & d)

    def baconAndHam(self):
        food1 = { "Eggs", "Bacon", "Spam", "Sausage"}
        food2 = { "Spam"}

        print(food1.difference(food2))
        print(food1 - food2)

        print("Is a subset:",food2.issubset(food1))



SetsWithBeen.unionExample()

print("*" *60)

unionD = SetsWithBeen()
unionD.unionTwoExample()

print("*" *60)
unionD.intersections()

print("*" *60)
unionD.baconAndHam()