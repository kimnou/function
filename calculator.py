# def sum(a,b):
#     add=a+b
#     return add
# def diff(c,d):
#     sub=c-d
#     return sub
# def product(e,f):
#     multiply=e*f
#     return multiply
# def div(g,h):
#     divide=g/h
#     return(divide)
# print(div(5,10))
# print(diff(5,10))
# print(sum(5,10))
# print(product(5,10))



# def total(num1,num2):
#     add=num1+num2
#     return add
# def diff(num1,num2):
#     sub=num1-num2
#     return sub
# def product(num1,num2):
#     multiply=num1*num2
#     return multiply
# def div(num1,num2):
#     divide=num1/num2
#     return divide
# def op():
#     operator=input("enter operator:")
#     if operator=="add":
#         print(total(num1,num2))
#     elif operator=="subtract":
#         print(diff(num1,num2))
#     elif operator=="multiply":
#         print(product(num1,num2))
#     elif operator=="divide":
#         print(div(num1,num2))
# num1=int(input("enter first num:"))
# num2=int(input("enter second num:"))
# op()       


def calculator(op):
    if op=="+":
        result=add(num1,num2)
    elif op=="-":
        result=sub(num1,num2)
    elif op=="*":
        result=product(num1,num2)
    elif op=="/":
        result=divide(num1,num2)
    elif op=="%":
        result=mod(num1,num2)
    print(result)
def add(num1,num2):
    sum=num1+num2
    return sum
def sub(num1,num2):
    diff=num1-num2
    return diff
def product(num1,num2):
    multiply=num1*num2
    return multiply
def divide(num1,num2):
    division=num1,num2
    return division
def float(num1,num2):
    floor_div=num1//num2
    return floor_div
def mod(num1,num2):
    modulus=num1%num2
    return modulus
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
op=input("enter operator:")
calculator(op)