#Inputs the number
full_number = str(input("Please enter a four digit number."))
#Creates variable
element=0
#Creates empty list
str_list=[]
#Every digit in the the number
for n in full_number:
        #Adds that digit to the list
	str_list.append(full_number[element])
	#Increments variable so it can go to next digit
	element=element+1
#Creates empty list for integers
int_lst=[]
#Converts all digits from strings to integers
int_lst = [int(element) for element in str_list]
#Creates easier variable names
first=int_lst[0]
second=int_lst[1]
third=int_lst[2]
fourth=int_lst[3]
##TEST IF THERE IS THERE ARE 4 EQUAL DIGITS
if first==second and first==third and first==fourth:
    #Prints the only output
    #Sep function removes spaces in number
    print(first,second,third,fourth,sep="")
##TEST IF THERE IS THERE ARE 3 EQUAL DIGITS
#Test if 4th digit is different
elif first==second and first==third:
        #Prints all outcomes possible
	print(first,second,third,fourth,sep="")
	print(first,second,fourth,third,sep="")
	print(first,fourth,third,second,sep="")
	print(fourth,second,third,first,sep="")
#Test if 3rd digit is different
elif first==second and first==fourth:
	print(first,second,third,fourth,sep="")
	print(first,second,fourth,third,sep="")
	print(first,third,second,fourth,sep="")
	print(third,second,first,fourth,sep="")
#Test if 2nd digit is different
elif first==third and first==fourth:
	print(first,second,third,fourth,sep="")
	print(first,third,second,fourth,sep="")
	print(first,fourth,third,second,sep="")
	print(second,first,third,fourth,sep="")
#Test if 1st digit is different
elif second==third and second==fourth:
	print(first,second,third,fourth,sep="")
	print(second,first,third,fourth,sep="")
	print(third,second,first,fourth,sep="")
	print(fourth,second,third,first,sep="")
#TEST IF THERE IS THERE ARE 2 "PAIRS OF" EQUAL DIGITS
#Test if 1&2 are equal and 3&4 are equal
elif first==second and third==fourth:
        print(first,first,third,third,sep="")
        print(first,third,first,third,sep="")
        print(first,third,third,first,sep="")
        print(third,third,first,first,sep="")
        print(third,first,third,first,sep="")
        print(third,first,first,third,sep="")
#Test if 1&3 are equal and 2&4 are equal
elif first==third and second==fourth:
        print(first,first,second,second,sep="")
        print(first,second,first,second,sep="")
        print(first,second,second,first,sep="")
        print(second,second,first,first,sep="")
        print(second,first,second,first,sep="")
        print(second,first,first,second,sep="")
#Test if 1&4 are equal and 2&3 are equal
elif first==fourth and second==third:
        print(first,first,third,third,sep="")
        print(first,third,first,third,sep="")
        print(first,third,third,first,sep="")
        print(third,third,first,first,sep="")
        print(third,first,third,first,sep="")
        print(third,first,first,third,sep="")
#TEST IF THERE IS THERE ARE 2 EQUAL DIGITS
#Test if 1&2 are equal, other digits are different
elif first==second:
        print(first,first,third,fourth,sep="")
        print(first,third,first,fourth,sep="")
        print(first,first,fourth,third,sep="")
        print(first,fourth,first,third,sep="")
        print(first,third,fourth,first,sep="")
        print(first,fourth,third,first,sep="")
        print(third,fourth,first,first,sep="")
        print(third,first,fourth,first,sep="")
        print(third,first,first,fourth,sep="")
        print(fourth,third,first,first,sep="")
        print(fourth,first,third,first,sep="")
        print(fourth,first,first,third,sep="")
#Test if 1&3 are equal
elif first==third:
        print(first,first,second,fourth,sep="")
        print(first,second,first,fourth,sep="")
        print(first,first,fourth,second,sep="")
        print(first,fourth,first,second,sep="")
        print(first,second,fourth,first,sep="")
        print(first,fourth,second,first,sep="")
        print(second,fourth,first,first,sep="")
        print(second,first,fourth,first,sep="")
        print(second,first,first,fourth,sep="")
        print(fourth,second,first,first,sep="")
        print(fourth,first,second,first,sep="")
        print(fourth,first,first,second,sep="")
#Test if 1&4 are equal
elif first==fourth:
        print(first,first,third,second,sep="")
        print(first,third,first,second,sep="")
        print(first,first,second,third,sep="")
        print(first,second,first,third,sep="")
        print(first,third,second,first,sep="")
        print(first,second,third,first,sep="")
        print(third,second,first,first,sep="")
        print(third,first,second,first,sep="")
        print(third,first,first,second,sep="")
        print(second,third,first,first,sep="")
        print(second,first,third,first,sep="")
        print(second,first,first,third,sep="")
#Test if 2&3 are equal
elif second==third:
        print(second,second,first,fourth,sep="")
        print(second,first,second,fourth,sep="")
        print(second,second,fourth,first,sep="")
        print(second,fourth,second,first,sep="")
        print(second,first,fourth,second,sep="")
        print(second,fourth,first,second,sep="")
        print(first,fourth,second,second,sep="")
        print(first,second,fourth,second,sep="")
        print(first,second,second,fourth,sep="")
        print(fourth,first,second,second,sep="")
        print(fourth,second,first,second,sep="")
        print(fourth,second,second,first,sep="")
#Test if 2&4 are equal
elif second==fourth:
        print(second,second,first,third,sep="")
        print(second,first,second,third,sep="")
        print(second,second,third,first,sep="")
        print(second,third,second,first,sep="")
        print(second,first,third,second,sep="")
        print(second,third,first,second,sep="")
        print(first,third,second,second,sep="")
        print(first,second,third,second,sep="")
        print(first,second,second,third,sep="")
        print(third,first,second,second,sep="")
        print(third,second,first,second,sep="")
        print(third,second,second,first,sep="")
#Test if 3&4 are equal
elif third==fourth:
        print(third,third,first,second,sep="")
        print(third,first,third,second,sep="")
        print(third,third,second,first,sep="")
        print(third,second,third,first,sep="")
        print(third,first,second,third,sep="")
        print(third,second,first,third,sep="")
        print(first,second,third,third,sep="")
        print(first,third,second,third,sep="")
        print(first,third,third,second,sep="")
        print(second,first,third,third,sep="")
        print(second,third,first,third,sep="")
        print(second,third,third,first,sep="")
#TEST IF THERE IS THERE ARE NO EQUAL DIGITS
else:   #Imports itertools library
        import itertools
        #Names combined a list of all possible combinations in the form of nested lists
        combined=((list(itertools.permutations(int_lst,4))))
        #Gets each combination in the large list
        for a_pin in combined:
                #Gets each digit from that combination
                for digit in a_pin:
                        #Prints the digit and doesn't start a new line
                        print(digit,end="")
                #Starts a new line
                print("")
#METHOD 2 OF PRINTING ALL 24 COMBINATIONS
        #print(first,second,third,fourth)
        #print(first,second,fourth,third)
        #print(first,third,second,fourth)
        #print(first,third,fourth,second)
        #print(first,fourth,second,third)
        #print(first,fourth,third,second)
        #print(second,first,third,fourth)
        #print(second,first,fourth,third)
        #print(second,third,first,fourth)
        #print(second,third,fourth,first)
        #print(second,fourth,first,third)
        #print(second,fourth,third,first)
        #print(third,first,second,fourth)
        #print(third,first,fourth,second)
        #print(third,second,first,fourth)
        #print(third,second,fourth,first)
        #print(third,fourth,first,second)
        #print(third,fourth,second,first)
        #print(fourth,first,second,third)
        #print(fourth,first,third,second)
        #print(fourth,second,first,third)
        #print(fourth,second,third,first)
        #print(fourth,third,first,second)
        #print(fourth,third,second,first)
