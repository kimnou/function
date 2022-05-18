first=input("enter string:")
second=input("enter string:")
def string(first,second):
    if len(first)>len(second):
        print(first)
    elif len(second)>len(first):
        print(second)
    elif len(first)==len(second):
        print(first,"\n",second)
string(first,second)