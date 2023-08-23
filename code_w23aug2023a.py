def constant(a):
    if type(a) is int:
        return a
    else:
        return "%s"%a

def plus(x, y):
    if type(x) is int and type(y) is int:
        return x+y
    else:
        return "(%s+%s)"%(x, y)

def times(x, y):
    if type(x) is int and type(y) is int:
        return x*y
    else:
        return "(%s*%s)"%(x, y)

def less(x, y):
    if type(x) is int and type(y) is int:
        return x<y
    else:
        return "(%s<%s)"%(x, y)

if less("2", "3"):
    ...

if less("3", "2"):
    ...

def f(x, y):
    return times(plus(x, y), plus(x, y))

print(f(constant(2), constant(3)))
print(f(constant("2"), constant("3")))
print(less(f(constant("2"), constant("3")), f(constant("4"), constant("5")))
