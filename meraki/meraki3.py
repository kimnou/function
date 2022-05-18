# def students(name):
#     for i in name:
#         print(i)
# name=["jen","hoz","afgan"]
# students(name)


# def students(*name):
#     for i in name:
#         print(i)
# students("jen","hoz","afgan")


# def isGreaterThan20(a,b):
#     print(a,b)
# a=20
# b=50
# isGreaterThan20(a,b)


# def isGreaterThan20():
#     for i in range(20,50):
#         print(i)
# isGreaterThan20()


# def isGreaterThan20(name, marks="20"):
#     print(name,"got", marks," in examination")
# isGreaterThan20("hannah")
# isGreaterThan20("jen","45")

def isGreaterthan20(a,b=20):
    x=a>b
    print(x)
isGreaterthan20(30)