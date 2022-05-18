## Write a Python function to check whether a number is perfect or not. Go to the editor
## Perfect Number : A positive integer that is equal to the sum of 
## its proper positive divisors, excluding the number itself 
## perfect numbers are 6,28,496,8128

def perfect(number):
    i=1
    sum=0
    while i<number:
        if number%i==0:
            sum=sum+i
        i+=1
        return perfect(sum)
    if number==sum:
        print(number,"is perfect number")
    else:
        print(number,"is not perfect number")
number=int(input("enter number:"))
perfect(number)
