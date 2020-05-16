import random
import time
'''import pdb;pdb.set_trace()

PYTHON DEBUGGER!!!
Add it into a line to see states of variables...
'''


def game(total,tries):
    if tries<10:
        tries+=1
        print("\nTRY: ",tries)
        '''guess=input("ENTER A NUMBER BETWEEN 1 & 2: ")'''
        guess=1
        num1=random.randint(1,2)
        print(num1)
        
        try:
            if int(guess)==(num1):
                print("Correct")
                total+=1
                time.sleep(1)
                game(total,tries)
                
            elif int(guess)!=(num1):
                print("Incorrect")
                time.sleep(1)
                game(total,tries)
                   
        except:
            print("Not an integer")
        return total
        
    else:
        return total


print("Hi GUYS!!!")
total=0
tries=0
total=game(total,tries)


print(total)
if total==10:
    print("Well done, full marks")
elif total>5:
    print("Well done, half marks")
elif total>2:
    print("Well done, you got over 2!")
else:
    print("BAD SCORE DUDE")
    
print("Score: ",total)

