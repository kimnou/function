## Write a Python function to calculate the factorial of a number.
# The function accepts the number as an argument

## The factorial of a number is the product of all the integers 
## from 1 to that number. 
## For example, the factorial of 6 is 1*2*3*4*5*6 = 720 .

def factorial(number):
    i=1
    fac=1
    while i<=number:
        fac=fac*i
        i+=1
    print(fac)
number=int(input("enter number:"))
factorial(number)
