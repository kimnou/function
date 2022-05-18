## First take a password string input from the user.
## It must follow the following rules to set strong password
## 1.Minimum length should be atleast 6
## 2.Maximum length not to exceed 16
## 3.Must have at least one dollar sign ($)
## 4.Password must contain atleast one capital and one small letter
## If the password is following this rule then print 
# "strong password", otherwise type "weak password"

def strong_password(password):
    digit='0123456789'
    upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower='abcdefghijklmnopqrstuvwxyz'
    special_char='@#$_'
    sum=0
    a=0
    x=0
    y=0
    z=0
    if len(password)>6 or len(password)<=16:
        i=0
        while i<(len(password)):
            if password[i] in digit:
                x=1
            elif password[i] in upper:
                y=1
            elif password[i] in lower:
                z=1
            elif password[i] in special_char:
                a=1
            i=i+1
        sum=x+y+z+a
        if sum<4:
            print("password should have atleast one capital,one small,one special character and one digit ")
        else:
            print("strong password ")
password=input("enter the password:-")
strong_password(password)