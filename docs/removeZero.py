## Q12.Numbers ending with zeros are boring.
## They might be fun in your world, but not here.
## Get rid of them. Only the ending ones.
##1450 -> 145
##960000 -> 96
##1050 -> 105
##-1050 -> -105

def removeZero(number):
    if number%10==0:
        print(number//10)
    else:
        print("number does not end with zero")
number=int(input("enter number:-"))
removeZero(number)
