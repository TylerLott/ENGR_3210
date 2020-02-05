# Gaussian Elimination with partial pivoting


# pivot if larger than an order of magnitude
def gauss_elim(a, b):
    # forward elimination
    n = len(a)
    k = 0
    while k < n:
        i = k+1
        while i < n:
            factor = a[i][k] / a[k][k]
            j = k+1
            while j < n:
                a[i][j] = a[i][j] - factor * a[k][j]
                j += 1
            b[i] = b[i] - factor * b[k]
            i += 1
        k += 1

    # back substitution

    print(a)
    print(b)


if __name__ == "__main__":
    arr = [[1, 2, -1], [5, 2, 2], [-3, 5, -1]]
    c = [2, 9, 1]

    gauss_elim(arr, c)


