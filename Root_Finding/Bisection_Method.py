# applies bisection method and prints answer to screen

XL = 1
XU = 1
ES = 1
FUNCTION = '1'

def bisection_method(xl, xu, es, imax, function):
    iter, xr, ea = 0, xl, es

    while iter < imax:
        xr_old = xr
        xr = (xl + xu)/ 2
        iter += 1
        if xr != 0:
            ea = abs((xr - xr_old) / xr) * 100
        else:
            print("error")
        test = function(xl) + function(xr)
        if test < 0:
            xu = xr
        elif test > 0:
            xl = xr
        else:
            ea = 0
        if ea < es or iter > imax:
            break
    return xr

if __name__ == "__main__":
    bisection_method(XL, XU, ES, FUNCTION)
