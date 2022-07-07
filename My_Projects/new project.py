Name=input("\nEnter your name : ")
Age=int(input("Enter your age : "))
Hobby=input("Enter your hobby : ")
Add=input("Enter your address : ")
if (Age>=18):
    print("You are Eligible for Job")
    print("what would you like get into? ")
    print("HCL")
    print("Microsoft")
    print("Google")
    print("Facebook")
    Company_Name=input("Name your company where you want to work :")
    if (Company_Name=="HCL"):
        print("What is fullform of CPU")
        Answer=input("Enter your answer")
        if(Answer=="Central processing Unit"):
            print(f"CONGRATULATIONS \n You are Eligible for Job \n your name is {Name} \n your age is{Age} your hobby is {Hobby}")
        else:
            print("You are not Eligible for Job")
        
    if (Company_Name=="Microsoft"):
        print("What is known as brain of computer")
        Answer=input("Enter your answer")
        if(Answer=="CPU"):
            print("fCONGRATULATIONS \n You are Eligible for Job \n your name is {Name} \n your age is{Age} your hobby is {Hobby}")
        else:
            print("You are not Eligible for Job")
        
    if (Company_Name=="Google"):
        print("What is spelling of Apple")
        Answer=input("Enter your answer")
        if(Answer=="Apple"):
            print(f"CONGRATULATIONS \n You are Eligible for Job \n your name is {Name} \n your age is{Age} your hobby is {Hobby}")
        else:
            print("You are not Eligible for Job")
        
    if (Company_Name=="Facebook"):
        print("What is spelling of Google")
        Answer=input("Enter your answer")
        if(Answer=="Google"):
            print(f"CONGRATULATIONS \n You are Eligible for Job \n your name is {Name} \n your age is {Age} \n your hobby is {Hobby}")
        else:
            print("You are not Eligible for Job")
else:
    print("You are not Eligible for Job")     
        
    
    
