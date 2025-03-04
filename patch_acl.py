import requests
import json
import base64
import os
from dotenv import load_dotenv
from rich import print

#Disable self-signed ssl certificate warnings
requests.packages.urllib3.disable_warnings()

#Load environment variables
load_dotenv()

#Get the username and password from the environment file
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
userpass = f'{username}:{password}'
userpass_encode = base64.b64encode(userpass.encode()).decode()

url = "https://10.1.10.61:443/restconf/data/native/ip/access-list/Cisco-IOS-XE-acl:extended"

payload = json.dumps({
    "Cisco-IOS-XE-acl:extended": [
        {
            "name": "James_Bond4",
            "access-list-seq-rule": [
                {
                    "sequence": "124",
                    "ace-rule": {
                        "action": "permit",
                        "protocol": "tcp",
                        "host": "199.168.0.1",
                        "src-eq": 1024,
                        "dst-host": "10.1.0.1",
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

response = requests.request("PATCH", url, headers=headers, data=payload, verify=False)
print("[green]Adding/Updating access-list in the device:[/green]")
print(response.status_code)

##Show the access-list in the deivce

response = requests.request("GET", url, headers=headers, verify=False)
print("Access-lists in the device:")
print(response.status_code)
print(response.text)


###instructions how you run the script when using os evn
# (.Vrestconf) sushil@Ubuntu24:~/restconf$ source .env 
# (.Vrestconf) sushil@Ubuntu24:~/restconf$ python3 delete_acl.py 
