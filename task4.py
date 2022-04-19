number=int(input("plz enter number"))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("buzz")
elif number % 5 == 0:
    print("Fizz")
else:
    print("invalid number")

