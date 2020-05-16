pets = [] # Start with an empty list
while True:
    p = input( "Please add an item to the shopping list ('q' - quit )")
    if p=='q':
        break
    else:
        if p in pets:
            print("Item -",p,"- is already in the shopping list")
        else:
            pets.append(p)
        pets.sort()
        print(pets)



'''sumx = 0
n = int(input("How many numbers ? ")) 
xlist = []
for count in range(n): 
      x = float(input( "Enter a number : ")) 
      sumx = sumx + x 
      xlist.append(x)
print ("The sum was " + str(sumx))
print ("The average was " + (str(sumx/n)))
print("           x      x-Mean")
for x in xlist:
    print("%12.2f %11.2f"%(x,x-sumx/n))'''


'''pets = [] # Start with an empty list
while True:
    p = input( "Enter a pet (or q to quit): ")
    if p=='q':
        break
    else:
        pets.append(p)
for pet in pets:
    print(pet)'''

'''modules =['COA201','COA122','COA124']
for i in modules:
    print("18"+i)'''

'''string=input("Please enter a list of modules. Use ',' to seperate the modules")
list1=string.split(",")
list1.sort()
print(list1)'''

'''shopping=["Bread","Milk","Tea","Soap"]
print  (shopping[ 3])
'''
'''modules = ['COA122','COA108','COA111','COA123']
print(modules[0])'''

'''modules = ['COA122','COA108','COA111','COA123']
modules[2]='COA256'
print(modules)
'''
'''modules = ['COA122','COA108','COA111','COA123']
modules.insert(2,'COA256')
print(modules)'''
'''
modules = ['COA122','COA108','COA111','COA123']
del(modules[0])
print(modules)'''

'''modules =['COA001','COA105','COA107','COA108']
modules+=['COA220','COA122','COA202']
print(modules)'''

'''modules = ['COA122','COA108','COA111','COA123']
modules.append('COA201' )
print(modules)'''

