#Imports random
import random
#Open file
file1=open("quizmaker.txt","r")
#Turn file to list
data = file1.read().splitlines()

#Score
score=0
#Creates the pointers to each question so they can be randomly selected
pointers=[0,1,2,3,4,5]

#Takes every 2nd line from list
for i in range(6):
    #Chooese the random question
    choice = random.choice(pointers)
    #This will give position of question in long list
    choose = 2 * choice

    #The answer is the term after the question
    answer=choose+1
    #Asks user the question from long list
    user_answer=input(data[choose])
    #Checks if correct, increments score
    if data[answer]==user_answer:
        score=score+1
        print("YAHHH")
    #If wrong, says the wrong answer
    else:
        print("NAHHH, the answer is:")
        print(data[answer])
    #This goes through pointer list
    for x in pointers:
        #If the position of question is found in pointer list
        if choice==x:
            #Deletes the number from pointer list so it won't ask question again
            delete=pointers.index(x)
    pointers.pop(delete)

#Closes file
file1.close
#End message and final score
print("FINISHED QUIZ")
print("You got a total of ",score, " correct!")
