def analyise_sentence(list_0):
    list1=list_0.lower()
    list2=list1.split()
    print(list2)
    index=0
    word=input(str("What word would you like to search for? "))
    word1=word.lower()
    if word1 in list2:
        print("I have found the word you entered!")
    else:
        print("Not in there...SORRY! Try Again!")
        analyise_sentence(list_0)
    enumeratedList=enumerate(list1)
    print(enumeratedList)
    number=int(input("What number do you want? "))
    for index, item in enumeratedList:
        if index==number-1:
            print("The word you wanted is",item,".")
    
    
        
list1=("ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU, ASK WHAT YOU CAN DO FOR YOUR COUNTRY")
analyise_sentence(list1)
