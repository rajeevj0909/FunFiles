#Creates the function called "Index List"
def indexlist(a_list):
    #Asks the user for a number
    number=int(input("What number would you like?"))
    #Creates an empty list
    index_list=[]
    #Creates a variable with the value of 0 
    index=0
    #Checks in every element of the list
    for i in a_list:
        #Adds the index to the list
        index_list.append(index)
        #Index adds 1 to itself
        index=index+1
        #If the number is in the index list
    if number in index_list:
        #Returns the letter
        return a_list[number-1]
    #Any other result
    else:
        #Prints an error
        return "not found"

#The list
testlist=["a","b","c","d","e"]
#Runs the function and prints the answer
print(indexlist(testlist))
