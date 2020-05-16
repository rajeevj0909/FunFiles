password=input(str("Whats the password? "))
hashed=hash(password)

print("You typed in ", password)
print("Your hashed password is ", hashed)
guesses=0

def attempts(hashed,guesses):
   attempt=input(str("\nTo login, please enter your password: "))
   hashetAttempt=hash(attempt)
   print("Hashed attempt is: ", hashetAttempt)
   
   if hashed==hashetAttempt:
      print("ACCESS GRANTED")
   else:
      print("ACCESS DENIED")
      guesses=guesses+1
      if guesses<3:
         attempts(hashed,guesses)

   
attempts(hashed,guesses)
