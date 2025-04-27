# Api endpoint - .its address or the location of the data 
# API req - checks if eligible to ask for dta and returns dta upon call

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

latitude = float(response.json()["iss_position"]["latitude"])
longitude = float(response.json()["iss_position"]["longitude"])

data = (longitude,latitude)
print(data)


# response code
'''
1XX : Wait 
2XX : Valid for response
3XX : Not Authorized
4XX : You Screwed up
5XX : I Screwed Up

'''