def write():
    f = open("practice.txt","w")
    for i in range(10):
        f.write("This is line %d\n"%(i+1))
    f.close()

def read():
    f = open("practice.txt","r")
    contents = f.read()
    print(contents)
    f.close()

def append(text):
    f = open("practice.txt","a")
    f.write(text)
    f.close()


userInput = input("'w' to write to the file \n'r' to read from the file \n'a' to append")
if userInput == 'w':
    write()
elif userInput == 'r':
    read()
elif userInput == 'a':
    text = input("enter some text to add to the file:\n")
    append(text)

