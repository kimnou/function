##Q10.Create a function that takes 2 positive integers in form of a string
## as an input, and outputs the sum (also as a string):
## "4",  "5" --> "9"
## "34", "5" --> "39"

def sum(a,b):
    total=int(a)+int(b)
    print("'",total,"'")
a=input("enter integer string:")
b=input("enter integer string:")
# sum("2","3")
sum(a,b)

