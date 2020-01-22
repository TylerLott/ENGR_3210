# applies bisection method and prints answer to screen

XL = .5
XU = 1
ES = .1


def bisection_method(xl, xu, es, imax):
    iter = 0
    xr = xl
    ea = es

    while iter < imax:
        xr_old = xr
        xr = (xl + xu) / 2
        iter += 1
        if xr != 0:
            ea = abs((xr - xr_old) / xr) * 100
        else:
            print("error")
        test = (xl**5 - (10 * xl**4) + (46 * xl**3) - (90 * xl**2) + (85 * xl) - 31) + \
               (xr**5 - (10 * xr**4) + (46 * xr**3) - (90 * xr**2) + (85 * xr) - 31)
        if test < 0:
            xl = xr
        elif test > 0:
            xu = xr
        else:
            ea = 0
        if ea < es:
            break
    return xr


if __name__ == "__main__":
    result = bisection_method(XL, XU, ES, 10000)
    print(result)
