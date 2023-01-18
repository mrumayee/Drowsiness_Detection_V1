# import requests

# url = "https://www.google.com/maps/dir/?api=1&origin=Kalyan&destination=Mumbai&travelmode=driving"

# payload={}
# headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)


# # print(response['routes'][0]['legs'][0]['steps'][2]['html_instructions'])

# print(response.text)


# 19.0726778, 72.9001570

import webbrowser

webbrowser.open('https://www.google.com/maps/dir/?api=1&origin=Kalyan&destination=Mumbai&travelmode=driving')