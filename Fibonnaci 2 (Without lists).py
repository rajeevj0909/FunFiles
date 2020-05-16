pos=int(input("What position in the Fibonacci sequence would you like?"))
start = 0
second = 1

if pos == 1:
    print(0)
elif pos == 2:
    print = 1
else:
    for i in range(pos-2):
        start = start+second
        second=second+start
        print(start)
        print(second)
    print(second)

l=[ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34]