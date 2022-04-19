import re
my_name = input("plz enter your name: ")
my_email = input("plz enter your email: ")
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
if not my_name:
    print("empty name ")
elif my_name.isdigit():
    print("invalid ")
else:
  print("your name is: " ,my_name )
if(re.fullmatch(regex, my_email)):
    print("your name is: "  ,my_email)
else:
    print("Invalid Email")
 

