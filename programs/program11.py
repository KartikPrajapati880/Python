# 11. WAP to check a list contain palindrom of elements [1, 2, 3, 4] [1, "abc", "abc", 1] (Hint use copy() method) 
# palindrom means if you reverse any object and it same as orignal after reversing means it's palindrom

listOne = [1, 2, 3, 4]
newListOne = listOne.copy()
newListOne.reverse()

if (newListOne == listOne):
    print("List One is Palindrom")
else:
    print("List One is not palindrom")

listTwo = [1, "abc", "abc", 1]
newListTwo = listTwo.copy()
newListTwo.reverse()

if (newListTwo == listTwo):
    print("List Two is Palindrom")
else:
    print("List Two is not palindrom")