import requests
from yaml import safe_load
from rich import print

requests.packages.urllib3.disable_warnings()

device = {
    "host": "192.168.0.184",
    "port": "443",
    "user": "admin",
    "password": "C1sco12345"
}

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

#Method:-DELETE VLAN id=45

url = f"https://{device['host']}:{device['port']}/restconf/data/native/vlan/vlan-list=45"

response = requests.delete(url=url, headers=headers, auth=(device['user'], device['password']), verify=False)

response.raise_for_status()
if response.ok:
    print(f"[green]Successfully DELETED VLAN:[/green] {response.status_code}")
    
#PRINT the Loopback
print("\n")
print("[blue]PRINT THE VLAN TABLE\n")

url_get = f"https://{device['host']}:{device['port']}/restconf/data/native/vlan"
response = requests.get(url=url_get, headers=headers, auth=(device['user'], device['password']), verify=False)
print(response.text)