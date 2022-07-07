import random
print("welcome to ALONE NUMBER")
print("Rule:- \n 1.Enter your name \n 2.Enter your own number \n 3. if your number is equales to Alone Number you will win the game \n 4. Either you will lose the game or try again ")

Name=input("Enter your name: ")
i=random.randint(1,100)
a=0
while (1>0):
    a+=1
    Number=int(input("Guess  the Alone Number : "))
    if (i==Number):
        
        
        print(f"Congratulation {Name} you have won the game")
        print(f"You won this match  at :>{a}  attempts")
        
        print("\n")
    if(i>Number):
        print("your number is too small \n try again")
    if(i<Number):
        print("Sorry, your number is too big\n try again")