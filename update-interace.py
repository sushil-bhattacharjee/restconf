import requests
from yaml import safe_load
from rich import print

requests.packages.urllib3.disable_warnings()

device = {
    "host": "192.168.0.59",
    "port": "443",
    "user": "admin",
    "password": "C1sco12345"
}

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

#Method:-1: Change the Loopback1 ip addess
'''
{
  "Cisco-IOS-XE-native:Loopback": [
    {
      "name": 1,
      "ip": {
        "address": {
          "primary": {
            "address": "1.1.1.1",
            "mask": "255.255.255.255"
          }
        }
      }
    }
  ]
}
Since Loopback is a list, therefore it is required to write "Loopback=1" instead of just
Loopback in PUT method.
'''
url = f"https://{device['host']}:{device['port']}/restconf/data/native/interface/Loopback=1"

with open("loopconf.yml", "r") as f:
    loopback_config = safe_load(f)

response = requests.put(url=url, headers=headers, auth=(device['user'], device['password']), \
    json=loopback_config, verify=False)

response.raise_for_status()
if response.ok:
    print(f"[green]Successfully UPDATED loopback interface:[/green] {response.status_code}")