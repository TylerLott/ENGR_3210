# Gaussian Elimination with partial pivoting


# pivot if larger than an order of magnitude
def gauss_elim(a, b):
    # forward elimination

    a, b = upper_triangle(a, b)

    # n = len(a)
    # k = 0
    # while k < n:
    #     i = k+1
    #     while i < n:
    #         factor = a[i][k] / a[k][k]
    #         print(factor)
    #
    #         # partial pivot
    #         if factor >= (a[k][i] / a[i][i]):
    #             tempA = a[k]
    #             a[k] = a[i]
    #             a[i] = tempA
    #             tempB = b[k]
    #             b[k] = b[i]
    #             b[i] = tempB
    #             factor = a[i][k] / a[k][k]
    #
    #         j = k+1
    #         while j < n:
    #             a[i][j] = a[i][j] - factor * a[k][j]
    #             j += 1
    #         b[i] = b[i] - factor * b[k]
    #         i += 1
    #     k += 1

    # back substitution
    n = len(a)
    i = n-1
    f = [0] * n
    f[n-1] = b[i] / a[i][i]
    while i >= 0:
        s = b[i]
        j = n-1
        while j > i:
            s = s - a[i][j] * f[j]
            j -= 1
        f[i] = s / a[i][i]
        i -= 1

    return f


def upper_triangle(a, b):
    # forward elimination
    n = len(a)
    k = 0
    while k < n:
        i = k + 1
        while i < n:
            factor = a[i][k] / a[k][k]

            # partial pivot
            if factor >= (a[k][i] / a[i][i]):
                tempA = a[k]
                a[k] = a[i]
                a[i] = tempA
                tempB = b[k]
                b[k] = b[i]
                b[i] = tempB
                factor = a[i][k] / a[k][k]

            j = k + 1
            while j < n:
                a[i][j] = a[i][j] - factor * a[k][j]
                j += 1
            b[i] = b[i] - factor * b[k]
            i += 1
        k += 1

    return a, b


if __name__ == "__main__":
    arr = [[1, 2, -1], [5, 2, 2], [-3, 5, -1]]
    c = [2, 9, 1]

    # arr = [[10, 2, -1], [-3, -6, 2], [1, 1, 5]]
    # c = [27, -61.5, -21.5]

    ans = gauss_elim(arr, c)
    print(ans)


