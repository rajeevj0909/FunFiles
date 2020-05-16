def max(a, b):
    if num1>num2:
        largest=num1
    elif num1==num2:
        print("ERROR")
    else:
        largest=num2
    return largest

num1=int(input("Enter first number.    "))
num2=int(input("Enter second number.    "))
answer=max(num1, num2)
print("The bigger number is", answer)

