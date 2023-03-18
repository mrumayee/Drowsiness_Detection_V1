from email import header
from wsgiref import headers
import fitbit
# import gather_keys_oauth2 as Oauth2
import pandas as pd 
import datetime
from pprint import pprint
import json
import requests

# Program to print FITBIT DATA

# Validity for access token 1 year


access_token = "YOUR_ACCESS_TOKEN"
user_id = "YOUR_USER_ID" 

def fitbit_callback():

# Step Count : /activities/steps/date/today/today.json
# Heart Rate : /activities/heart/date/today/today/1d.json -- 1 month | 1d--1 day

    activity_request = requests.get('https://api.fitbit.com/1/user/'+ user_id +'/activities/heart/date/today/1d.json', headers = {'Authorization':'Bearer '+ access_token})

    # Check the status 
    # st.write('Status : '+ str(activity_request.status_code))

    # Display the time and value of the heartrate
    time = (activity_request.json()["activities-heart-intraday"]['dataset'])
    # print(time)
    value = (activity_request.json()["activities-heart-intraday"])
    # print(value)
    return time , value


if __name__ == '__main__':
    print(fitbit_callback())
