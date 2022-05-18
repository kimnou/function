## Q26. Write a function called fizz_buzz that takes a number.
## If the number is divisible by 3, it should return “Fizz”.
## If it is divisible by 5, it should return “Buzz”.
## If it is divisible by both 3 and 5, it should return “FizzBuzz”.
## Otherwise, it should return the same number.


def fizz_buzz(number):
    if number%3==0 and number%5==0:
        return "fizzbuzz"
    elif number%3==0:
        return "fizz"
    elif number%5==0:
        return "buzz"
    else:
        return number
number=int(input("enter number:"))
print(fizz_buzz(number))