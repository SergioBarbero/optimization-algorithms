from random import randint
from FlowShopPermutation import flowShopPermutation
from readFromFile import readFromFile

def randomSearch(matrix, tries):
    print("________Random search________")
    bestSecuence = generateRandomOrder(matrix)
    best = flowShopPermutation(bestSecuence, matrix)
    print("Initial state")
    print(str(bestSecuence) + " | " + str(best));
    for i in range(tries):
        secuence = generateRandomOrder(matrix)
        current = flowShopPermutation(secuence, matrix);
        if(best > current):
            best = current;
            bestSecuence = secuence;
    print("Best")
    print(str(bestSecuence) + " | " + str(best));
    return bestSecuence;

def generateRandomOrder(matrix):
    secuence = [-1 for i in range(len(matrix))];
    for j in range(len(secuence)):
        newValue = randint(0, len(matrix) - 1);
        while (newValue in secuence):
            newValue = randint(0, len(matrix) - 1);
        secuence[j] = newValue;
    return secuence

