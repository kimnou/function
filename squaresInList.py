## Write a Python function to create and print a list where the values are 
# square of numbers between 1 and 30 (both included).

def squares(number):
    i=1
    list=[]
    while i<=number:
        list.append(i**2)
        i+=1
    print(list)
# number=int(input("enter number:"))
squares(30)