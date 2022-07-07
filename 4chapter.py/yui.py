# def is_palindrom(a):

#  b=a[::-1]
#  if a==b:
#    return True
#  else :
#     return False
# a=input("Enter any word : ")

# print(is_palindrom(a))   


def is_palindrom(a):
 if a == a[::-1]:
   return True
 else:
  return False
# a=input("Enter any word : ")
print(is_palindrom("madam"))             