# tee ratkaisu tänne
# Write your solution here
import math
def get_station_data(filename: str):
    with open(filename) as places:
        d = {}
        for place in places:
            place = place.split(";")
            if place[0] == "Longitude":
                continue
            d[place[3]] = float(place[0]) , float(place[1])
    return d

def distance(stations: dict, station1: str, station2: str):
    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict): 
    my_list = []
    for key1 in stations:
        for key in stations:
            x_km = (stations[key1][0] - stations[key][0]) * 55.26
            y_km = (stations[key1][1] - stations[key][1]) * 111.2
            distance = math.sqrt(x_km**2 + y_km**2)
            if my_list == []:
                my_list.append(key1)
                my_list.append(key)
                my_list.append(distance)
            if distance > my_list[2]:
                my_list = []
                my_list.append(key1)
                my_list.append(key)
                my_list.append(distance)
    return tuple(my_list)
if __name__ == "__main__":
    stations = get_station_data('stations3.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)