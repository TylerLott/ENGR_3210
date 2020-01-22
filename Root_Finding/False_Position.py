# applies false position method and prints answer to screen

# Question 1
# XL = 0.5
# XU = 1
# ES = 5

# Question 2
XL = -1
XU = 0
ES = 2


def function(x):
    # Question 1
    # return (x**5) - (10 * x**4) + (46 * x**3) - (90 * x**2) + (85 * x) - 31

    # Question 2
    return -(3 * x**3) + (20 * x**2) - (20 * x) - 12


def false_position(xl, xu, es, imax):
    iter = 0
    xr = xl
    ea = es

    while iter < imax:

        xr_old = xr
        xr = xl - (((xu - xl) * function(xl)) / (function(xu) - function(xl)))
        iter += 1

        if function(xr) * function(xl) < 0:
            xu = xr
        elif function(xr) * function(xl) > 0:
            xl = xr
        else:
            ea = 0

        if xr != 0:
            ea = abs((xr - xr_old) / xr) * 100
        else:
            print("error")

        if ea < es:
            break

    return xr


if __name__ == "__main__":
    result = false_position(XL, XU, ES, 100000)
    print(result)
