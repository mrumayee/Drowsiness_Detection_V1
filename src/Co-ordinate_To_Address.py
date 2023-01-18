from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
lald = "25.1726735,51.5653361"
print("Latitude and Longitude:",lald)
location = geolocator.geocode(lald)
print("Location address of the said Latitude and Longitude:")
print(location)