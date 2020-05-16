#The sentence and alphabet
sentence="The quick brown fox jumps over the lazy dog."
print(sentence)
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#Makes it all lowercase
sentence=sentence.lower()
#Turns sentence into list
list1=list(sentence)

#Checks if the sentence contains every letter by comparing 2 lists
for n in list1:
    for a in alphabet:
        if n==a:
            alphabet.remove(a)

#If alphabet list is empty, all character were used
if alphabet==[]:
    print("This is a PANGRAM!!!!")
#If not, prints whats remaining
else:
    print("NOT PANGRAM")
    print("It's missing:")
    print(alphabet)

'''”The quick brown fox jumps over the lazy dog” features all 26 English-language letters in it.
Your goal is to implement a program that takes a series of strings (one per line) and prints either True (the given string is a pangram), or False if it is not.

PLEASE ENSURE COMMENTS & VALIDATION ARE DONE TO THIS PLEASE. SEVERAL SUBMISSIONS ARE LACKING THESE'''