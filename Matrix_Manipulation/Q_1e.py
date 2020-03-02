from Gaussian_Elimination import gauss_elim, upper_triangle


def interiorNodes(startT, endT, n):
    # create an n by n matrix
    a = [[0 for ii in range(n)] for i in range(n)]
    b = [0 for i in range(n)]

    for i in range(n):
        a[i][i] = -2.03
        if i < n-1:
            a[i][i+1] = 1
        if i > 0:
            a[i][i-1] = 1

    b[0] = -startT - 0.3
    b[n-1] = -endT - 0.3

    for i in range(1, n-1):
        b[i] = -0.3

    return a, b


if __name__ == "__main__":
    a, b = interiorNodes(20, 100, 1)
    a, b = upper_triangle(a, b)
    one = gauss_elim(a, b)
    print(one)

    a, b = interiorNodes(20, 100, 4)
    a, b = upper_triangle(a, b)
    four = gauss_elim(a, b)
    print(four)

    a, b = interiorNodes(20, 100, 9)
    a, b = upper_triangle(a, b)
    nine = gauss_elim(a, b)
    print(nine)

    a, b = interiorNodes(20, 100, 19)
    a, b = upper_triangle(a, b)
    ninet = gauss_elim(a, b)
    print(ninet)


