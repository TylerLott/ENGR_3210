# This is a more general regression model

# IMPORTS
import numpy as np


def GeneralReg(x, y):
    def z0(a):
        return 1

    def z1(a):
        return a

    def z2(a):
        return 1 / a

    zArr = []

    for ii in x:
       zArr.append([z0(ii), z1(ii), z2(ii)])

    print(zArr)
    firstHalf = np.dot(np.transpose(zArr), zArr)

    secHalf = np.dot(np.linalg.inv(firstHalf), np.transpose(zArr))

    return np.dot(secHalf, y)


if __name__ == '__main__':

    x = [1, 2, 3, 4, 5]
    y = [2.2, 2.8, 3.6, 4.5, 5.5]

    z0, z1, z2 = GeneralReg(x, y)

    print("The regression fit is y="+str(z0)+"+"+str(z1)+"x+"+str(z2)+"/x")

