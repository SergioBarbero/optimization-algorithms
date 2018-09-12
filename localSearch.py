from readFromFile import readFromFile
from FlowShopPermutation import flowShopPermutation
from randomSearch import generateRandomOrder

def firstImprovement(matrix, order):
    print("_________Local search_________")
    best = flowShopPermutation(order, matrix);
    bestOrder = order;
    print("Initial state")
    print(str(bestOrder) + " | " + str(best));
    for i in range(0, len(order)-1):
        for j in range(i+1, len(order)):
            neighbour = list(order);
            x = order[i];
            y = order[j];
            neighbour[i] = y;
            neighbour[j] = x

            current = flowShopPermutation(neighbour, matrix);
            if current < best:
                best = current;
                bestOrder = neighbour;

            #print(neighbour);
            #print(current)
    print("Best")
    print(str(bestOrder) + " | " + str(best));
    return [bestOrder, best]
