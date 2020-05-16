my_file = open("delete_entry.txt","r")
lines  = my_file.readlines()
my_file.close()
my_file = open("delete_entry.txt","r")
nickname_to_delete=input('What would you like to find in your file?')
for l in lines:
    if l == nickname_to_delete:
        print ('Yes it is there')
    elif l!=nickname_to_delete+"\n":
        print("No it isn't")
my_file.close()
