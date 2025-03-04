import requests
import json
import base64
import os
from dotenv import load_dotenv
from rich import print

# Disable self-signed ssl certificate warnings
requests.packages.urllib3.disable_warnings()

load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
userpass = f'{username}:{password}'
userpass_encode = base64.b64encode(userpass.encode()).decode()

url = "https://10.1.10.61:443/restconf/data/native/ip/access-list/"

payload = json.dumps({
  "Cisco-IOS-XE-acl:extended": [
    {
      "name": "Prod10_Chpater06",
      "access-list-seq-rule": [
        {
          "sequence": "5",
          "ace-rule": {
            "action": "permit",
            "protocol": "tcp",
            "host": "198.51.100.1",
            "dst-host": "203.0.113.2",
            "dst-eq": 1443
          }
        }
      ]
    }
  ]
})
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',
  'Authorization': f'Basic {userpass_encode}'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)
print("[red] IT WILL CREATE A NEW ACL IF THERE IS NO ACL AT ALL. IF THERE IS ALREADY AN ACL, USE PATCH TO ADD NEW ACL[/red]")
print("Adding access-list in the device:")
print(response.status_code)

##Show the access-list in the deivce

response = requests.request("GET", url, headers=headers, verify=False)
print("Access-lists in the device:")
print(response.status_code)
print(response.text)

###instructions how you run the script when using os evn
# (.Vrestconf) sushil@Ubuntu24:~/restconf$ source .env 
# (.Vrestconf) sushil@Ubuntu24:~/restconf$ python3 delete_acl.py 