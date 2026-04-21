# Print the multiplication table of a number `n` using `range()`.

num = int(input("Enter number: "))

for el in range(1, 11):
    print(f"{num} X {el} = {num*el}")