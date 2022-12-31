def factorial(n):
    if n in factorial.__dict__:
        return factorial.__dict__[n]

    if n > 1:
        fac = n * factorial(n - 1)
    else:
        fac = 1

    factorial.__dict__[n] = fac
    return fac

print(factorial(5))