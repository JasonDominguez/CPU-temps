#! /usr/bin/env python3

def makeXtable(data):
    xTable = []
    for temp in data:
        xTable.append(temp[0])
    return xTable

def makeYtable(data, core):
    y = []
    for temp in data:
        y.append(temp[1][core])
    return y

def makeXmatrix(data):
    xMatrix = []
    for temp in data:
        xMatrix.append([1, temp[0]])
    return xMatrix

def makeYmatrix(data, core):
    y = []
    for temp in data:
        y.append([temp[1][core]])
    return y

def transpose(matrix):
    tMatrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return tMatrix
    
def multiply(m1, m2):
    result = [[0 for x in range(len(m2[0]))] for y in range(len(m1))]
    for i in range(len(m1)): 
        for j in range(len(m2[0])): 
            for k in range(len(m2)): 
                result[i][j] += m1[i][k] * m2[k][j] 
    
    return result

    
    
     
