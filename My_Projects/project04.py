import random
print("Welcom to $ Rock paper Scissor $ ")

print("Rule:- \n 1.Rock= 👊 = 0 \n 2.Paper= ✋ = 1 \n 3.Scissor= ✂ =2 \n 4.Rock=Rock=Ty\n Rock=Paper=Paper.W \nRock=Scissor=Scissor.W")
print("5.Paper=paper=Ty \n Paper=Rock=Paper.W \n Paper=Scissor=Scissor.W ")
print("6. Scissor=Scissor=Ty \n Scissor=Rock=Rock.W \n Scissor=Paper=Scissor.W")
Name=input("\U0001F604 Enter your Good name \U0001F604 :-  ")



while True:
    i=str(random.randint(0,2)) 
    Number=input(" \U0001F604 Enter your choice \U0001F604 :-")

    if (i=="0" and Number =="0" ):
        print(f"Rock=Rock:- This match has tied \n Try Again")
        
    if (i=="0" and Number=="1"):
        print(f"Rock=Paper :- Congratulations \U0001F490\U0001F490\U0001F490 {Name} you are winner")      
        
    if (i=="0" and Number=="2"):
        print(f"Rock=Scissor :- Sorry \U0001F61E \U0001F61E \U0001F61E {Name} You have lost the match")
        
    if (i=="1" and Number=="1"):
        print("Paper=Paper :-This match has tied \n Try Again")
        
    if(i=="1" and Number=="0"):
        print(f"Paper=Rock :-  Sorry \U0001F61E \U0001F61E \U0001F61E {Name} You have lost the match")
          
    if(i=="1" and Number=="2"):
        print(f"Paper=Scissor :- Congratulations \U0001F490\U0001F490\U0001F490 {Name} you are winner")
        
    if(i=="2" and Number=="2"):
        print("Scissor=Scissor :-This match has tied \n Try Again")
        
    if(i=="2" and Number=="0"):
        print(f"Scissor= Rock:-  Congratulations \U0001F490\U0001F490\U0001F490 {Name} you are winner")
        
    if(i=="2" and Number=="1"):
        print(f"Scissor=Rock:- Sorry \U0001F61E \U0001F61E \U0001F61E {Name} You have lost the match")
        