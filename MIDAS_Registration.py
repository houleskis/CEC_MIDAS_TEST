import requests
import json
import base64

##Encode registration values as base64

#organization is an optional value in the registration API
organization = "your_org_name"
org_encodedBytes = base64.b64encode(organization.encode("utf-8"))
organization64 = str(org_encodedBytes, "utf-8")

username = "your_username_here"
user_encodedBytes = base64.b64encode(username.encode("utf-8"))
username64 = str(user_encodedBytes, "utf-8")

password = "your_password_here"
pswd_encodedBytes = base64.b64encode(password.encode("utf-8"))
password64 = str(pswd_encodedBytes, "utf-8")

emailaddress = "your_email_here"
email_encodedBytes = base64.b64encode(emailaddress.encode("utf-8"))
emailaddress64 = str(email_encodedBytes, "utf-8")

fullname = "your_email_here"
fullname_encodedBytes = base64.b64encode(fullname.encode("utf-8"))
fullname64 = str(fullname_encodedBytes, "utf-8")


#Put together the dict for the JSON payload
registration_info = {"organization":organization64,"username":username64,"password":password64,"emailaddress":emailaddress64,"fullname":fullname64}

url = 'https://cecwats2.org/api/registration'
headers =  {"Content-Type":"application/json"}

response = requests.post(url, data=json.dumps(registration_info), headers=headers)

#Prints below will return 200 response for successful call
print(response)
#Response text should be: 'User account for your_user_name was successfully created. A verification email has been sent to your_email. Please click the link in the email in order to start using the API.'
print(response.text)
