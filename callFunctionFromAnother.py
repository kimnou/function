def list(num):
    i=1
    b=[]
    while i<=num:
        a=i
        b.append(a)
        i+=1
    return b
def even_odd(b):
    i=0
    while i<len(b):
        if b[i]%2==0:
            print(b[i],"EVEN")
        else:
            print(b[i],"ODD")
        i+=1
num=int(input("enter number:"))
print(list(num))
even_odd(list(num))
