# LU decomposition

from Gaussian_Elimination import gauss_elim


def luDecomposition(a, b):
    n = len(a)
    pivots = []
    l = [[0 for x in range(n)] for y in range(n)]
    u = [[0 for x in range(n)] for y in range(n)]

    # Decomposing matrix into Upper and Lower triangular matrix
    for i in range(n):

        # Upper Triangular
        for k in range(i, n):

            sum = 0
            for j in range(i):

                # partial pivot
                row1 = a[j][j] / a[k][j]
                row2 = a[k][j] / a[j][j]
                if abs(row1) < abs(row2):
                    tempA = a[k]
                    a[k] = a[j]
                    a[j] = tempA
                    tempB = b[k]
                    b[k] = b[j]
                    b[j] = tempB
                    pivots.append([k, j])

                sum += (l[i][j] * u[j][k])

            u[i][k] = a[i][k] - sum

            # Lower Triangular
        for k in range(i, n):
            if i == k:
                l[i][i] = 1
            else:

                sum = 0
                for j in range(i):
                    sum += (l[k][j] * u[j][i])

                l[k][i] = (a[k][i] - sum) / u[i][i]

    return u, l, b, pivots


def solveFromLU(u, l, b):
    b = solveLower(l, b)
    b = gauss_elim(u, b)

    return b


def solveLower(l, b):
    # forward substitution
    n = len(l)
    i = 0
    f = [0] * n
    f[0] = b[i] / l[i][i]
    while i < n:
        s = b[i]
        j = 0
        while j < i:
            s = s - l[i][j] * f[j]
            j += 1
        f[i] = s / l[i][i]
        i += 1

    return f


def inverseFromLU(u, l, pivots):

    inverse = []
    pre_upper = []
    n = len(u)
    final = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        b = [0 for x in range(n)]

        b[i] = 1

        next = solveLower(l, b)

        pre_upper.append(next)

    for i in pre_upper:

        column = gauss_elim(u, i)

        inverse.append(column)

    # pivots reverses pivot from the initial pivot
    pivots.reverse()
    for i in pivots:
        k = i[0]
        j = i[1]

        tempA = inverse[j]
        inverse[j] = inverse[k]
        inverse[k] = tempA

    for i in range(len(inverse)):
        for j in range(len(inverse)):
            final[i][j] = inverse [j][i]

    return final


if __name__ == "__main__":

    arr = [[1, 1],
           [5.652233, .1769212]]

    b = [10, 90]
    #
    # arr = [[2, -6, -1],
    #        [-3, -1, 7],
    #        [-8, 1, -2]]
    #
    # b = [-38, -34, -20]

    # arr = [[8, 4, -1],
    #        [-2, 5, 1],
    #        [2, -1, 6]]
    #
    # b = [11, 4, 7]

    u, l, b, piv = luDecomposition(arr, b)
    u, l, b, piv2 = luDecomposition(arr, b)

    print("Solved equations:")
    print(solveFromLU(u, l, b))

    print()
    print("inverse matrix")

    inv = inverseFromLU(u, l, piv)

    for i in inv:
        print(i)


