## Write a Python function to multiply all the numbers in a list.
## Sample List : (8, 2, 3, -1, 7)
## Expected Output : -336

def multiply(list):
    i=0
    product=1
    while i<len(list):
        product=product*list[i]
        i+=1
    print(product)
list=[8,2,3,-1,7]
multiply(list)