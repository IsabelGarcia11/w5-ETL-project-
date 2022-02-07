import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import re
import numpy
import folium
from folium.plugins import HeatMapWithTime as HMWT
from folium.plugins import HeatMap as HM
from folium import plugins

def location(x):
    if str(x)>='40.56233'and str(x)<'40.6501':
        return "Staten Island"
    if str(x)>='40.6501'and str(x)<'40.689798':
        return "Brooklyn"
    if str(x)>='40.689798'and str(x)<'40.703663772':
        return "Queens"
    if str(x)>='40.703663772'and str(x)<'40.84985':
        return "Manhattan"
    else:
        return "Bronx"


def generateBaseMap(default_location=[40.751873, -73.977706], default_zoom_start=11):
    
    base_map = folium.Map(location=default_location, 
                          control_scale=True, 
                          zoom_start=default_zoom_start)
    
    return base_map


def split(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr   = arr[size:]
     arrs.append(arr)
     return arrs

def names(x):
    if x=='The Bronx':
        return 'Bronx'
    else:
        return x
def total(x):
    if x=='Manhattan':
        return '113'
    if x=='Brooklyn':
        return '77'
    if x=='Queens':
        return '35'
    if x=='Bronx':
        return '16'
    if x=='Staten Island':
        return '5'