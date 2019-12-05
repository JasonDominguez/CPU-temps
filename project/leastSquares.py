#! /usr/bin/env python3
from tableMaker import makeXmatrix, makeYmatrix, transpose, multiply

def leastSquares(data):
    x = makeXmatrix(data)
    y = makeYmatrix(data, 0) # add loop for cores
    xT = transpose(x)
    xTx = multiply(xT, x)
    xTy = multiply(xT, y)

    
    xtx_xty = []
    for i in range(len(xTx)):
            xtx_xty.append([xTx[i] + xTy[i]])
    
    print(f"xTy is a {len(xtx_xty)} by {len(xtx_xty[0])}")
    
