## Q25. Given a list of numbers, write a Python program 
# to count positive and negative numbers in a List using function.
## Example:
## list1 = [2, -7, 5, -64, -14]
## Output: pos = 2, neg = 3

def numbers(list):
    positive_count=0
    negative_count=0
    i=0
    while i<len(list):
        if list[i]>0:
            positive_count+=1
        else:
            negative_count+=1
        i+=1
    print("positive:",positive_count)
    print("negative:",negative_count)
list=[2,-7,5,-64,-14]
numbers(list)