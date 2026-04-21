# Print the multiplication table of a number `n`.

num = int(input("Enter the number: "))

cnt = 1

while cnt <= 10:
    print(f"{num} X {cnt} = {num*cnt}")
    cnt+=1