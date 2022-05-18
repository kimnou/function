def year(age):
    if age<=14:
        print("kids drink toddy")
    elif age>14 and age<18:
        print("teens drink coke")
    elif age>=18 and age<21:
        print("young adult drink beer")
    else:
        print("adults drink whiskey")
age=int(input("enter age:"))
year(age)