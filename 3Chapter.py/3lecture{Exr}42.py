
Winning_number = 43
while True:
    number = int(input("guess a number"))
    if Winning_number==number:
        print("YOU WIN!!")
    elif  Winning_number>number: 
        print("too low")
    elif    Winning_number<number:
        print("too big")    
          
