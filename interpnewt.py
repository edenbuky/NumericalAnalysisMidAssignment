# 2. A function which evaluates Newton’s interpolation polynomial at a new set of points
def interpnewt(c,x,xnew):

    def newton_polynomial(c,x,r):
        n = x.size - 1
        p = c[0,n]
        for i in range(1,n + 1):
            p = c[0,n - i] + (r - x[0,n - i])*p
        return p
    m = xnew.size
    ynew = np.empty((1,m))
    for i in range(m):
        ynew[0,i] = newton_polynomial(c,x,xnew[0,i])
    return ynew
