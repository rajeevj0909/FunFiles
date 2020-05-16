def add(list1,counter,total):
    n=len(list1)
    if n==counter:
        print(total)
    else:
        total=add(list1[counter],counter,total)+total
        return(total)
    return counter
    counter = counter + 1

list1=[1,2,3,4]
counter=0
total=0
add(list1,counter,total)
