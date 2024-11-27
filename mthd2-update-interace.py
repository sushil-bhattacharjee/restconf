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

#Method:-2: Change the Loopback1 ip addess under entire interface container, hence all-interface.yml
'''
Since Loopback is a leaf-list, therefore it is required to rewrite entire interface container in PUT method.
'''
url = f"https://{device['host']}:{device['port']}/restconf/data/native/interface"

with open("all-interface.yml", "r") as f:
    loopback_config = safe_load(f)

response = requests.put(url=url, headers=headers, auth=(device['user'], device['password']), \
    json=loopback_config, verify=False)

response.raise_for_status()
if response.ok:
    print(f"[green]Successfully UPDATED loopback interface:[/green] {response.status_code}")
    
#PRINT the Loopback
print("\n")
print("[blue]PRINT THE Loopback Interface\n")

url_get = f"https://{device['host']}:{device['port']}/restconf/data/native/interface/Loopback"
response = requests.get(url=url_get, headers=headers, auth=(device['user'], device['password']), verify=False)
print(response.text)