# 4. WAP to input 2 numbers, a and b print True if a is grater than or equal to b if not print False

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

def isGraterOrEqual(x, y):
    if (x >= y) :
        return True
    else:
        return False
    
print("Number 1 is grater than or qual to number 2: ", isGraterOrEqual(num1, num2))