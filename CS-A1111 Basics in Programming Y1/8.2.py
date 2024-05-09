from math import pi, cos, sqrt

EARTH_RADIUS = 6371  # km
EARTH_CIRCUMFERENCE = EARTH_RADIUS * 2 * pi  # km
DEGREE_EQUATOR = EARTH_CIRCUMFERENCE / 360  # km


def degrees_to_radians(deg):
    rad = deg * (pi / 180)
    return rad


def calculate_longitude_degree_length(latitude_degrees):
    return cos(degrees_to_radians(latitude_degrees)) * DEGREE_EQUATOR  # km


def calculate_distance(lat1, lon1, lat2, lon2):
    latitude_degree_length = 111.2  # km, roughly constant for our purposes
    longitude_degree_length = calculate_longitude_degree_length((lat1 + lat2) / 2)
    # km, depends on latitude due to Earth being round

    # Write your distance formula here.
    x = lat2 - lat1
    xx = x * latitude_degree_length
    y = lon2 - lon1
    yy = y * longitude_degree_length
    distance = sqrt((xx * xx) + (yy * yy))

    return distance


def day(info):
    d = info.split(";")
    day1 = d[3]
    day1d = day1.split("T")
    dx = day1d[1].split("Z")
    offday1 = dx[0]

    return offday1


def mini(t1, t2):

    q = t1.split(":")
    e = t2.split(":")
    durHH = int(e[0]) - int(q[0])
    durMM = int(e[1]) - int(q[1])
    durSS = int(e[2]) - int(q[2])

    if durMM < 0:
        durMM += 60
        durHH -= 1
    if durSS < 0:
        durSS += 60
        durMM -= 1

    return durHH, durMM, durSS


def main():

    tiedot = []
    x = True
    while x:
        try:
            filename = input("Journey file name:\n")
            file = open(filename, 'r')

            x = False
        except OSError:
            print("Could not open the file {:s}, try again.".format(filename))
            x = True

    i = 0
    x = 0
    for rivi in file:
        rivi = rivi.rstrip()
        tiedot.append(rivi)
    pituus = 0
    for i in range(0, len(tiedot)):
        eka = 0
        eka1 = 0
        toka = 0
        toka1 = 0
        if x > 2:

            eka = float(tiedot[i].split(";")[0])
            eka1 = float(tiedot[i].split(";")[1])
            if i + 1 < len(tiedot):
                toka = float(tiedot[i+1].split(";")[0])
                toka1 = float(tiedot[i+1].split(";")[1])
                pit = calculate_distance(eka, eka1, toka, toka1)
                pituus += pit
        x += 1

    da = day(tiedot[3])
    dl = day(tiedot[(len(tiedot)) - 1])

    kestoHH, kestoMM, kestoSS = mini(da, dl)

    aika = (kestoHH * 60) + kestoMM + (kestoSS / 60)
    print("Your journey took {:.1f} minutes.".format(aika))
    print("You travelled {:.1f} kilometers.".format(pituus))


main()
