#! /usr/bin/env python3
from tableMaker import makeXtable, makeYtable

def interpolation (data, core):
    """
    Notes:
        This function takes the data set and a core number and returns a piecewise 
        Linear Interpolation approximation for each step in the data set.
        This function is based on using Newton's form

    Args:
        data: a list with each element containing a time and a list of the core tempatures at that time
        core: 0-indexed core number

    Yields:
        a list of dict objects {'xFrom': , 'xTo': , 'yi': ,'c0': , 'c1': , 'type': }
    
    """
    x = makeXtable(data)
    y = makeYtable(data, core)
    solution = []

    i = 1
    while i < len(x):
        if y[i] == y[i-1]:#will cause c1 to be exactly 0
            c1 = 0
            c0 = y[i-1]
        elif (y[i]-y[i-1]) == (x[i]-x[i-1]):#will cause c1 to be exactly 1
            c1 = 1
            c0 = y[i-1] - x[i-1]
        else:
            c1 = (y[i]-y[i-1])/(x[i]-x[i-1])
            c0 = y[i-1] - c1 * x[i-1]
        
        temp = {
                'xFrom': x[i-1], 
                'xTo': x[i], 
                'yi': i-1,
                'c0': c0, 
                'c1': c1, 
                'type': "interpolation"
                }
        
        solution.append(temp)
        i += 1

    return solution



    # for temp in data:
    #     x_table.append(temp[0])
    #     y_table.append(temp[1])
        # temp[0]       is steptime 0,30,60... x
        # temp[1]       is all for core temps
        # temp[1][0]    is first core temp     y