# def greet():
#     print("hello")
#     greet()
# greet()

# import sys
# sys.setrecursionlimit(100)
# i=0
# def greet():
#     global i
#     i+=1
#     print(i,"hello")
#     greet()
# greet()


# def greet():
#     i=0
#     while i<100:
#         i+=1
#         print(i,"hello")
#         greet()
# greet()


#================factorial=================

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return (n*factorial(n-1))
# n=int(input("enter number:"))
# res=factorial(n)
# print(res)


#==============even_odd====================
# def even_odd(num):
#     sum=0
#     modulus=0
#     while num!=0 :
#         modulus=num%10
#         sum+=modulus
#         num//=10
#     if sum%2==0:
#         return sum,"even"
#     else:
#         return sum,"odd"
# num=int(input("enter number"))
# print(even_odd(num))


def even(n):
    if n>9:
        i=0
        sum=0
        re=0
        while i<n:
            re=n%10
            sum=sum+re
            n=n//10
        return even(sum)
    else:
        if n%2==0:
            print(n,"even")
        else:
            print(n,"odd")
n=int(input("enter the number:"))
even(n)




# def recursivesum(num):
#     if num>9:
#         i=0
#         sum=0
#         while i<=num:
#             r=num%10
#             sum=sum+r
#             num=num//10
#         return recursivesum(sum)
#     else:
#         return num
# num=int(input("enter number:"))
# print(recursivesum(num))

