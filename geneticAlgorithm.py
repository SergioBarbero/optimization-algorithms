from random import randint
from FlowShopPermutation import flowShopPermutation
from localSearch import firstImprovement
from randomSearch import generateRandomOrder
import random
from readFromFile import readFromFile

#Prints a population
def printPopulation(population, matrix):
    for i in population:
        printSolution(i, getFitness(i, matrix))
    print()

#Prints a concrete solution
def printSolution(solution, fitness):
    print(str(solution) + ' | ' + str(fitness))

#Runs genetic algoritm
def run(matrix, n, ngen, k, p):
    print("________Genetic algorithm________")
    #We get out first generation
    population = randomPopulation(matrix, n)
    for i in range(ngen):
        print("Generation number " + str(i))
        printPopulation(population, matrix)
        # Selection
        population = selection(k, population, matrix)
        printPopulation(population, matrix)
        # Crossover
        population = crossPopulation(population)
        printPopulation(population, matrix)
        #Mutation
        population = mutationPopulation(population, matrix, p)
        printPopulation(population, matrix)

    [solution, fitness] = getBest(population, matrix)
    print("     Best solution: ")
    printSolution(solution, fitness)
    return solution

#Get the best solution from a population
def getBest(population, matrix):
    best = 100000000000
    solution = []
    for i in population:
        current = getFitness(i, matrix)
        if current < best:
            best = current
            solution = i
    return [solution, best]

#Initialize a random first population with n elements
def randomPopulation(matrix, n):
    population = []
    for i in range(n):
        population.append(generateRandomOrder(matrix))
    return population

#Executes mutation operation to a whole population (doesn't mean it's going to mutate imperative)
def mutationPopulation(population, matrix, p):
    print("     Mutation")
    for i in range(len(population)):
        population[i] = mutation(population[i], matrix, p)
    return population


#Random mutation in one point with a p probability
def mutation(solution, matrix, p):
    r = random.random()
    if r < p:
        i = randint(0, len(solution)-1)
        solution[i] = (solution[i] + 1) % len(matrix)
    return solution


#Tournament selection, best element of k random elements from our population are passed to the next generation
def selection(k, population, matrix):
    print("     Selection")
    sumFit = 0
    fitnesses = [0 for i in range(k)]
    nextGen = []
    competitor = [[0 for i in range(len(population[0]))] for j in range(k)]
    for i in range(len(population)):
        for j in range(0, k):
            index = randint(0, len(population)-1)
            competitor[j] = population[index]
            fitnesses[j] = getFitness(competitor[j], matrix)
        #getting index of the best competitor
        best = 100000000
        for j in range(len(competitor)):
            if best > fitnesses[j]:
                indBest = j
                best = fitnesses[j]
        nextGen.append(competitor[indBest])
    return nextGen

#Creating couples and crossing among them in a random point
def crossPopulation(population):

    parent1 = []
    parent2 = []
    point = randint(1, len(population[0]) - 1)
    print("     Crossover: index = " + str(point))
    for i in range(0, len(population)-1, 2):
        j = i
        j = j+1
        [parent1, parent2] = crossover(population[i], population[j], point)
        population[i] = parent1
        population[j] = parent2
    return population


#Crossover in one point given
def crossover(solution1, solution2, point):
    #Random point shouldn't be 0 or len(solution) - 1
    part11 = [solution1[i] for i in range(point)]
    part12 = [solution1[i] for i in range(point, len(solution1))]
    part21 = [solution2[i] for i in range(point)]
    part22 = [solution2[i] for i in range(point, len(solution1))]

    child1 = part11 + part22
    child2 = part21 + part12

    return [child1, child2]


def getFitness(solution, matrix):
    return flowShopPermutation(solution, matrix)



