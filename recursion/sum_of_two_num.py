def sum(num1,num2):
    if num2==0:
        return num1
    elif num1==0:
        return num2
    else:
        return sum(num1, num2-1)+1
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
print(sum(num1,num2))