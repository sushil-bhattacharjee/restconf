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

# #PRINT ALL THE INTERFACES
# print("\n[yellow]PRINT ALL THE INTERFACES\n")
# url_in = f"https://{device['host']}:{device['port']}/restconf/data/native/interface"


# response_in = requests.get(url=url_in, headers=headers, auth=(device['user'], device['password']), verify=False)
# print(response_in.text)

# #PRINT THE LOOPBACK INTERFACE
# print("[blue]PRINT THE LOOPBACK INTERFACE\n")
# url_LB = f"https://{device['host']}:{device['port']}/restconf/data/native/interface/Loopback"


# response_LB = requests.get(url=url_LB, headers=headers, auth=(device['user'], device['password']), verify=False)
# print(response_LB.text)

#PRINT THE LOOPBACK routing table
print("[red]PRINT THE ROUTING TABLE\n")
url_rp = f"https://{device['host']}:{device['port']}/restconf/data/ietf-routing:routing"

response_rp = requests.get(url=url_rp, headers=headers, auth=(device['user'], device['password']), verify=False)
print(response_rp.text)
