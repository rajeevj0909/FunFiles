valid_pswd = False
while valid_pswd == False:
    user_pswd = input("Please enter a password")
    if len(user_pswd) <+ 6:
        print("This password is too small")
    elif len(user_pswd) > 12:
        print("This password is too big")
    else:
        print("This password is acceptable")
        valid_pswd = True        
upper_flag = 0
lower_flag = 0
num_flag = 0
for char in user_pswd:
    if char.isupper():
        upper_flag = 1
    elif char.islower():
        lower_flag = 1
    elif char.isdigit():
        num_flag = 1
total = upper_flag + lower_flag + num_flag
if total == 3:
    print("This password has been rated 'Strong'")
elif total == 2:
    print("This password has been rated 'Medium'")
else:
    print("This password has been rated 'Weak'")
        
