def add(list1,counter):
    if len(list1)==counter:
        return 0
    else:
        return list1[counter]+add(list1,counter+1)

list1=[1,2,3,4]
counter=0
print(add(list1,counter))