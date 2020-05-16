#List
list1=[1,5,7,23,54,76,88,145,256,555,1000,2044,5001]
print(list1)
#User Input
target=int(input("Wat numba u lukin faw?"))
#Used to get index at the end
index=0

#Function to recurse
def search(list1,index):
    print("------------------------\n",list1)
    print(index)
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


    #Checks if the middle of list is the target
    if mid==target:
        print("FOUND! Position: ",index+centre+1)
    #If target is on left side
    elif target<mid:
        print(target," is on the left side.")
        #Removes the left side (including mid)
        for count in range(len(list1)-centre):
            list1.pop(centre)
            print(list1)
        #Shortens the list again
        search(list1,index)
    #If target is on right side
    else:
        print(target," is on the right side.")
        #Removes the right side (including mid)
        for count in range(centre+1):
            index+=1
            list1.pop(0)
            print(list1)
        #Shortens the list again
        search(list1,index)
        
#Searches for first time
search(list1,index)
