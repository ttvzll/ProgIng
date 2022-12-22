def func(x):
    def myfunc(y):
        return x + y
    return myfunc
f = func(5)
print(f(2))