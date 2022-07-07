while True:
    name=input("Enter your good name:>")
    age=int(input("Enetr your age:>"))
    if age>=14 and (name[0]== "a" or name[0]=="A"):
     print("you can watch the movie")
    else:
        print("sorry, you can't atch the movie")