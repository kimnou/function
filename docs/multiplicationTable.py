## Q16.Print multiplication table of 12 using function.

def table(num):
    i=1
    while i<=10:
        print(num,"*",i,"=",num*i)
        i+=1
table(12)