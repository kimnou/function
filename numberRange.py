##Write a Python function to check whether a number falls in a given range.

# def check_range(number):
#     if number in range(5,10):
#         print(number,"is in given range")
#     else:
#         print(number,"is not in given range")
# number=int(input("enter number:"))
# check_range(number)


# def check_range(first,last,number):
#     if number in range(first,last):
#         print(number,"is in range")
#     else:
#         print(number,"is not in range")
# first=int(input("enter start range:"))
# last=int(input("enter end range:"))
# number=int(input("enter the number:"))
# check_range(first,last,number)

def check_range(first,last,number):
    if number>=first and number<=last:
        print(number,"is in range")
    else:
        print(number,"is not in range")
first=int(input("enter start range:"))
last=int(input("enter end range:"))
number=int(input("enter the number:"))
check_range(first,last,number)