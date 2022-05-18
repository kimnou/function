## Write a Python function that checks 
## whether a passed string is palindrome or not

def palindrome(string):
    string_list=list(string)
    i=-1
    a=[]
    while i>=-len(string):
        a.append(string[i])
        i-=1
    if string_list==a:
        return True
    else:
        return False
string=input("enter string:")
print(palindrome(string))


  