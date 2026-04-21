# Write a program to find the sum of first `n` numbers using a `while` loop.
# Sum 1 + 2 + 3 + 4 + 5 = 15


num = int(input("Enter the number: "))
cnt = 1
sum = 0
while cnt <= num:
    sum += cnt
    cnt += 1

print("Sum: ", sum)