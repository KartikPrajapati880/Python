# 16. WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}

m1 = int(input("Enter the chem subject marks: "))
m2 = int(input("Enter the maths subject marks: "))
m3 = int(input("Enter the physic subject marks: "))

marks.update({"chem": m1})
marks.update({"maths": m2})
marks.update({"physic": m3})

print(marks)