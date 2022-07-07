while True :
    Number=input("Enter set of no." )
    # int(N2umber[i])
    total=0
    i=0
    while i<len(Number):
        total+=int(Number[i])
        i+=1
    print(total)
