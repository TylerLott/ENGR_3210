# applies secant method and prints answer to screen

# root 1 use XL = -.5 , XU = 0
# root 2 use XL = 1 , XU = 3
# root 3 use XL = 5 , XU = 6

XL = 5
XU = 6
ES = .01


def function(x):
    # Question 5
    return (-3 * x ** 3) + (20 * x ** 2) - 20 * x - 12


def secant(xl, xu, es, imax):
    iter = 0
    xr = xl
    ea = es

    while iter < imax:

        xr_old = xr
        xr = xl - (((xu - xl) * function(xl)) / (function(xu) - function(xl)))
        iter += 1

        if xr + xl < xr + xu:
            xu = xr
        else:
            xl = xr

        if xr != 0:
            ea = abs((xr - xr_old) / xr) * 100
        else:
            print("error")

        if ea < es:
            break
    return xr


if __name__ == "__main__":
    result = secant(XL, XU, ES, 100000000)
    print(result)