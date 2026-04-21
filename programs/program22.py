# Search for a number `x` in the tuple using a loop:
# `(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

tpl = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

num = int(input("Enter the number: "))

idx = 0
while idx < len(tpl):
    if(num == tpl[idx]):
        print("Number found: ", num)
        break
    
    idx += 1