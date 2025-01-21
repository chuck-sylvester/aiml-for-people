# helper_functions.py
# CPS
# January 21, 2025

""" Helper functions for file_io program """

FOLDER_NAME = "./"
FILENAME = "vista_stations.txt"

# read stations from file
def read_stations():
    stations = []
    with open(FOLDER_NAME + FILENAME, "r") as station_file:
        for line in station_file:
            line = line.replace("\n", "")
            stations.append(line)
    print(f"{stations}\n")
    return stations

# write stations to file
def write_stations(stations):
    with open(FOLDER_NAME + FILENAME, "w") as station_file:
        for station in stations:
            station_file.write(f"{station}\n")

# list stations from file
def list_stations(stations):
    for i, station in enumerate(stations, start=1):
        print(f"{i}. {station}")
    print()

# add a station
def add_station(stations):
    station = input("Station: ")
    stations.append(station)
    write_stations(stations)
    print(f"{station} as added.\n")

# delete a station
