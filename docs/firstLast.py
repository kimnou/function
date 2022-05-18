## Q1.Write a Python program to count the number of strings where the string length is 2     or more and the first and last characters are the same from a given list of strings.
## list=['abc', 'xyz', 'aba', '1221']
## result= 2.


def strings(list):
    list=["aba","abc","1221","xyz"]
    i=0
    count=0
    while i<len(list):
        if list[i][0]==list[i][-1]:
            count+=1
        i+=1
    print(count)
# list=["aba","abc","1221","xyz"]
strings(list)
