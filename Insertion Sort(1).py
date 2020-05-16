list1=[25,654,2,9657,6543,765,4312,65]
sorted_list=[]
sorted_list.append(list1[0])
for item in range(1,len(list1)):
    for value in range(len(sorted_list),0,-1):
        print(sorted_list,"  ",list1)
        if list1[item]<sorted_list[value-1]:
            pass
        else:
            sorted_list.insert(value,list1[item])
            
