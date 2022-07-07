import random
print("Welcome to gamer Zone")
name=input("What is your good name:>")
print(f"Hello {name},are you intteligent?, I just want to check your presence of mind")
# alone= int("56")
alone=random.randint(0,100)
while (11>0):


    number=int(input("Guess the alone number"))
    if alone == number :
        print("you are intelligent")
    if alone>number :
        print(" number is to small than number")
    if alone<number:
            print("number is  too big than number")
            
        


