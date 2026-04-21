# Write a function to print the elements of a list in a single line. (`list` is the parameter)
lst = [1, 2, 3, 4, 5, 9, 12, 30]

def pri_el(list):
    
    for el in list:
        print("Element is: ", el)

pri_el(lst)