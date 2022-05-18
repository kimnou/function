#Define a function which takes one argument which is the limit upto which the
#  function has to print the numbers and their label(even or odd).
def even_and_odd(n):
    i=0
    while i<=n:
        if i%2==0:
            print(i,"even")
        else:
            print(i,"odd")
        i=i+1
n=int(input("enter the number:"))
even_and_odd(n)