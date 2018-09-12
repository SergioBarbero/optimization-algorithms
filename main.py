import geneticAlgorithm
import localSearch
import randomSearch
import simulatedAnnealing
from readFromFile import readFromFile

########################################################################################################################
#                                                                                                                      #
#                                                 LOCAL SEARCH                                                         #
#                                                                                                                      #
########################################################################################################################
#Change values of these variables here below as you want


matrix = readFromFile("filesFlowShopPermutation/Doc1.txt");
order = randomSearch.generateRandomOrder(matrix);
localSearch.firstImprovement(matrix, order);

########################################################################################################################
#                                                                                                                      #
#                                                 RANDOM SEARCH                                                        #
#                                                                                                                      #
########################################################################################################################
#Change values of these variables here below as you want

myMatrix = readFromFile("filesFlowShopPermutation/Doc5.txt")
tries = 100;
randomSearch.randomSearch(myMatrix, tries);


########################################################################################################################
#                                                                                                                      #
#                                                 SIMULATED ANNEALING                                                  #
#                                                                                                                      #
########################################################################################################################
#Change values of these variables here below as you want

myMatrix =  readFromFile("filesFlowShopPermutation/Doc5.txt")
alpha = 0.9
L = 100
finalT = 0.001
bestAnnealing = simulatedAnnealing.simulatedAnnealing(alpha, L, finalT, myMatrix)
localSearch.firstImprovement(myMatrix, bestAnnealing)


########################################################################################################################
#                                                                                                                      #
#                                                 GENETICAL ALGORITHM                                                  #
#                                                                                                                      #
########################################################################################################################
#Change values of these variables here below as you want


myMatrix =  readFromFile("filesFlowShopPermutation/Doc5.txt")  #Problem to solve - Important: READ NOTE
n = 50 #Size of my population
nGen = 20 #Number of generations of my algorithm
k = 30 #Size of the tournament
p = 0.2 #Probability of mutation [0,1]

solution = geneticAlgorithm.run(myMatrix, n, nGen, k, p) #Runs such a genetic algorithm
localSearch.firstImprovement(myMatrix, solution) #Runs local search from the best solution found in order to find our local optimum

#Note: If you're in Windows not Linux, then paths are written in this way "filesFlowShopPermutation\Doc5.txt"
