import math
import random as rand

from randomSearch import generateRandomOrder
from random import randint, random, uniform
from readFromFile import readFromFile
from localSearch import firstImprovement

from FlowShopPermutation import flowShopPermutation, printMatrix


def simulatedAnnealing(alpha, L, finalT, matrix):
    print("______Simulated Annealing______")
    currentA = generateRandomOrder(matrix)
    costSact = flowShopPermutation(currentA, matrix)
    print("Initial state")
    print(str(currentA) + " | " + str(costSact));
    print()
    T = flowShopPermutation(currentA, matrix) * 0.4
    while (T >= finalT):
        for i in range(L):
            #Getting our random neighbour
            neighbour = list(currentA)
            x = randint(0, len(currentA)-1)
            y = randint(0, len(currentA)-1)
            while x == y:
                y = randint(0, len(currentA)-1)
            neighbour[x] = currentA[y]
            neighbour[y] = currentA[x]
            #Getting costs
            costScand = flowShopPermutation(neighbour, matrix)
            costSact = flowShopPermutation(currentA, matrix)
            #difference
            delta = costScand - costSact
            r = rand.random()
            if r < pow(math.e, -delta/T) or delta < 0:
                currentA = neighbour
                #print(str(currentA) + " | " + str(costSact));
        T = alpha * T

    print("Final state")
    print(str(currentA) + " | " + str(costSact));
    return currentA













