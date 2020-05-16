#The unordered list
lists=[1,10,2,9,3,8,4,7,5,6]
#Prints the original list
print(lists)
#For length of numbers in list
for element in range(len(lists)-1,0,-1):
    #For each number from element
    for digit in range(element):
        #If that number is larger than the number next to it in the list
        if int(lists[digit])>int(lists[digit+1]):
            #Takes the number of the one infront
            swap=lists[digit]
            #Swaps the original digit and the new digit
            lists[digit]=lists[digit+1]
            #Takes the number originally there and stores that
            lists[digit+1]=swap
#Prints the final list
    print(lists)


