file1=open("rockclimbing.txt","a")
'''
for line in file1:
    print (line)
'''
def details():
    f_name=input("What's your first name?  ")
    l_name=input("What's your last name?   ")
    birth=input("When were born? (dd/mm/yyyy) ")
    address=input("What's your address?  ")
    email=input("What's your email?  ")
    contact_no=input("What's your emergency contact number?   ")
    
    print("\n\nName: ",f_name+" ",l_name)
    print("You were born: ",birth)
    print("You live at: ",address)
    print("Yor email is: ",email)
    print("Your emergency contact number is: ",contact_no)

    check=input("Are these correct?")
    if check=="Yes":
        file1.write("\n\n")
        file1.write(f_name)
        file1.write("\n")
        file1.write(l_name)
        file1.write("\n")
        file1.write(birth)
        file1.write("\n")
        file1.write(address)
        file1.write("\n")
        file1.write(email)
        file1.write("\n")
        file1.write(contact_no)
        file1.write("\n")
    else:
        print("Tell us your details again....")
        details()
        
    add_person=input("Do you want to add another person?  ")
    if add_person=="Yes":
        details()
    else:
        print("Okay then! ")

details()



file1.close()
