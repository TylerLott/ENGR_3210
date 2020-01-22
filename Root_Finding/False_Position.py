# applies false position method and prints answer to screen

import math

# Question 1
# XL = 0.5
# XU = 1
# ES = 5

# Question 2
# XL = -1
# XU = 0
# ES = 2

# Question 3
# equation: v(m) = ((9.81 * m) / 15) * (1 - e**((-15 / m) * 10) - 36) = 0
XL = 20
XU = 80
ES = .1



def function(x):
    # Question 1
    # return (x**5) - (10 * x**4) + (46 * x**3) - (90 * x**2) + (85 * x) - 31

    # Question 2
    # return -(3 * x**3) + (20 * x**2) - (20 * x) - 12

    # Question 3
    return (.654 * x) * (1 - math.pow(math.e, (-(15 / x) * 10))) - 36


def false_position(xl, xu, es, imax):
    # initialize variables
    iter = 0
    xr = xl
    ea = es

    # iterative loop that runs until ea is less than es OR iterations are more than imax
    while iter < imax:

        # keep xr_old to calculate error
        xr_old = xr

        # calculate new xr using the secant of the two given points
        xr = xl - (((xu - xl) * function(xl)) / (function(xu) - function(xl)))

        # up the iterator by one
        iter += 1

        # IF the sum of the functions of the first point and new point is less than zero
        # THEN the second point is set to the new point
        # ELSE the first point is set to the new point
        # ELSE the root is perfectly found and error is set to zero
        if function(xr) * function(xl) < 0:
            xu = xr
        elif function(xr) * function(xl) > 0:
            xl = xr
        else:
            ea = 0

        # calculate the error
        if xr != 0:
            ea = abs((xr - xr_old) / xr) * 100
        else:
            print("error")

        # if the error is less than the input threshold then break
        if ea < es:
            break

    return xr


if __name__ == "__main__":
    result = false_position(XL, XU, ES, 100000)
    print(result)
