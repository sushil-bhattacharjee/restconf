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

#Method:-2: Change the entire static ip routing of route container, hence routeconf.yml

url = f"https://{device['host']}:{device['port']}/restconf/data/native/ip/route"

with open("routeconf.yml", "r") as f:
    route_config = safe_load(f)

response = requests.put(url=url, headers=headers, auth=(device['user'], device['password']), \
    json=route_config, verify=False)

response.raise_for_status()
if response.ok:
    print(f"[green]Successfully UPDATED routing tables:[/green] {response.status_code}")
    
#PRINT the Loopback
print("\n")
print("[blue]PRINT THE ROUTING TABLE\n")

url_get = f"https://{device['host']}:{device['port']}/restconf/data/native/ip/route"
response = requests.get(url=url_get, headers=headers, auth=(device['user'], device['password']), verify=False)
print(response.text)