def greater(a,b):
    if a>b:
        return "a is greater"
    elif b>a:
        return "b is greater"
    else:
        return "all are equale"
num1=int(input("Enetr first number"))
num2=int(input("Enter second number"))
print(greater(num1, num2))    