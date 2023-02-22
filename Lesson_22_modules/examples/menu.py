from funcs import speed, volume

req = input("What do you want to calculate? 1 for speed, 2 for volume\n")
if req == '1':
    dist = int(input("Write distance passed in km: "))
    time = int(input("Write time in hrs: "))
    print("The speed is", speed(dist, time), "km/hr")
elif req == '2':
    length = int(input("Length in mtrs = "))
    height = int(input("Height in mtrs = "))
    width = int(input("Width in mtrs= "))
    print("The volume is", volume(length, height, width), "cubic metres")
else:
    print("Wrong entry")




