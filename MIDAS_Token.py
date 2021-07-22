import requests
import json
import base64

#Function passes through your MIDAS username and password as strings and returns the JWT token as a string

def GetToken(username, password):
    #encodes the username and password as bytes
    user_encodedBytes = base64.b64encode(username.encode("utf-8"))
    pswd_encodedBytes = base64.b64encode(password.encode("utf-8"))

    headers = {b'Authorization': b'BASIC ' + user_encodedBytes + b':' + pswd_encodedBytes}
    url = 'https://cecwats2.org/api/token'

    response = requests.get(url,headers=headers)
    print(response.text)

    return response.headers['Token']



