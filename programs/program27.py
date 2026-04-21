# Write a program to find the factorial of a number `n` using a `for` loop.
# Factorial 1 * 2 * 3 * 4 * 5 = 120

num = int(input("Enter the number: "))
fact = 1

for el in range(1, (num+1)):
    fact *= el

print("Fact: ", fact) 
