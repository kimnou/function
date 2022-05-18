#Write a Python program to reverse a string.
#Sample String : "1234abcd"
#Output : "dcba4321".

# def reverse(string):
#     print(string[::-1])
# # string=input("enter string:-")
# string=["1234abcd"]
# reverse(string)

# def reverse(string):
#     i=-1
#     while i>=-len(string):
#         print(string[i],end="")
#         i-=1
# string=input("enter string:")
# reverse(string)


def reverse(string):
    l=len(string)-1
    i=l
    while i>=0:
        print(string[i],end="")
        i-=1
string=input("enter string:")
reverse(string)