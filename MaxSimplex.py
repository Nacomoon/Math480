class MaxSimplex():
    def __init__(this, a, b, c):
        x = this.cmax(c)
        y = this.amin(a,b,x[1])
        this.class_field = (x,y)
    def cmax(this, c):
        cmax = 0
        index = -1
        for x in c:
            if cmax < x:
                cmax = x
                index = c.index(cmax)
        return (cmax, index)
    def amin(this, a,b,index):
        amin = 10e6
        aleav = 0
        for x in a:
            a1 = x[index]
            b1 = b[a.index(x)]
            if x[index] > 0 and b1/a1 < amin:
                amin = b1/a1
                aleav = a1
                index2 = a.index(x)
        return (aleav, index2)
