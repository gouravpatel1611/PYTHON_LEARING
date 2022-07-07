def greater_than(a,b,c):
    if a==b==c:
        return "all are equles"
    elif a==b:
        if a>c:
            return "a & b are equales & greater than c "
        else:
            return "c is greater"
    elif a==c:
        if a>b:
            return " a & c is greater"
        else:
            return "b is greater"
    elif b==c:
        if b>a:
            return"b & c is greater"
        else:
            return "a is greater"   
    elif a>b and a>c:
        return "a is greater"
    elif b>a and b>c:
        return"b is greater"
    else:
        return "c is greater"     
    
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3=int(input("Enter third number "))
print(greater_than(num1,num2,num3))
