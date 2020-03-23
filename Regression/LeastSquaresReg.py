# This is a simple linear regression given arrays of x and y points


def LeastSquaresReg(x, y):
    sumX = 0
    sumY = 0
    sumXY = 0
    sumx2 = 0

    for i in range(len(x)):
        sumX += x[i]
        sumY += y[i]
        sumXY += (y[i] * x[i])
        sumx2 += x[i]**2

    mean = ((len(x) * sumXY) - (sumX * sumY)) / ((len(x) * sumx2) - sumX**2)

    b = (sumY - (mean * sumX)) / len(x)

    return mean, b


if __name__ == '__main__':

    x = [0, 2, 4, 6, 9, 11, 12, 15, 17, 19]
    y = [5, 6, 7, 6, 9, 8, 7, 10, 12, 12]

    print(LeastSquaresReg(x, y))
