def subtraction(num1,num2):
    if num2==0:
        return num1
    return subtraction(num1-1,num2-1)
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
print(subtraction(num1,num2))