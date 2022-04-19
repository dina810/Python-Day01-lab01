string = input("Please enter your String: ")
reversed_string = ''
for i in string:
    reversed_string = i + reversed_string
print("\nThe Original String is: ", string)
print("The Reversed String is: ", reversed_string)