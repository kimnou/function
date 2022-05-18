def squares(number):
    i=1
    while i<=number:
        print(i,":",i**2,end=", ")
        i+=1
number=int(input("enter number:"))
squares(number)
