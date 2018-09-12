def flowShopPermutation(order, matrix):
    final = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    largest = 0;
    for i in range(len(order)):
        for j in range(len(matrix[0])):
            if i == 0:
                if j == 0:
                    final[order[i]][j] = matrix[order[i]][j];
                else:
                    final[order[i]][j] = final[order[i]][j-1] + matrix[order[i]][j];
            else:
                if j == 0:
                    final[order[i]][j] = final[order[i-1]][j] + matrix[order[i]][j];
                else:
                    final[order[i]][j] = max(final[order[i]][j-1],final[order[i-1]][j]) + matrix[order[i]][j];
                    #final[order[i]][j] = int(max(2, 3)) + matrix[order[i]][j];

            if final[order[i]][j] > largest:
                largest = final[order[i]][j];
    return largest;

def printMatrix(matrix):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in matrix]));
