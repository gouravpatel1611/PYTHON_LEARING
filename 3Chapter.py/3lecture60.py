
sum=0
while True:
    n=int(input("Enter last number"))
    for i in range(1,n+1):
     sum+=i
    print(f" {i} :{sum}")
    i+=1