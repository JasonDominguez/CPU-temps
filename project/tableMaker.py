#! /usr/bin/env python3

def makeXtable(data):
    """
    Notes:
        This function takes the data set and returns a list of times

    Args:
        data: a list with each element containing a time and a list of the core tempatures at that time

    Yields:
        a list of times
    
    """
    xTable = []
    for temp in data:
        xTable.append(temp[0])
    return xTable


def makeYtable(data, core):
    """
    Notes:
        This function takes the data set and a core number and returns a list of tempetures for the given core

    Args:
        data: a list with each element containing a time and a list of the core tempatures at that time
        core: 0-indexed core number

    Yields:
        a list of tempetures
    
    """
    y = []
    for temp in data:
        y.append(temp[1][core])
    return y


def makeXmatrix(data):
    """
    Notes:
        This functions takes the data set and returns a list in which 
        each element contains a list [1, temp].

    Args:
        data: a list with each element containing a time and a list of the core tempatures at that time

    Yields:
        a matrix in nested list form
    
    """
    xMatrix = []
    for temp in data:
        xMatrix.append([1, temp[0]])
    return xMatrix


def makeYmatrix(data, core):
    """
    Notes:
        Nearly identical to the makeYtable function but returns a list or lists
        to allow for use in matrix maniplations

    Args:
        data: a list with each element containing a time and a list of the core tempatures at that time
        core: 0-indexed core number


    Yields:
        a list of tempetures, where each element is a list
    
    """
    y = []
    for temp in data:
        y.append([temp[1][core]])
    return y


    


    
    
     
