Name="Shivanishivam"
# print('S :',Name.count("S"))
# print('h :',Name.count("h"))
# print('i :',Name.count("i"))
# print('v :',Name.count("v"))
# print('a :',Name.count("a"))
# print('m :',Name.count("m"))
# print('  :',Name.count(" "))
# print('s :',Name.count("s"))

temp_var = []
i= 0
while i<len(Name):
    if Name[i] not in temp_var :
        temp_var.append( Name[i])
        print(temp_var)
        print(f"{Name[i]}: {Name.count(Name[i])}")
    i+=1