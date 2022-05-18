## Harshad NUmber : A number divisible by the sum of its digits.
## 156,200,180,36

def harshad(num):
    n=num
    sum=0
    while n>0:
        r=n%10
        sum=sum+r
        n=n//10
    if num%sum==0:
        print(num, "is harshad number")
    else:
        print(num,"is not harshad number")
num=int(input("enter number:"))
harshad(num)