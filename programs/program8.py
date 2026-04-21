# 8. WAP to find the greatest of 3 numbers entered by the user.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter two number: "))
num3 = float(input("Enter three number: "))

if(num1 >= num2 and num1 >= num3):
    print("num 1 is grater", num1)
elif(num2 >= num3):
    print("num2  is grater", num2)
else:
    print("num3  is grater", num3)
 