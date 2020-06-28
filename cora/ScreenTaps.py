from math import sqrt
import math

class ScreeTaps:
    BASE_NAME = "icon"
    RADIUS = 20

    def __init__(self):
        print("Starting Screen Tap game...")

    def screenTapGame1(self, A, B, X, Y):
        keyTap = (X, Y)
        matchPoint= 0
        founded = False
        lstInRange = []

        if(len(A) == len(B)):
            game = dict(self.createGameTable(A,B))
            index = 0

            print(game)
            for positions in game:
                tmpPosition = tuple(game[positions])

                founded= self.isInRange(keyTap, tmpPosition)
                lstInRange.append(founded)

                if(founded):
                    print("Lo encontre:" + str(tmpPosition))
                    matchPoint = index
                    break
                elif index < len(A):
                    index += 1
                else:
                    matchPoint = -1
                    print("Todos los puntos estan fuera del rango...", lstInRange)
                    break

            print(matchPoint)

    def createGameTable(self, A, B):
        countKey = 0
        game = {}

        for index in range(len(A)):
            a = A[countKey]
            b = B[countKey]
            iconTap = (a, b)
            game[self.BASE_NAME + str(countKey)] = iconTap
            countKey += 1

        return game

    def isInRange(self, keyTap , position):
        i = 0
        print(keyTap)
        print(position)

        #for i in position:
        #    print("-->",i)

        for index in range(len(position)):
            print("-->",position[index])
            print("++", keyTap[index])
            calc1 = keyTap[index] - position[index]
            calc2 = keyTap[index+1] - position[index+1]
            print("Calc1:", calc1)
            print("Calc2:", calc1)
            d = sqrt((calc1 ** 2) + (calc2 ** 2))
            #d = (calc1 ** 2) + (calc2 ** 2)
            #d2 = d**2
            #r2 = self.RADIUS ** 2
            r2 = self.RADIUS

            print("Distancia:", d)
            # inside the circle if d<r, on the circle if d=r, and outside the circle if d>r
            #if (d < self.RADIUS) or (d == self.RADIUS):
            if (d < r2) or (d == r2):
                return True
            else:
                return False


games = ScreeTaps()

A = [100, 200, 100]
B = [50, 100, 100]

#X = 100
#Y = 70
#X = 100
#Y = 100
X = 200
Y = 60

games.screenTapGame1(A,B,X,Y)



