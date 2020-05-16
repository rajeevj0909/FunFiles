list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
found=False
target=int(input("Pick a number 1-20? "))
#while found==False:
for x in range(4):
    #print("new")
    mid=len(list1)//2
    print(mid)
    print(list1)
    print(list1[mid-1])
    
    if list1[mid-1]==target:
        found=True
        print("GOtcha")
    else:
        if list1[mid-1]>target:
            for i in range(mid+1):
                list1.pop(len(list1)-1)
            print("near the start")
        elif list1[mid-1]<target:
            for i in range(mid+1):
                list1.pop(0)
            print("near the end")

print(found)
