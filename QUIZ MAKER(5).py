file1=open("quizmaker.txt","r")
data = file1.read().splitlines()
counter=-1
total=0
for line in data[::2]:
    counter=counter+2
    answer=input(line)
    if data[counter]==answer:
        total=total+1
        print("YAHHH")
    else:
        print("NAHHH, the answer is:")
        print(data[counter])

file1.close
print("FINISHED QUIZ")
print("You got a total of ",total, " correct!")

