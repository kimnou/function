## take two list.Now,create a new list in which elements 
# in both the lists are to occur only once.
# list1 = [1, 5, 10, 12, 16, 20]
# list2 = [1, 2, 10, 13, 16]
# new_list = [1, 2, 5, 10, 12, 13, 16, 20]

# def unique(list1,list2):
#     list1.extend(list2)
#     i=0
#     new_list=[]
#     while i<len(list1):
#         if list1[i] not in new_list:
#             new_list.append(list1[i])
#         i+=1
#     new_list.sort()
#     print(new_list)
# list1=[1, 5, 10, 12, 16, 20]
# list2=[1, 2, 10, 13, 16]
# unique(list1,list2)