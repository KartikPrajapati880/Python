# Write a function to find the factorial of a number `n`. (`n` is the parameter)

def factorial(n):
    cnt = 1
    fact = 1

    while cnt <= n:
        fact *= cnt
        cnt+=1

    print("Factorial", fact)
    
factorial(5)
