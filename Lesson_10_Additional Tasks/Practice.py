def wind(deg):
    deg = (abs(deg) % 360)
    return "North" if deg == 0 else "NE" if 0 < deg < 90 else "East" if deg == 90 \
        else "SE" if 90 < deg < 180 else "S" if deg == 180 else "SW" if 180 < deg < 270 \
            else "W" if deg == 270 else "NW"

print(wind(int(input("Write direction: "))))


