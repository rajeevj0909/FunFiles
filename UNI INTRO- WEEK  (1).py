'''def letter_count(s,l):
    total=0
    for i in s:
        if i==l:
            total+=1
    return total

print (letter_count("occur","c"))
'''
'''def username(department,first_name,middle_name,surname):
    user=(department[0]+department[1]+first_name[0]+middle_name[0]+surname[0])
    user=user.lower()
    return(user)

user_name=username("Computer Science","Peter","Andrew","Bull")
print(user_name)'''

'''def street_address(house,street,town,postcode):
    joined=str(house)+" "+street+"\n"+town+"\n"+postcode
    return joined

s=street_address(10,"Downing Street","London","ABC XYZ")
print(s)'''

'''def print_address(house,street,town,postcode):
    print(house, street)
    print(town)
    print(postcode)'''
    
'''def print_square(indent,side):
    symbol= "^" 
    for j in range(0,side):
        print (indent*" " + side*symbol)
symbol= "*" 
print_square (0,3)''' 

'''def print_square(indent,side):
    
    for j in range(0,side):
        print (indent*" " + side*symbol)
symbol= "*" 
print_square (0,3) '''


'''def do_I_work_hard(hours_per_week):
    if hours_per_week>37.5:
        return True
    else:
        return False

x=int(input("How many hours per week do you work?"))
if do_I_work_hard(x)==True:
    print ("I work hard")
else:
    print ("I could work harder")'''

'''import math
def discriminant(a,b,c):
    d=math.sqrt((b**2)-(4*a*c))
    return (d)'''

'''def add2(x):
    return(x+2)'''


'''def do_I_work_hard(hours_per_week):
    if hours_per_week>37.5:
        print("I work hard")
    else:
        print("I could work harder")'''
        
'''def poem():
    print ("I wandered lonely as a cloud")
    print ("That floats on high o'er vales and hills,")
    print ("When all at once I saw a crowd,")
    print ("A host, of golden daffodils;")
    print ("Beside the lake, beneath the trees,")
    print ("Fluttering and dancing in the breeze.")

def poem_times(n):
    for i in range(n):
        poem()'''

'''def poem():
    print("I wandered lonely as a cloud\
\nThat floats on high o'er vales and hills,\
\nWhen all at once I saw a crowd,\
\nA host, of golden daffodils;\
\nBeside the lake, beneath the trees,\
\nFluttering and dancing in the breeze.")

def poem_times_3():
    poem()
    poem()
    poem()

poem_times_3()'''


'''def poem():
    print("I wandered lonely as a cloud\
\nThat floats on high o'er vales and hills,\
\nWhen all at once I saw a crowd,\
\nA host, of golden daffodils;\
\nBeside the lake, beneath the trees,\
\nFluttering and dancing in the breeze.")


poem()
poem()
poem()'''
