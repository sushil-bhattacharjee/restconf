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

url = f"https://{device['host']}:{device['port']}/restconf/data/native/interface/Loopback"

with open("loopconf.yml", "r") as f:
    loopback_config = safe_load(f)

response = requests.get(url=url, headers=headers, auth=(device['user'], device['password']), verify=False)
print(response.text)
# response.raise_for_status()
# if response.ok:
#     print(f"[green]Successfully created loopback interface:[/green] {response.status_code}")