list1=[2,3,4,5,6,7,8]
print(list1)
target=int(input("What u lookin for?"))
for item in range(len(list1)):
    if list1[item]==target:
        print(item+1)
