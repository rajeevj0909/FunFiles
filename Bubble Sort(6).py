list1=[25,654,2,9657,6543,765,4312,65,44]
swapping=True
while swapping ==True:
    swapping =False
    for item in range(len(list1)-1):
        if list1[item]>list1[item+1]:
            print(list1)
            temp=list1[item]
            list1[item]=list1[item+1]
            list1[item+1]=temp
            swapping =True
print(list1)
