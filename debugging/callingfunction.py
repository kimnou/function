# def fun2():
#     print ("Called by fun1()")
# def fun1():                          # function definition
#     print ("Called by main function")
#     fun2()                              # calling fun2() from fun1()
# fun1()


# def add_1(a):
#     return(a + 1)
# def add_2(c):
#     return(c + 2)
# output = add_1(add_2(0))
# print(output)


# def repeat(function, n):
#     return function(n)
# def square(n):
#     return n ** 2
# output = repeat(square, 3)
# print(output)


# def outside():
#     print("im outside")
#     def inside():
#         print("am inside")
#     inside()
# outside()


def outside():
    print("im outside")
def inside():
    print("am inside")
    outside()
inside()
