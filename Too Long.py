def tooLong(num1):
    if len(num1)<14:
        answer="TRUE"
    else:
        answer="FALSE"
    return answer
        
num1=input("Enter the sentence.  ")
answer=tooLong(num1)
print(answer)
