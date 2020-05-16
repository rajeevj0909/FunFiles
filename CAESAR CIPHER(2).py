#List of alphabet
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#Takes a user sentence
sentence=input("What's your sentence?")
#Shows the sentence for comparison to new code
print(sentence)
#Turns to lowercase so it can find in alphabet list
sentence=sentence.lower()
#Turns sentence into list to do each character individually
list1=list(sentence)
#Creates new list for coded message
coded=[]
#Goes through every character in sentence.
for character in list1:
    #If the character is a letter in the alphabet
    if character in alphabet:
        #Finds position of letter in alphabet
        for letter in alphabet:
            if character==letter:
                position_old=alphabet.index(character)
        #Finds new position of letter
        if position_old<23:
            position_new=position_old+3
        #If letter is at the end of alphabet
        else:
            #These positions go back to the start
            position_new=position_old-23
        #Adds the new letter to the new list
        coded.append(alphabet[position_new])
    #If the character is NOT a letter in the alphabet
    else:
        #Adds it into the new list
        coded.append(character)
#Joins the new list into a sentence
coded_sentence="".join(coded)
#Prints new sentence
print(coded_sentence)

#Attack the zombies at dawn!
#dwwdfn wkh crpelhv dw gdzq!
