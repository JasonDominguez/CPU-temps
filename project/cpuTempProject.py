#! /usr/bin/env python3
import sys
from parse_temps import (parse_raw_temps)
from linearInterpolation import interpolation
from leastSquares import leastSquares


def main():
    """
    This main function serves as the driver for the project. Such functions
    are not required in Python. However, we want to prevent unnecessary module
    level (i.e., global) variables.
    """
    input_temps = sys.argv[1]
    includes_units = sys.argv[2] == "False"  # set to False for files without units
    data = []

    with open(input_temps, 'r') as temps_file:
        for temps_as_floats in parse_raw_temps(temps_file, units=includes_units):
            data.append(temps_as_floats)

    basename = input_temps.split('.')[0]
    for coreNum in range(len(data[0][1])):
        f = open(f"{basename}-core-{coreNum}.txt", "w")
        ls = leastSquares(data, coreNum)
        li = interpolation(data, coreNum)
        for l in li:
            f.write(strCreator(l))
        f.write(strCreator(ls))
        f.close()


def strCreator(sol):
    """
    Notes:
        This function creates the output string in the form x_k <= x < x_k+1; y_i = c_0 + c_1 x; type
        where
            x_k and x_k+1 are the domain in which y_k is applicable
            y_k is the kth function
            type is either least-squares or interpolation

    Args:
        sol: Dict{'xFrom': , 'xTo': , 'yi': ,'c0': , 'c1': , 'type': }

    Yields:
        A formated string with new line charater at the end
    """

    domain = f"{sol['xFrom']} <= x < {sol['xTo']};"

    if sol['c1'] == 0:
        func = f"y{sol['yi']} = {'{:.3f}'.format(sol['c0'])};"
    elif sol['c1'] == 1:
        func = f"y{sol['yi']} = {'{:.3f}'.format(sol['c0'])} + x;"
    elif sol['c1'] < 0:
        func = f"y{sol['yi']} = {'{:.3f}'.format(sol['c0'])} - {'{:.4g}'.format(abs(sol['c1']))}x;"
    else:
        func = f"y{sol['yi']} = {'{:.3f}'.format(sol['c0'])} + {'{:.4g}'.format(sol['c1'])}x;"

    string = f"{domain:^20}{func:<30}{sol['type']}\n"
    return string



if __name__ == "__main__":
    main()

