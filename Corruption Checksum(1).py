list1=[5, 1, 9, 5]
list2=[7, 5, 3]
list3=[2, 4, 6, 8]


list1.sort()
total1=list1[len(list1)-1]-list1[0]

list2.sort()
total2=list2[len(list2)-1]-list2[0]

list3.sort()
total3=list3[len(list3)-1]-list3[0]

total=total1+total2+total3
print(total)

items=str(input("Whats the list?"))
print(items)
bundle=[]
for digit in items:
    if digit=="\t":
        bundle.append("Tab")
    elif digit=="\n":
        bundle.append("NEWWWWW LINNEEEEEEEEEEEEEE")
    else:
        bundle.append(digit)

print(bundle)

