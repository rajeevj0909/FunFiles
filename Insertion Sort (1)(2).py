list1=[9,8,7,6,5,4,3,2,1]
for item in range(1,len(list1)):
    print(item,":  ",list1)
    for value in range(item):
        if list1[item]<list1[value]:
            temp=list1[item]
            list1[item]=list1[value]
            list1[value]=temp

print(list1)
