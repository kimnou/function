## Q2.Write a Python function to find the Max of three numbers.

def maximum(num1,num2,num3):
    if num1>num2 and num2>=num3:
        print(num1,"is maximum")
    elif num2>num1 and num1>=num3:
        print(num2,"is maximum")
    else:
        print(num3,"is maximum")
num1=int(input("enter first number:-"))
num2=int(input("enter second number:-"))
num3=int(input("enter third number:-"))
maximum(num1,num2,num3)