#! /usr/bin/env python3
from tableMaker import makeXmatrix, makeYmatrix

def leastSquares(data, core):
        step = data[1][0]-data[0][0]
        x = makeXmatrix(data)
        y = makeYmatrix(data, core)
        xT = transpose(x)
        xTx = multiply(xT, x)
        xTy = multiply(xT, y)
        xtx_xty = []
        for i in range(len(xTx)):
                xtx_xty.append(xTx[i] + xTy[i])
        solved = gaussianElimination(xtx_xty)
        temp = {
                'xFrom': data[0][0], 
                'xTo': (len(data)-1)*step, 
                'yi': "",
                'c0': solved[0], 
                'c1': solved[1], 
                'type': "least-squares"
                }
        return temp

def gaussianElimination(m):
        n = len(m)
        # Search for maximum in this column
        for i in range(0, n):
                maxEl = abs(m[i][i])
                maxRow = i
                for k in range(i+1, n):
                        if abs(m[k][i]) > maxEl:
                                maxEl = abs(m[k][i])
                                maxRow = k

                # Swap maximum row with current row (column by column)
                for k in range(i, n+1):
                        tmp = m[maxRow][k]
                        m[maxRow][k] = m[i][k]
                        m[i][k] = tmp

                # Make all rows below this one 0 in current column
                for k in range(i+1, n):
                        c = -m[k][i]/m[i][i]
                        for j in range(i, n+1):
                                if i == j:
                                        m[k][j] = 0
                                else:
                                        m[k][j] += c * m[i][j]

        # Solve equation Ax=b for an upper triangular matrix A
        x = [0 for i in range(n)]
        for i in range(n-1, -1, -1):
                x[i] = m[i][n]/m[i][i]
                for k in range(i-1, -1, -1):
                        m[k][n] -= m[k][i] * x[i]
        return x 

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