while True:
    def greater(a,b,c):
        if a>b and a>c:
            return "a is greter"
        elif b>a and b>c:
            return " b is greater "  
        else:
            return " c is greater"
        a=int(input("Enter a : "))
        b=int(input("Enter b : "))
        c=int(input("Enter c : ")) 
    print(greater(num1,num2,num3))
        
    