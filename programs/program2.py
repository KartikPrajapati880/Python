# 2. WAP to input side of a square and print its area
side = float(input("Enter the side of a square:"))

def areaOfSquare1(s):
    return s * s

def areaOfSquare2(s): # Using exponentiation operator
    return s ** 2

print("Area of the square is: ", areaOfSquare1(side))
print("Area of the square is: ", areaOfSquare2(side))
