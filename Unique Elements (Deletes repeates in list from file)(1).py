def UniqueElements(original):
    emptyList=[]
    for i in original:
        if i not in emptyList:
            emptyList.append(i)
    return emptyList


myfile=open("List.txt","r")
numbers=myfile.readlines()
final=UniqueElements(numbers)
myfile.close()
print(final)

