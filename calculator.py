"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
print('welcome to the calculator app')
user_input = input('what would you like to calculate: ')
user_input = user_input.split(' ')

num1 = int(user_input[0])
num2 = int(user_input[2])
if user_input[1] == '+':
    print(add(num1, num2))
if user_input[1] == '-':
    print(subtract(num1, num2))
if user_input[1] == '*':
    print(multiply(num1, num2))
if user_input[1] == '/':
    print(divide(num1, num2))
if user_input[1] == 'square':
    print(square(num1, num2))
if user_input[1] == 'cube':
    print(cube(num1, num2))
if user_input[1] == 'pow':
    print(power(num1, num2))
if user_input[1] == 'mod':
    print(mod(num1, num2))
