#function for main menu
def main_menu():
    #Variable to run the function
    run=input("Do you want to create, add data, locate, delete or update?")
    #if the user enters create,it will run create
    if "create"==run:
        file_create()
    #if the user enters add data,it will run add data
    elif "add data"==run:
        add_data()
    #if the user enters locate,it will run locate
    elif "locate"==run:
        locate()
    #if the user enters delete,it will run delete
    elif "delete"==run:
        delete()
    #if the user enters update,it will run update
    elif "update"==run:
        update()
    #if the user enters something else,it will run again
    else:
        print("SORRY,TRY AGAIN")
        #Goes back to main menu
        main_menu()


#function for creating the file        
def file_create():
    #creates the file
    file=open("database.txt","a")
    #closes the file
    file.close()
    #Goes back to main menu
    main_menu()

#function for adding data
def add_data():
    #Opens the file to edit it
    file=open("database.txt","a")
    #Creates a variable fore the name
    name=input("What is your name?")
    #Creates a variable fore the score
    score=int(input("What is your score?"))
    #Combines the name and score together
    both=name+" "+str(score)
    #Adds the name and score to the file together
    file.write(both+"\n")
    #closes the file
    file.close()
    #Goes back to main menu
    main_menu()

#function for locating data
def locate():
    #Asks if they want to search for the name or the score
    locate=input("Do you want to search for name or score? ")
    #Opens it in read mode to search
    file=open("database.txt","r")
    #runs the if statement for searching by name 
    if locate=="name":
        #Asks for the name being searched
        name=input("Who's name are you searching for? ")
        for line in file:
            if name in line:
                print(line)
                main_menu()
    #runs the if statement for searching by score
    elif locate=="score":
        #Asks for the score being searched
        score=input("What score are you searching for? ")
        for line in file:
            if score in line:
                print(line)
    #closes the file
    file.close
    #Goes back to main menu
    main_menu()

#function for deleting
def delete():
    #Opens the file in read mode
    file=open("database.txt","r")
    #Asks what the user wants to delete
    deleting=input("Who's name and score do you want to delete?   ")
    #Turns the file into a variable
    the_file=file.readlines()
    #Closes the file
    file.close()
    #Opens the file to rewrite it
    file=open("database.txt","w")
    #Checks every line
    for l in the_file:
        #If the line isnt the same as what the user wants to delete
        if l!=deleting+"\n":
            #Prints out that line
            file.write(l)
    #closes the file
    file.close()
    #Goes back to main menu
    main_menu()

#function for updating
def update():
    #Opens the file in read mode
    file=open("database.txt","r")
    #Asks the user what they want changed
    original=input("Whose name and score do you want to change?  ")
    #Turns the file into a variable
    the_file=file.readlines()
    #Closes the file
    file.close()
    #Asks who they are searching for again for validation
    name=input("Who are you searching for? ")
    #Checks every line
    for line in the_file:
        #Checks if name1 is in the line
        if name in line:
            #Prints the line
            print(line)
    #Asks what they want to change it to 
    updated=input("What do you want to change it to?  ")
    #Opens it to rewrite it
    file=open("database.txt","w")
    #Checks every line in the file
    for line in the_file:
        #If the line doesnt equal what the user entered
        if line!=original+"\n":
            #Prints that line
            file.write(line)
        #Anything else that does equal it
        else:
            #Adds in the variable that the user wants to change it to
            file.write(updated+"\n")
    #closes the file
    file.close()
    #Goes back to main menu
    main_menu()

#Runs the main menu
main_menu()
