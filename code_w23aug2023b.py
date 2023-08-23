def constant(a):
    return (a, str(a))

def plus(x, y):
    return (x[0]+y[0], "(%s+%s)"%(x[1], y[1]))

def times(x, y):
    return (x[0]*y[0], "(%s*%s)"%(x[1], y[1]))

def less(x, y):
    return x[0]<y[0]

def f(x, y):
    return times(plus(x, y), plus(x, y))

print(f(constant(2), constant(3)))
print(less(f(constant(2), constant(3)), f(constant(3), constant(4))))
print(less(f(constant(3), constant(4)), f(constant(2), constant(3))))
