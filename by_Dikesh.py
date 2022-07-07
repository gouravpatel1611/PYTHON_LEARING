m1=int(input("enter a marks of student1 : "))
m2=int(input("enter a marks of student2 : "))
m3=int(input("enter a marks of student3 : "))
m4=int(input("enter a marks of student4 : "))
m5=int(input("enter a marks of student5 : "))
m6=int(input("enter a marks of student6 : "))
marks=[m1,m2,m3,m4,m5,m6]
marks.sort()
print(marks)
print(f"average of marks of all students is : {sum(marks)/2}")

    
    

        