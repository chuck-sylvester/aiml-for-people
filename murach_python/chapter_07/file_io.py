# file_io.py
# CPS
# January 21, 2025

""" Sample script that demonstrates text file I/O """

from helper_functions import read_stations, list_stations, add_station

# display menu
def display_menu():
    print("\nVistA Stations")
    print()
    print("COMMAND MENU")
    print("list - List all stations")
    print("add  - Add a station")
    print("del  - Delete a station")
    print("exit - Exit program")
    print()

# main function
def main():
    display_menu()
    stations = read_stations()
    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list_stations(stations)
        elif command.lower() == "add":
            add_station(stations)
        elif command.lower() == "del":
            print("You selected: delete")
        elif command.lower() == "exit":
            print("You selected: exit")
            break
        else:
            print("\nNot a valid command. Please try again.\n")

if __name__ == "__main__":
    main()