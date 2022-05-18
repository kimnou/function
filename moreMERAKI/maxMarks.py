## marks=[[45,21,42,63],[12,42,42,53],[42,90,78,13],[94,89,78,76],[87,55,98,99]]
#63
#53
#90
#94
#99

def marks(list):
    i=0
    while i<len(list):
        j=0
        maximum=0
        while j<len(list[i]):
            maximum=max(list[i])
            j+=1
        i+=1
        print(maximum)
list=[[45,21,42,63],[12,42,42,53],[42,90,78,13],[94,89,78,76],[87,55,98,99]]
marks(list)