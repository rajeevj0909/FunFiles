hash1="45F29576330664B03C241376E160F6E848AA443C5075930F2F3A19813AA54D75"
hash2="CE64FA43F9D9EBE9B46550431A61062912C30B444A3A7D06EBD08A6857160897"

list1=list(hash1)
list2=list(hash2)

counter=0
total=0
for character in hash1:
    if list1[counter]==list2[counter]:
       print(counter," is ",character)
       total+=1
    counter+=1

print("There are ",total)
