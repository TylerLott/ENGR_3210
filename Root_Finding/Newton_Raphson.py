# applies Newton Raphson method and prints answer to screen

# use 0 for root 1
# use 3 for root 2
# use 4.5 for root 3

X0 = 4.5
ES = .01


def function(x):
    # Question 4
    return (.5 * x**3) - (4 * x**2) + 8 * x - 1


def deriv_function(x):
    # Question 4
    return (1.5 * x**2) - (8 * x) + 8



def newton_raphson(x0, es):

    # define x0_old to calculate the error
    xr_old = x0

    # this is the actual newton raphson part, calculates a new x based on the old point subtracting the point from
    # the function divided by the derivative of the function
    xr = x0 - (function(x0) / deriv_function(x0))

    # calculate the error and print error if xr = 0
    if xr != 0:
        ea = abs((xr - xr_old) / xr) * 100
    else:
        print("error")

    # if within the range of accuracy wanted return xr
    if ea < es:
        return xr
    else:
        # if not in range of accuracy recursively call the function using xr as the new x0 point
        return newton_raphson(xr, es)


if __name__ == "__main__":
    result = newton_raphson(X0, ES)
    print(result)