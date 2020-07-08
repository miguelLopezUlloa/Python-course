from functools import reduce

def soluDos(number):
    cad1 = str(number)
    lstSum = list(cad1)
    print(cad1)
    suma = 0
    lstLen= len(lstSum)
    print("Long List:", lstLen)

    for index in range(lstLen-1):
        opr1 = int(lstSum[index])
        suma += opr1
        return suma

# Toma el numero y lo convierte en una lista
# tomando cada digito en una posicipon de la lista
def getListNumbers(number):
    cad1 = str(number)
    lstSum = list(cad1)
    lstItems = list(map(int, lstSum))

    return lstItems

def  calcSuma(lst_numbers):
    sumaInicio = reduce(lambda x, y: x + y, lst_numbers)
    return sumaInicio

def searchSum(number):
    lstInNumbers= getListNumbers(number)
    sumIni = calcSuma(lstInNumbers)
    sumEquals = False
    result = 0
    i=1

    while (not(sumEquals)):
        tmpListNumbers = getListNumbers(number + i)
        sumaNueva = calcSuma(tmpListNumbers)

        if(sumIni == sumaNueva):
            sumEquals= True
            result = number + i

        i+=1

    return result

def searchMissingNumber(lstNumbers):
    missing = 0

    if (lstNumbers[0] < 0):
        missing = 1
    else:
       # missing = list(filter(lambda x,y:x <= y, setSorted) )
       pattern = set(range(1, len(lstNumbers) + 1))
       setSorted = set(lstNumbers)
       #print(setSorted)
       setMissing = pattern.difference(setSorted)
       lstMissing = list(setMissing)
       size = len(lstMissing)

       if size >= 1:
          missing = lstMissing[size-1]
       else:
           missing = max(lstNumbers) + 1
           #missing = lstNumbers[len(lstNumbers)-1] + 1

    return missing

#solution(A=[1,3,6,4,1,2])
#soluDos(1990)

#print(soluTres(1990))
#print(soluTres(28))

print(searchSum(1990))

print(searchMissingNumber(lstNumbers=[1, 3, 6, 4, 1, 2]))
print(searchMissingNumber(lstNumbers=[1,2,3]))
print(searchMissingNumber(lstNumbers=[-1, -2, -3]))






