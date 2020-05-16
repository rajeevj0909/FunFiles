def locate_in_list(contents):
    search=str(input("What letter do you want to look for?  "))
    if search in contents:
        print("Found the letter do you wanted")
    else:
        print("Not in there...SORRY")


list1=["a","b","c","d","e","f","g"]
locate_in_list(list1)
