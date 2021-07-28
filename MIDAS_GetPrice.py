import requests
import json

#Query passes in JWT access token as "token", Rate Identification Number (RIN) as rateID formatted as a string, and "alldata" or "realtime" for queryType formatted as a string

def GetPrice(token, rateID, queryType):
    headers = {'accept': 'application/json', 'Authorization': "Bearer " + token}
    url = 'https://cecwats2.org/api/valuedata?id=' + rateID + '&querytype=' + queryType
    pricing_response = requests.get(url, headers=headers)

    return (json.loads(pricing_response.text))
