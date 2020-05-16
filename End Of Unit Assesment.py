print("Hi, here is a few questions about python")
incorrect
score=0
attemps<3
answer1=input("What is the capital of Spain: n/a:London n/b:Madrid n/c:New York")
if answer1 == "Madrid":
    print("Correct")
    score=score + 1
    else
    incorrect=incorrect+1
    answer15=input(" WRONG, TRY AGAIN. What is the capital of Spain: n/a:London n/b:Madrid n/c:New York")
    if answer15 == "Madrid":
        print("Correct") score=score+1
    else
    print("Incorrect, next question") incorrect=incorrect+1
answer2=input("What is 6*3")
if answer2 == "18":
    print("Correct")
    score=score + 1
    else
   incorrect=incorrect+1
   answer25=input(" WRONG, TRY AGAIN. What is 6*3")
                  if answer25 == "18":
    print("Correct") score=score+1
    else
    print("Incorrect, next question") incorrect=incorrect+1
answer3=input("What is 100-10?")
if answer3 == "90":
    print("Correct")
    score=score + 1
    else
   incorrect=incorrect+1
   answer35=input(" WRONG, TRY AGAIN. What is 100-10?")
                  if answer35 == "90":
    print("Correct") score=score+1
    else
    print("Incorrect, next question") incorrect=incorrect+1
answer4=input("What is 10*11?")
if answer4 == "110":
    print("Correct")
    score=score + 1
    else
   incorrect=incorrect+1
   answer45=input(" WRONG, TRY AGAIN. What is 10*11?")
                  if answer45 == "110":
    print("Correct") score=score+1
    else
    print("Incorrect, next question") incorrect=incorrect+1
answer5=input("What is 120-12?")
if answer5 == "108":
    print("Correct")
    score=score + 1
    else
   incorrect=incorrect+1
   answer55=input(" WRONG, TRY AGAIN. What is 120-12?")
                  if answer55 == "108":
    print("Correct") score=score+1
    else
    print("Incorrect, Now YOUR SCORE!") incorrect=incorrect+1
print(score)
print(incorrect)
