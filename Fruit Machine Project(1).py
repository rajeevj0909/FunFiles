#programmes random from the library
import random
#creates a list of values under the variable name symbols
symbols = ["Cherry","Bell","Lemon","Orange","Star","Skull"]
#gives the value of 100 to the variable user_credit
user_credit = 100
#programmes it so that the variable SPIN haas a value of yes
SPIN = "yes"
#creates a loop so that while the user wants to spin and the user's credit is more than 0 then ...
while SPIN == "yes" and user_credit > 0:
    #for every spin 20 is taken away from the user's credit
    user_credit = user_credit - 20
    #gives the variable spin 1 the value of a random value of the variable symbols
    spin1 = random.choice(symbols)
    #gives the variable spin 2 the value of a random value of the variable symbols
    spin2 = random.choice(symbols)
    #gives the variable spin 3 the value of a random value of the variable symbols
    spin3 = random.choice(symbols)
    #prints what the 3 spins are and what the user's creedit is after each go
    print("Spins :",spin1,",",spin2,",",spin3,"& Credit :",user_credit)
    #if all 3 spins are Cherry then ...
    if spin1=="Cherry" and spin2=="Cherry" and spin3=="Cherry" :
        #the user's credit increases by 50
        user_credit = user_credit + 50
        #tells the user they have gained 50 credit
        print("Well Done ! You have gained 50 credits.")
    #if all 3 spins are Lemon then ...
    elif spin1=="Lemon" and spin2=="Lemon" and spin3=="Lemon" :
        #the user's credit increases by 50
        user_credit = user_credit + 50
        #tells the user they have gained 50 credit
        print("Well Done ! You have gained 50 credits.")
    #if all 3 spins are Orange then ...
    elif spin1=="Orange" and spin2=="Orange" and spin3=="Orange" :
        #the user's credit increases by 50
        user_credit = user_credit + 50
        #tells the user they have gained 50 credit
        print("Well Done ! You have gained 50 credits.")
    #if all 3 spins are Star then ...
    elif spin1=="Star" and spin2=="Star" and spin3=="Star" :
        #the user's credit increases by 50
        user_credit = user_credit + 50
        #tells the user they have gained 50 credit
        print("Well Done ! You have gained 50 credits.")
    #if all 3 spins are Bell then ...
    elif spin1=="Bell" and spin2=="Bell" and spin3=="Bell" :
        #user's credit increases by 100
        user_credit = user_credit + 100
        #tells the user they have gained 100 credit
        print("Well Done ! You have gained 100 credits .")
    #if all 3 spins are Skull then ...
    elif spin1=="Skull" and spin2=="Skull" and spin3=="Skull" :
        #the user loses all of their credit
        user_credit = user_credit - user_credit
        #tells the user they have lost all their credit
        print("Bad Luck! You have lost all of your credits.")
    #if 2 of the spins are Skull then ...
    elif spin1=="Skull" and spin2=="Skull" or spin1=="Skull" and spin3=="Skull" or spin2=="Skull" and spin3=="Skull" :
        #the user's credit decreases by 100
        user_credit = user_credit - 100
        #tells the user they have gained 50 credit
        print("Bad Luck! You have lost 100 credits.")
    #gives the variable SPIN a second value of the outcome of the question "Do you want to spin?"
    SPIN = input("Do you want to spin?")
    #if the user's credit is equal to or less than 0 / spin equals anythng other than yes then ...
    if user_credit <= 0 or SPIN == "":
    #SPIN gets a value of no which ends the loop
        SPIN = "no"
    


