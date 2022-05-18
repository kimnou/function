def table(num, i):
    print(num," X ",i," = ",num * i)
    if i<10:
        table(num, i + 1)
num=int(input("enter number:"))
table(num, 1)