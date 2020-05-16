#Makes the function
def analyse_sentence(sentence):
    #Turns sentence into list
    sentence_list=sentence.split()
    #Creates an empty list
    unique_list=[]
    #Creates a numbered List
    numbered_list=[]

    #TO MAKE THE UNIQUE LIST
    #For every word in the list
    for word in sentence_list:
        #If the word isn't unique_list already
        if word not in unique_list:
            #Adds the word into the list
            unique_list.append(word)

    #For every word in the sentence        
    for word1 in sentence_list:
        #If the word is also in the unique sentence
        if word1 in unique_list:
            #Adds word to numbered list
            numbered_list.append(unique_list.index(word1)+1)
    file=open("task2.txt","w")
    file.write("The sentence:  \n")
    file.write("ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY \n   \n")
    file.write("List in numbers: \n")
    file.write(str(numbered_list))

    
#The list
sentence="ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY"
#Runs the function
analyse_sentence(sentence)
