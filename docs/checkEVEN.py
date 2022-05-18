## Q13.Write a function to check if a number is even or not.

def even(number):
    if number%2==0:
        print(number,"is even")
    else:
        print(number,"is not even")
number=int(input("enter number:-"))
even(number)