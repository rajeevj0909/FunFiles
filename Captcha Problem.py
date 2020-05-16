number=str(input("Whats your numbers"))
number1=[]
for digit in number:
    digit = int(digit)
    number1.append(digit)
print(number1)

count=1
total=0
length = len(number)
for digit in len(number1):
    if length=count:
        break
    elif number1[digit]==number1[count]:
        total=total+int(number1[count])
        count=count+1
    else:
        counter = counter + 1
if number1[length-1] == number1[0]:
        total = total + int(total[0])
print(total)

pinput = '1122'
puzzle = list(pinput)
counter = 1
answer = 0

length = len(puzzle)
for i in range(len(puzzle)):
    if length == counter:
        break
    elif puzzle[i] == puzzle[counter]:
        answer = answer + int(puzzle[counter])
        counter = counter + 1
    else:
        counter = counter + 1
if puzzle[length-1] == puzzle[0]:
        answer = answer + int(puzzle[0])
print(answer)
