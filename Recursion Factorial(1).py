def calcFactorial(n):
    if n == 0:
        factorial=1
    else:
        factorial = n * calcFactorial (n-1)
        print(factorial)
    return factorial

n=int(input("Number?"))
print(calcFactorial(n))