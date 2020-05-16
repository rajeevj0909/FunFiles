#List
list1=[1,5,7,23,54,76,88,145,256,555,1000,2044,5001]
print(list1)
#User Input
target=int(input("Wat numba u lukin faw?"))
#Flag for found item
found=False
#Used to get index at the end
index=0

#Runs only until the target is found
while found==False:
    print("------------------------\n",list1)
    #Check for odd or even
    if len(list1)%2==0:
        print("Even List")
        #Determines index of centre of list
        centre=int((len(list1)/2)-1)
        #Identifies the value at the centre
        mid=list1[centre]
    else:
        print("Odd list")
        #Determines index of centre of list
        centre=int((len(list1)-1)/2)
        #Identifies the value at the centre
        mid=list1[centre]

    #If target is not in list
    if len(list1)==0:
        print("Not inder uno")
        found=True
    #Checks if the middle of list is the target    
    elif mid==target:
        print("FOUND! Position: ",index+centre+1)
        found=True
    #If target is on left side
    elif target<mid:
        print(target," is on the left of ",mid)
        #Removes the left side (including mid)
        for count in range(len(list1)-centre):
            list1.pop(centre)
            print(list1)
    #If target is on right side
    else:
        print(target," is on the right of ",mid)
        #Removes the right side (including mid)
        for count in range(centre+1):
            index+=1
            list1.pop(0)
            print(list1)
    #Runs the while loop again with a shortened list
