# A calculator will go here.

first_num = input("Enter your first number: ")

while not first_num.isnumeric():
    first_num = input("That's not a number. Try again: ")

operator = input("Enter the operation that you'd like to perform: ")

while not operator in ["*", "-", "+", "/"]:
    operator = input("Sorry, I don't recognize that operator. Try again: ")

second_num = input("Enter the second number: ")

while not second_num.isnumeric():
    second_num = input("That's not a number. Try again: ")

