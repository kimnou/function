def numbers_less_than_twenty(list):
    i=0
    while i<len(list):
        a=list[i]
        if a>20:
            list.remove(a)
        else:
            i+=1
    return list
num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
num_list_sub_20 = numbers_less_than_twenty(num_list)
if num_list==num_list_sub_20:
    print("same")
else:
    print("not same")
print ("Initial list:",num_list)
print ("List that doesn't contain numbers greate than 20:", num_list_sub_20)