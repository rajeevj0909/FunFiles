0.#1------------------------------------------
#def locate_in_list(contents):
    #search=str(input("What letter do you want to look for?  "))
    #if search in contents:
        #print("Found the letter do you wanted")
    #else:
        #print("Not in there...SORRY")
#list1=["a","b","c","d","e","f","g"]
#locate_in_list(list1)
#-------------------------------------------------
#def word_location():
    #word=input("What word are you looking for?")
    #story = open("story.txt","r")
    #story_list=[]
    #for line in story:
        #for word in line.split():
            #story_list.append(word)
        #story.close()
        #print(story_list)
    #for i in story_list:
        #if word in story_list:
            #print (story.index(i)+1)

#word_location()
#------------------------------------------------------
#def lowerCaseToList():
    #a_string=input(str("Enter a sentence. "))
    #string1=a_string.lower()
    #string2=string1.split()

    #print(string2)
#lowerCaseToList()
#---------------------------------------------------------
##Makes the function
#def indexList(sentence):
    #Makes the list numbered
    #enumeratedList=enumerate(sentence)
    #Prints the list
    #print(sentence)
    #Asks for the number
    #number=int(input("What number do you want? "))
    #Searches for the number asked in the numbered list.
    #for index, item in enumeratedList:
        #If it matches
        #if index==number-1:
            #Prints the word numbered
            #print("The word you wanted is",item,".")
    
#The lst
#sentence=["I ","KNOW ","Android ","is ","the ","BEST"]
#Runs the function
#indexList(sentence)
#--------------------------------------------------------
#Runs the function
def analyise_sentence(list_0):
    #Puts the sentence in lower case
    list1=list_0.lower()
    #Makes the sentence into a list
    list2=list1.split()
    #A counter for the sentence
    counter=0
    #Asks for the word wanting to be searched
    word=input(str("What word would you like to search for? "))
    #Makes the word lower case
    word1=word.lower()
    #If statement for finding the word in the list
    if word1 not in list2:
        #If it is not in there it prints an error
        print("Not in there...SORRY! Try Again!")
    #Searches every item in the list
    for item in list2:
        #Counts the word
        counter=counter+1
        #If the item is in the list
        if item==word1:
            #Prints where it is
            print("The number you wanted is",counter,".")
            
#The sentence        
sentence=("ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU, ASK WHAT YOU CAN DO FOR YOUR COUNTRY")
#Runs the function
analyise_sentence(sentence)
