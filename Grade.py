file=open("grade.txt", "a")
grade=input("What's your grade")
file.write(grade)
file=open("grade.txt","r")
for i in file:
    print(i)
file.close()

