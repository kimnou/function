# def list(numbers):
#     i=0
#     a=[]
#     while i<len(numbers):
#         if numbers[i]%3==0 or numbers[i]%8==0:
#             a.append(numbers[i])
#         i+=1
#     print(a)
# numbers=[1,2,5,6,24,40,23,3]
# list(numbers) 



# list=["hello","world","this","is","great"]
# i=0
# a=''
# while i<len(list):
#     a+=list[i]+" "
#     i+=1
# print("'"+a+"'")
# while i<len(list):
#     a=list[i]
#     i+=1
#     print(a,end=" ")



# def multiples(num1,num2):
#     if num2>0 and num1>0:
#         i=0
#         sum=0
#         while i<=num2:
#             if i%num1==0:
#                 sum=sum+i
#             i+=1
#         print(sum)
#     else:
#         print("invalid")
# num1=int(input("enter number:"))
# num2=int(input("enter number:"))
# multiples(num1,num2)



# def multiples(num1,num2):
#     if num2<0 or num1<0:
#         print("invalid")
#     else:
#         i=0
#         sum=0
#         while i<=num2:
#             if i%num1==0:
#                 sum=sum+i
#             i+=1
#         print(sum)
# num1=int(input("enter number:"))
# num2=int(input("enter number:"))
# multiples(num1,num2)


# def func(list1,list2):
#     i=0
#     j=0
#     b=[]
#     d=[]
#     while i<len(list1) and j<len(list2):
#         a=list1[i]+list2[j]
#         b.append(a)
#         i+=1
#         j+=1
#     c=" ".join(b)
#     d.append(c)
#     print(d)
#     print(b)
# list1=["m","na","i","ki"]
# list2=["y","me","s","m"]
# func(list1,list2)


# def sum_number(list):
#     i=1
#     n=0
#     new_list=[]
#     while i<=len(list):
#         n=n+i
#         new_list.append(n)
#         i+=1
#     print(new_list)
# list=[1,2,3,4,5]
# sum_number(list)


# i=1
# num=10
# a=[]
# while i<=num:
#     n=int(input("enter number:"))
#     i+=1
#     a.append(n)
#     max=a[0]
#     min=a[0]
#     for j in a:
#         if max<j:
#             max=j
#         if min>j:
#             min=j
# print("largest number is:",max)
# print("smallest number is:",min)


# def func(list):
#     i=0
#     a=[]
#     while i<len(list):
#         if type(list[i])==type([]):
#             j=0
#             while j<len(list[i]):
#                 a.append(list[i][j])
#                 j+=1
#         else:
#             a.append(list[i])
#         i+=1
#     print(a)
# list=[1,2,[3,4,[5,6],7,8,[9,[10]]]]
# func(list)



# def remainder(a,b):
#     r=0
#     if a>b:
#         r=a%b
#     elif a<b:
#         r=b%a
#     print(r)
# a=int(input("enter number:"))
# b=int(input("enter number:"))
# remainder(a,b)


# a=[1,2,3,[4,[5,6,[7]],8],[9]]
# b=[]
# def fun(a):
#     for i in a:
#         if type(i)==list:
#             fun(i)
#         else:
#             b.append(i)
# # print(a)
# fun(a)
# print(b)



# def items(a):
#     new_list=[]
#     i=0
#     j=0
#     while i<len(a):
#         if type(a[i]) is list:
#             new_list.extend(a[i])
#         else:
#             new_list.append(a[i])
#         i+=1
#     print(new_list)
# a=[1,2,[3,4],[5,6],7,8,[9,10]]
# # a=[1,2,[3,4,[5,6],7,8,[9,[10]]]]
# items(a) 



# def first(a):
#     def second(b):
#         return a+b
#     b=int(input("enter number:"))
#     return second(b)
# a=int(input("enter number:"))
# print(first(a))


def first():
    def second():
        i=1
        sum=0
        while i<=10:
            sum=sum+1
            i+=1
        return sum+1
    return second()
print(first())
    



# def first(num1,num2):
#     a=num1+num2
#     return a
# def second(num1,num2):
#     b=num1/num2
#     return b
# def third(num1,num2):
#     c=num1%num2
#     return c
# def main(operator):
#     if operator=="+":
#         print(first(num1,num2))
#     elif operator=="/":
#         print(second(num1,num2))
#     elif operator=="%":
#         print(third(num1,num2))
#     else:
#         print("operator not found")
# num1=int(input("enter first number:"))
# num2=int(input("enter second number:"))
# operator=input("enter operator:")
# main(operator)


# def first():

# def foo(a, b, c):
#     pass
# def bar(a, b, c):
#     pass
# # test code
# if foo(1, 2, 3, 4) == 1:
#     print("Good.")
# if foo(1, 2, 3, 4, 5) == 2:
#     print("Better.")
# if bar(1, 2, 3, magicnumber=6) == False:
#     print("Great.")
# if bar(1, 2, 3, magicnumber=7) == True:
#     print("Awesome!")

# def first(list):
#     i=0
#     sum=0
#     while i<len(list):
#         sum=sum+list[i]
#         i+=1
#     return sum
# def second(list):
#     i=0
#     even=[]
#     while i<len(list):
#         if list[i]%2==0:
#             even.append(list[i])
#         i+=1
#     return even
# def third(list):
#     if 10 in list:
#         return "ten"
# def main(x):
#     if x==1:
#         print(first(list))
#     elif x==2:
#         print(second(list))
#     elif x==3:
#         print(third(list))
# list=[1,2,3,4,5,6,7,8,9,10]
# x=int(input("enter number:"))
# main(x)



# def square(num):
#     result=num*num
#     return result
# def cube(num):
#     result=num*num*num
#     return result
# def main(x):
#     if x==2:
#         print(square(num))
#     elif x==3:
#         print(cube(num))
# num=int(input("enter number:"))
# x=int(input("enter 2 0r 3:"))
# main(x)



# def square(num):
#     a=num*num
#     return a
# def cube(num):
#     b=num*num*num
#     return b
# def main():
#     c=square(num)+cube(num)
#     return c
# num=int(input("enter number:"))
# print(main())


# def square(num):
#     a=num*num
#     return a
# def cube(num):
#     b=num*num*num
#     return b
# def main():
#     print("square of given number:",square(num))
#     print("cube of given number:",cube(num))
# num=int(input("enter number:"))
# main()

