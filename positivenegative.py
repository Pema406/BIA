# Objective:
# Create a program that takes in user input
# and determines if the number is positive or negative
# print: "Your number is positive" or "Your number is negative"

# If else
# print()
# input()
userinput = input('please type any number:')
userinputtyped = type(userinput)
print('The type of user input is:',userinputtyped)
userInputNumber = float(userinput)
print('The type of userInputNumber is:', type(userInputNumber))
if userInputNumber > 0:
    print('The number is positive')

if userInputNumber < 0:
    print('The number is negative')

if userInputNumber == 0:
    print('The number is zero')

