## Write a loop to print all the numbers from 1 to 1000. But
## If the number is divisible by 3 then get "Nav" printed.
## If the number is divisible by 7 then get "Gurukul" printed.
## If the number is divisible by both 3 and 7, then get "Navgurukul" printed.

def loop(number):
    i=1
    while i<number:
        if i%3==0 and i%7==0:
            print(i,"navgurukul")
        elif i%3==0:
            print(i,"nav")
        elif i%7==0:
            print(i,"gurukul")
        i+=1
loop(1000)