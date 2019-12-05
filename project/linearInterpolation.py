#! /usr/bin/env python3
from tableMaker import makeXtable, makeYtable

def interpolation (data):
    x = makeXtable(data)
    y = makeYtable(data, 0) #add loop for all cores
    solution = []

    i = 1
    while i < len(x):
        xFrom = x[i-1]
        xTo = x[i]
        yi = i-1
        c1 = (y[i]-y[i-1])/(x[i]-x[i-1])
        x0 = x[i-1]
        c0 = y[i-1] - c1 * x0

        c1 = '{:.2e}'.format(c1)
        c0 = '{:.2f}'.format(c0)
        temp = {'xFrom': xFrom, 'xTo': xTo, 'yi':yi, 'c1': c1, 'x0': x0, 'c0': c0}
        
        solution.append(temp)
        i += 1

    return solution



    # for temp in data:
    #     x_table.append(temp[0])
    #     y_table.append(temp[1])
        # temp[0]       is steptime 0,30,60... x
        # temp[1]       is all for core temps
        # temp[1][0]    is first core temp     y