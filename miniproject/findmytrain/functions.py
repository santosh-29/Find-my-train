from math import radians, cos, sin, asin, sqrt

def dist(lat1, long1, lat2, long2):
    #Haversine formula for distance
    # print(lat1, long1, lat2, long2)
    lat1, long1, lat2, long2 = map(radians, [float(lat1), float(long1), float(lat2), float(long2)])
    dlon = long2 - long1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6371* c
    return km

def directions(lat1, long1, lat2, long2):
    return "http://maps.google.com/maps?saddr="+str(lat1)+","+str(long1)+"&daddr="+str(lat2)+","+str(long2)