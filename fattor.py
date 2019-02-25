def factorial(g):
    if g == 0:
        return 1
    else:
        return g * factorial(n-1)
g=int(input("the fact is "))
print(factorial(g))
