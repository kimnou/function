# speed=int(input("enter speed:"))
# def driver(speed):
#     speed1=speed-70
#     point=speed1//5
#     if point<=70:
#         print("70")
#     elif point>70:
#         print(speed)
#     elif point>12:
#         print("license suspended")
# driver(speed)        
    
def driver(speed):
    if speed<=70:
        print("70")
    else:
        speed1=speed-70
        point=speed1//5
        if point<=12:
            print("point is:",point)
        else:
            print("point:",point,"-","license suspended")
speed=int(input("enter speed:"))
driver(speed)
