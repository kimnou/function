def FibonacciSeries(n):
    if n==0:
        return 0
    elif(n==1):
        return 1
    else:
        return FibonacciSeries(n-1)+FibonacciSeries(n-2)
n=int(input("enter number limit:"))
for i in range(0,n):
    print(FibonacciSeries(i),end=" ")