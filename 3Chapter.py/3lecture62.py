while True:
    name=input("Enter your good name")
    temp_var=""
    for i in range(len(name)):
        if name[i]  not in temp_var :
        
            print(f"{name[i]} : {name.count(name[i])}")
            temp_var+=name[i]