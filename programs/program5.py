# 5. WAP to input user's first name and print it's length

firstName = input("Enter the first name: ")
print("Length of first name is: ", len(firstName))

# another approch via function

def lengthOfFirstName(str):
    return len(str)

print("Length of first name is: ", lengthOfFirstName(firstName))
