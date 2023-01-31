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


access_token = "access token here"
user_id = "user id here" 

def fitbit_callback():
    threshold = "normal"
# Step Count : /activities/steps/date/today/today.json
# Heart Rate : /activities/heart/date/today/today/1d.json -- 1 month | 1d--1 day

    activity_request = requests.get('https://api.fitbit.com/1/user/'+ user_id +'/activities/heart/date/today/1d.json', headers = {'Authorization':'Bearer '+ access_token})

    # Check the status 
    # st.write('Status : '+ str(activity_request.status_code))

    # Display the time and value of the heartrate
    time_1= (activity_request.json()["activities-heart-intraday"]['dataset'][-1]['time'])
    time_2 = (activity_request.json()["activities-heart-intraday"]['dataset'][-2]['time'])
    # print(time)
    value_1 = (activity_request.json()["activities-heart-intraday"]['dataset'][-1]['value'])
    value_2 = (activity_request.json()["activities-heart-intraday"]['dataset'][-2]['value'])

    sum=0
    avg=0
    for i in range(1,6):
        time = (activity_request.json()["activities-heart-intraday"]['dataset'][-i]['time'])
        value = (activity_request.json()["activities-heart-intraday"]['dataset'][-i]['value'])
        sum +=value
    avg= sum/5
    if avg > 100 or avg < 60 or abs(value_1-value_2) > 30:
        threshold= "abnormal"
    return threshold


if __name__ == '__main__':
    print(fitbit_callback())
