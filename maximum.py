def maxnum(list):
    i=0
    maxno=list[0]
    while i<len(list):
        if list[i]>maxno:
            maxno=list[i]
        i+=1
    return "maximum is:",maxno
list=[3,6,12,5,7,2,9]
print(maxnum(list))

