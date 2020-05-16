seq=[0,1]
a=0
b=1
number=int(input("What number do you want?"))

for i in range(number):
    a=seq[i]
    b=seq[i+1]
    a=a+b
    seq.append(a)


print(seq[number-1])
fib=[0,1,1,2,3,5,8,13]

