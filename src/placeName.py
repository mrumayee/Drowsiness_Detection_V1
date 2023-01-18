# Importing required libraries
from turtle import distance
from googleplaces import GooglePlaces, types
from numpy import RankWarning
import geopy.distance
import streamlit as st



count = 0
array = []
# Use your own API key for making api request calls
API_KEY = 'AIzaSyBckOEoNarjyygfYyQ86Hx-XWiFfBe-Tx8' 

# Initialising the GooglePlaces constructor
google_places = GooglePlaces(API_KEY)

origin = (19.254733652524887,73.14354077983727)


# call the function nearby search with
# the parameters as longitude, latitude,
# radius and type of place which needs to be searched of
# type can be HOSPITAL, CAFE, BAR, CASINO, etc
query_result = google_places.nearby_search(
		# lat_lng ={'lat': 46.1667, 'lng': -1.15},
		lat_lng ={'lat': 19.254733652524887, 'lng': 73.14354077983727}, #19.254733652524887, 73.14354077983727 - coordinates of Mrunmayee Home
		rankby= 'distance',
		# types =[types.TYPE_HOSPITAL] or
		# [types.TYPE_CAFE] or [type.TYPE_BAR]
		# or [type.TYPE_CASINO])
		types =[types.TYPE_RESTAURANT],
		)

# If any attributions related
# with search results print them
if query_result.has_attributions:
	print (query_result.html_attributions)


# Iterate over the search results
for place in query_result.places:
	count= count+1
	print(" ")
	# print(place)
	print("----------------------------------------------")
	print(" ")
	# place.get_details()
	st.write(str(count) + ")"+" Place Name : "+ place.name)
	st.write("    Latitude : ", place.geo_location['lat'])
	print("    Longitude : ", place.geo_location['lng'])
	dst = (float(place.geo_location['lat']),float(place.geo_location['lng']))
	print("    Co-ordinates of origin & destination are  : ",origin,dst)
	print("    Distance : ", geopy.distance.distance(origin,dst).km,"km")

