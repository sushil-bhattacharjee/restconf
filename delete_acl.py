import requests
import json
import base64
import os
from dotenv import load_dotenv
from rich import print

#Disable self-signed ssl certificate warnings
requests.packages.urllib3.disable_warnings()

# Load environment variables
load_dotenv()

# Get the username and password from the environment file
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

# Encode the username and password
userpass = f'{username}:{password}'
userpass_encode = base64.b64encode(userpass.encode()).decode()

url = "https://10.1.10.61:443/restconf/data/Cisco-IOS-XE-native:native/ip/access-list/Cisco-IOS-XE-acl:extended=Prod10_Chpater06"

payload = {}
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',
  'Authorization': f'Basic {userpass_encode}'
}

response = requests.request("DELETE", url, headers=headers, data=payload, verify=False)

print(response.text)

###instructions how you run the script when using os evn
# (.Vrestconf) sushil@Ubuntu24:~/restconf$ source .env 
# (.Vrestconf) sushil@Ubuntu24:~/restconf$ python3 delete_acl.py 