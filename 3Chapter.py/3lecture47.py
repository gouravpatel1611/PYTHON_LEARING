# while True:
    # user_age=int(input("Enter your age"))
    # if user_age in range(0,3):
    #     print("You can enter free")
    # elif user_age in range(4,10):
    #     print("your fees is 150")
    # elif user_age in range(11,60):
    #     print("your fees is 250")
    # elif user_age>=60:
    #     print("your age is 200")            

                  
while True:
    user_age=int(input("Enter your age"))
    if 1<=user_age<3:
     print("You can enter free")
    elif 4<user_age<10:
        print("your fees is 150")
    elif 11<user_age<60:
            print("your fees is 250")
    elif user_age>=60:
            print("your age is 200") 
    elif user_age<=0:
        print("you can't enter")                   

