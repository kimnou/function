## Q8.Write a Python function that accepts a string and calculate the 
# number of upper case letters and lower case letters.
## Sample String : 'The quick Brow Fox'
## Expected Output :
## No. of Uppercase characters : 3
## No. of Lower case Characters : 12


def alphabets(string):
    i=0
    count_UPPER=0
    count_lower=0
    while i<len(string):
        if string[i]>="a" and string[i]<="z":
            count_lower=count_lower+1
        elif string[i]>="A" and string[i]<="Z":
            count_UPPER=count_UPPER+1
        i+=1
    print("UPPERCASE:",count_UPPER)
    print("lowercase:",count_lower)
string=input("enter string:")
alphabets(string)

