def multiples(number):
    i=0
    sum=0
    while i<=number:
        if i%3==0 or i%5==0:
            sum=sum+i
        i+=1
    print(sum)
number=int(input("enter number:"))
multiples(number)

