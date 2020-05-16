def is_equal(a, b):
    if a==b:
        equal="Yes it is";
    else:
        equal="No it isn't";
    return equal

print ("Are these two numbers equal?")
num1=int(input("Enter number 1?  "))
num2=int(input("Enter number 2?  "))        
answer=is_equal(num1, num2)
print(answer)
