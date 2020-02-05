# applies secant method and prints answer to screen

# root 1 use XL = -.5 , XU = 0
# root 2 use XL = 1 , XU = 3
# root 3 use XL = 5 , XU = 6

XL = 5
XU = 6
ES = .1


def function(x):
    # Question 5
    return (-3 * x ** 3) + (20 * x ** 2) - 20 * x - 12


def secant(xl, xu, es, imax):
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

        # IF the average of the first and new point is less than the second point and new point
        # THEN change the second point to the new point
        # ELSE change the first point to the new point
        if xr + xl < xr + xu:
            xu = xr
        else:
            xl = xr

        # calculate the error
        if xr != 0:
            ea = abs((xr - xr_old) / xr) * 100
        else:
            print("error")

        # if the error is less than the threshold determined then break
        if ea < es:
            break
    return xr, xr_old


if __name__ == "__main__":
    result, result_old = secant(XL, XU, ES, 100000000)
    print(result, result_old)