# 15. You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
#    "python", “java", “C++", “python", “javascript", “java", “python", “java", “C++", “C"

list = ["python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"]
newList = set(list)
print(len(newList))