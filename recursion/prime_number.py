def CheckPrime(i,num):
    if num==i:
        return 0
    else:
        if(num%i==0):
            return 1
        else:
            return CheckPrime(i+1,num)
num=int(input("Enter your Number:"))
if(CheckPrime(2,num)==0):
    print("It is a Prime Number.")
else:
    print("It is not a Prime Number.")