#Write a program that serves as a basic calculator.
#It asks for twonumbers, then 
#it asks for an operator.
#Gracefully deal with input that doesn't cleanly convert to numbers.
#Deal with division by zero errors.

num1 = int(input('Enter First Number:'))
operator = input('Enter the Operator:')
num2 = int(input('Enter Second Number:'))


if operator == '+':
    print(num1 + num2)

elif operator == '-':
    print(num1 - num2)

elif operator == '*':
    print(num1 * num2)

elif operator == '/':
    if num2 == 0:
        print("Value error")
    else:
        print(num1/num2)


else:
    print("Invalid Operator")

