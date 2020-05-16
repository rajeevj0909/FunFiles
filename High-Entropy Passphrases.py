file=open("High-Entropy Passphrases.txt","r")
count=0
total=0
duplicates=[]
word=""
duplo=False
for line in file:
  count=count+1
  for letter in line:
    if letter=="\n" or letter==" ":
      if word not in duplicates:
        duplicates.append(word)
      else:
        duplo=True
      word=""
    else:
      word=word+letter
  if duplo==True:
    total=total+1
    duplo=False
    duplicates.append("*******************")
  print(duplicates)
  duplicates=[]
       
print("Lines in file")
print(count)
print("Total lines that have duplicates")
print(total)
final=count-total
print("Total lines that don't have duplicates")
print(final)
file.close()



