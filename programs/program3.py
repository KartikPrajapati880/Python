# 3. WAP to input 2 floating numbers and print their average

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

def average(x, y):
    return (x + y) / 2

print("Average of two numbers: ", average(num1, num2))