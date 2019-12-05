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


    


    
    
     
