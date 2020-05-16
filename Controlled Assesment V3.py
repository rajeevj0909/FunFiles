#TASK 2

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

    #TO MAKE THE NUMBERED LIST
    #For every word in the sentence        
    for word1 in sentence_list:
        #If the word is also in the unique sentence
        if word1 in unique_list:
            #Adds word to numbered list
            numbered_list.append(unique_list.index(word1))
            
    file=open("task2.txt","w")
    for i in unique_list:
        file.write(str(i+" "))
    file.write("\n")
    for i in numbered_list:  
        file.write(str(i))
        file.write(" ")
    file.close()

    #TASK 3

    
    compressed_file=open("task2.txt","r")
    compressed_list=[]
    for line in compressed_file:
        compressed_list.append(line.split())
    print(compressed_list)

    
    

  
story=open("Story.txt","r")
story=story.read()
#Runs the function
analyse_sentence(story)






    
