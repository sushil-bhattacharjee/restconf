import requests
import json
from rich import print

#Disable self-signed ssl certificate warnings
requests.packages.urllib3.disable_warnings()


url = "https://10.1.10.11/restconf/data/native/ip/route/vrf"

payload = json.dumps({
  "Cisco-IOS-XE-native:vrf": [
    {
      "name": "mgmt",
      "ip-route-interface-forwarding-list": [
        {
          "prefix": "0.0.0.0",
          "mask": "0.0.0.0",
          "fwd-list": [
            {
              "fwd": "10.1.10.2"
            }
          ]
        },
        {
          "prefix": "10.10.20.0",
          "mask": "255.255.255.0",
          "fwd-list": [
            {
              "fwd": "10.1.10.2"
            }
          ]
        },

        {
          "prefix": "192.168.89.0",
          "mask": "255.255.255.0",
          "fwd-list": [
            {
              "fwd": "192.168.89.101"
            }
          ]
        }
      ]
    }
  ]
})
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',
  'Authorization': 'Basic Y2lzY286Y2lzY28='
}

response = requests.request("PATCH", url, headers=headers, data=payload, verify=False)

response.raise_for_status()
if response.ok:
    print(f"\n[green]Successfully added prefix list for vrf-mgmt routes :[/green] {response.status_code}")

response_update = requests.request("GET", url, headers=headers, verify=False)
print("\n[red]show running-config | s ip route vrf mgmt")
print(response_update.text)
