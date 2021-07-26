import requests
import json

#Query passes in JWT access token as "token", Rate Identification Number (RIN) as rateID, and "alldata" or "realtime" for queryType

def GetPrice(token, rateID, queryType):
    headers = {'accept': 'application/json', 'Authorization': "Bearer " + token}
    url = 'https://cecwats2.org/api/pricedata?id=' + rateID + '&querytype=' + QueryType
    pricing_response = requests.get(url, headers=headers)

    return (json.loads(pricing_response.text))
