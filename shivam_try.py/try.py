if a==b==c:
  print( "all are equles")
elif a==b:
    if a>c:
      print( "a & b are equales & greater than c ")
    else:
      print( "c is greater")
elif a==c:
    if a>b:
      print( " a & c is greater")
    else:
      print( "b is greater")
elif b==c:
    if b>a:
      print("b & c is greater")
    else:
      print( "a is greater" )  
elif a>b and a>c:
  print( "a is greater")
elif b>a and b>c:
  print("b is greater")
else:
  print( "c is greater" )    