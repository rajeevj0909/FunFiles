def passMark():
    mark=int(input("Enter a number between 1 and 100, I will check if it is a pass."))
    print (mark)
    if mark>=50>100:
        print("PASS!")
    elif mark>100:
        print("ERROR")
    elif mark<0:
        print("ERROR")
    else:
        print("FAIL!")
passMark()
