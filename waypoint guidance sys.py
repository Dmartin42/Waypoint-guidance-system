import os as os
import webbrowser
from datetime import datetime

import gmplot
print(os.path.abspath(gmplot.__file__))
# Code for waypoint guidance system
# developed for NSDT2020 by Daniel Martin

api_key = input("Input google api key: ")

# current location: new_york for testing purposes
current_loc = [40.737102, -73.990318]
plot_points = []

# delete old data
if os.path.exists("coords.txt"):
    os.remove("coords.txt")
    if os.path.exists('map.html'):
        os.remove('map.html')
    print("data deleted")

# Point Coords: (40.737102,-73.990318),(40.749825,-73.987963),(40.752946,-73.987384),(40.755823,-73)


def get_map(title="WaGS"):
    return gmplot.GoogleMapPlotter(
        current_loc[0], current_loc[1], zoom=17, map_type="satellite",
        title=title, apikey=api_key)


def draw_current_location(gmap) -> None:
    gmap.marker(current_loc[0], current_loc[1],
                color='red', title="Current", label='A')
    

def draw_open_map(gmap) -> None:
    gmap.draw('map.html')
    webbrowser.open_new_tab('map.html')


def get_list_of_tuples(coords_list=[float]) -> list:
    return_list = []
    return_list.append((current_loc[0],current_loc[1]))
    for i in range(1, len(coords_list), 2):
        return_list.append((coords_list[i-1], coords_list[i]))

    return return_list



gmap = get_map(title="Input: WaGS")
draw_current_location(gmap=gmap)
gmap.enable_marker_dropping(color='blue', draggable=True)
draw_open_map(gmap=gmap)

while True:
    if os.path.exists("coords.txt"):
        f = open('map.html', 'r')
        f.close()
        print("Found")
        try:
            with open('coords.txt') as f:
                r = [float(x) for x in f.read().split(',')]
                break
        except FileNotFoundError:
            continue




plot_points = get_list_of_tuples(coords_list=r)
path = zip(*plot_points)
gmap = get_map()
gmap.plot(*path, edge_width=5, color='brown')
draw_current_location(gmap=gmap)
draw_open_map(gmap=gmap)
