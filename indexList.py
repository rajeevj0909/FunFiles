#Makes the function
def indexList(sentence):
    #Makes the list numbered
    enumeratedList=enumerate(sentence)
    #Prints the list
    print(sentence)
    #Asks for the number
    number=int(input("What number do you want? "))
    #Searches for the number asked in the numbered list.
    for index, item in enumeratedList:
        #If it matches
        if index==number-1:
            #Prints the word numbered
            print("The word you wanted is",item,".")
    
#The lst
sentence=["I ","KNOW ","Android ","is ","the ","BEST"]
#Runs the function
indexList(sentence)
