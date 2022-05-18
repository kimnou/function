## In this program, we will count the number of students 
## and the cost of one student will be calculated according 
## to the cost of one month of Navgurukul.
## Take input of two values ​​of input using:
## number of students and a student's expenses
## If total cost is 50000 (50 thousand) or less then
## print "We are within budget" otherwise print "We are out of budget".

def student_expense(students,expense):
    total_expense=students*expense
    if total_expense>50000:
        print(total_expense,":over budget")
    else:
        print(total_expense,":within budget")
students=int(input("enter no. of students:"))
expense=int(input("enter expense of one student:"))
student_expense(students,expense)