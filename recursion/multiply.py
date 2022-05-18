def multiplication(num1,num2):
    if num1<num2:
        return multiplication(num2, num1)
    elif num2!=0:
        return num1 + multiplication(num1, num2 - 1)
    else:
        return 0
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
print(multiplication(num1,num2))