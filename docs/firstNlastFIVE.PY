#Write a Python program to generate and print a list of first and last 5 
# elements where the values are square of numbers between 1 and 30 (both included).
#Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).

def list(number):
    i=1
    square=0
    a=[]
    b=[]
    while i<=number:
        square=i**2
        a.append(square)
        i+=1
    # print(a)
    x=(a[:5])
    y=(a[25:])
    b.append(x)
    b.append(y)
    print(b)
list(30)