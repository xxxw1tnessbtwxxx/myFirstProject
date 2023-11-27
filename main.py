import random
import math
def makeArray(): # 1
    return [random.randint(0, 50)**2 for i in range (int(input()))]

a = makeArray()
print(a)

def findNonUnique(list1: list): # 2
    nonunique = []
    for i in list1:
        for j in list1:
            if j == i:
                nonunique.append(j)

    print(set(nonunique))

findNonUnique([2, 3, 3, 4, 5, 1])

def makeThirdArray(list1: list, list2: list): # 3
    third_array = []
    
    for i in list2:
        if i not in list1:
            third_array.append(i)

    print(list1, list2, third_array, sep="\n")
    return third_array


a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 6, 7]

array = makeThirdArray(a, b)
print(array)

def replaceTwenty(list1: list): # 4
    for i in range(len(list1)):
        if list1[i] == 20:
            list1[i] = 200

    return list1

mySecArray = replaceTwenty([1, 20, 20, 20, 20, 20])
print(mySecArray)

def printOdd(list1: list): # 5
    for i in list1:
        if i == 15:
            break
        elif i % 2 != 0:
            print(i)

printOdd([1, 2, 3, 4, 5, 7, 15, 8, 9])

def makeThirdArrayBadestInput(list1: list): # 6
    n = int(input("Введите ограничение: "))
    maked_array = []
    for i in list1:
        if i < n:
            maked_array.append(i)

    print(maked_array)

print("#3333")
makeThirdArrayBadestInput([num for num in range(0, 21)])

def findRanges(list1: list): # 7
    print(max(list1))
    print(min(list1))

findRanges([0, 5, 7, 8])



