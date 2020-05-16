import random
carry_on=True
while carry_on:
    num=random.randint(1,10)
    print(num)
    question=input("Do you want to continue? y/n")
    if question=="n":
        carry_on=False
