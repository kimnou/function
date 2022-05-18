def distance(kms):
    if kms<=20:
        print("close")
    elif kms<50 and kms>20:
        print("median")
    else:
        print("far")
distance(20)
distance(30)
distance(90)