#! /usr/bin/env python3
import sys
from parse_temps import (parse_raw_temps)
from linearInterpolation import interpolation
from leastSquares import leastSquares


def main():
    """
    This main function serves as the driver for the demo. Such functions
    are not required in Python. However, we want to prevent unnecessary module
    level (i.e., global) variables.
    """

    input_temps = sys.argv[1]
    includes_units = sys.argv[2] == "False"  # set to False for files without units
    data = []

    with open(input_temps, 'r') as temps_file:
        for temps_as_floats in parse_raw_temps(temps_file, units=includes_units):
            data.append(temps_as_floats)

    leastSquares(data)
    # soltuions = interpolation(data)
    # for sol in soltuions:
    #     print(f"{sol['xFrom']:<5} <= x < {sol['xTo']:>5};    y{sol['yi']:<5} = {sol['c0']:<10} + {sol['c1']:>9}x; interpolation")
    
    



if __name__ == "__main__":
    main()