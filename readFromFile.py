from FlowShopPermutation import printMatrix
import re

def readFromFile(name):
    file = open(name, "r");
    content = file.readlines()
    content = [x for x in content];
    content.pop(0);
    matrix = []
    tmp = ""
    for i in range(len(content)):
        content[i] = re.sub(' +',' ', content[i])
        matrix.append([]);
        count = 0;
        for j in content[i]:
            if j == ' ' or j == '\n' or j == '\r':
                if (count % 2 == 0 and tmp != ""):
                    newValue = int(tmp);
                    matrix[i].append(newValue);
                count = count + 1;
                tmp = ""
            else:
                tmp = tmp + j;
    return matrix;


