def SumOfNaturalNumber(n):
    if n>0:
        return n+SumOfNaturalNumber(n-1)
    else:
        return n
n=int(input("enter number:"))
print(SumOfNaturalNumber(n))