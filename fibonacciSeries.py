## Fibonacci Series : a series in which each number is equal to 
## the sum of the preceding two numbers.(first two are 0 and 1 by default)

def fibonacci_series(num):
    a,b=0,1
    i=0
    while i<num:
        print(a)
        i+=1
        a,b=b,a+b
num=int(input("enter number:"))
fibonacci_series(num)