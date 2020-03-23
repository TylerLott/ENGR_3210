# applies the golden search method to find the minimum of a given function

# IMPORTS
import math

# golden section constant
phi = (math.sqrt(5) - 1) / 2


def goldenSectionMin(xl, xu, itter, itMax):

    # stop function after error is low enough
    if itter < itMax:
        x1 = xu - ((xu - xl) * phi)
        x2 = xl + ((xu - xl) * phi)
        # print(x1, x2)

        if function(x1) > function(x2):
            return goldenSectionMin(x1, xu, itter + 1, itMax)
        else:
            return goldenSectionMin(x2, xl, itter + 1, itMax)

    return xl


def absError(xl, xu, ea):
    numIter = 1
    while True:
        err = (xu - xl) / (1.618**numIter)
        if err < ea:
            break
        else:
            numIter += 1
    return numIter


def function(x):
    return 2*x + (6/x)


if __name__ == "__main__":
    maxIter = absError(1, 5, .00001)
    print(goldenSectionMin(1, 5, 0, maxIter))