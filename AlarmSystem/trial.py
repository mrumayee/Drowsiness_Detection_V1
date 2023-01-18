# Importing required libraries
from turtle import distance
from googleplaces import GooglePlaces, types
from numpy import RankWarning
import geopy.distance
from pandas import option_context
import requests
import streamlit as st

global array
array = []
# Use your own API key for making api request calls
API_KEY = 'AIzaSyBckOEoNarjyygfYyQ86Hx-XWiFfBe-Tx8'

google_places = GooglePlaces(API_KEY)
origin = (19.254733652524887, 73.14354077983727)


def nearbySearch(origin):
    global count
    count = 0
    global query_result

    global placeList
    placeList = {}

    query_result = google_places.nearby_search(
        # lat_lng ={'lat': 46.1667, 'lng': -1.15},
        # 19.254733652524887, 73.14354077983727 - coordinates of Mrunmayee Home
        lat_lng={'lat': 19.254733652524887, 'lng': 73.14354077983727},
        rankby='distance',
        # types =[types.TYPE_HOSPITAL] or
        # [types.TYPE_CAFE] or [type.TYPE_BAR]
        # or [type.TYPE_CASINO])
        types=[types.TYPE_RESTAURANT],
    )

    if query_result.has_attributions:
        print(query_result.html_attributions)

    for place in query_result.places:

        count = count+1
        print(" ")

        dst = (float(place.geo_location['lat']),
               float(place.geo_location['lng']))

        placeList[place.name] = dst  # Getting all data in Dictionary

        st.write(str(count) + ")"+" Place Name : " + place.name)
        st.write("    Latitude : ", place.geo_location['lat'])
        st.write("    Longitude : ", place.geo_location['lng'])
        st.write("    Distance : ", geopy.distance.distance(origin, dst).km, "km")


st.write(nearbySearch(origin))
