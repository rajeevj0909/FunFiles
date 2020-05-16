list1=[1,2,3,4,5,6,7,8,9]
found=False
target=int(input("Pick a number? "))
while found==False:
    mid=(len(list1)//2)+1
    if list1[mid-1]==target:
        found=True
        print("FOUND")
    else:
        if list1[mid]>target:
            for i in range(mid):
                list1.pop(len(list1)-1)
            print("near the start")
        elif list1[mid]<target:
            for i in range(mid):
                list1.pop(0)
            print("near the end")

print(found)
