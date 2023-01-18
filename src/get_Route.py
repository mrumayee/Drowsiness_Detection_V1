import webbrowser

url = "https://www.google.com/maps/search/?api=1&query="
lat = 19.254733652524887
long = 73.14354077983727
travelmode="&travelmode=driving"

# https://www.google.com/maps/dir/?api=1&origin=Kalyan&destination=Mumbai&travelmode=driving'

# url+'origin='+origin+'&'+'destination='+destination+travelmode ---- using names of destination and origin name
# url+str(lat)+"%2C"+str(long) -------------- for latitude and longitude
# dir_action=navigate

webbrowser.open('https://www.google.com/maps/search/?api=1&map_action=pano&query=19.254733652524887%2C73.14354077983727&dir_action=navigate')