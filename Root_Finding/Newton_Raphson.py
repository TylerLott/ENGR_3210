# applies Newton Raphson method and prints answer to screen

X0 = 4.5
ES = .01


def function(x):
    # Question 4
    return (.5 * x**3) - (4 * x**2) + 8 * x - 1

    # Question 5
    # return (-3 * x**3) + (20 * x**2) - 20 * x - 12


def deriv_function(x):
    # Question 4
    return (1.5 * x**2) - (8 * x) + 8

    # Question 5
    # return (-9 * x**2) + (40 * x) - 20


def newton_raphson(x0, es):

    xr_old = x0
    xr = x0 - (function(x0) / deriv_function(x0))

    if xr != 0:
        ea = abs((xr - xr_old) / xr) * 100
    else:
        print("error")

    if ea < es:
        return xr
    else:
        return newton_raphson(xr, es)


if __name__ == "__main__":
    result = newton_raphson(X0, ES)
    print(result)