#Validation for the input
valid = False
while valid == False:
    try:
        full_number = int(input("Please enter a four digit number."))
        if isinstance(full_number, int) == True:
            valid = True
    except ValueError:
        print("This is not a whole number")

#Calculating the different combinations
str_number = str(full_number)
digit1 = str_number[0]
digit2 = str_number[1]
digit3 = str_number[2]
digit4 = str_number[3]
combinations = []
for first in range(4):
    for second in range(4):
        for third in range(4):
            for fourth in range(4):
                poss_combo = [str_number[first],str_number[second],str_number[third],str_number[fourth]]
                if digit1 in poss_combo:
                    if digit2 in poss_combo:
                        if digit3 in poss_combo:
                            if digit4 in poss_combo:
                                if poss_combo not in combinations:
                                    combinations.append(poss_combo)
print(combinations)
        
    
