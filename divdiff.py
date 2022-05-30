import numpy as np
# 1. A function that constructs the coefficients required for evaluating the Newton form of the interpolation polynomial
def divdiff(x,y):
    n = x.size
    f = np.zeros((n,n),float)
    c = np.empty((1,n))
    for i in range(n):
        f[i,0] = y[0,i]
    for j in range(1,n):
        for i in range(j,n):
            f[i,j] = float(f[i,j-1] -f[i-1,j-1])/float(x[0,i]-x[0,i-j])
    for i in range(n):
        c[0,i] = f[i,i]
    return c
