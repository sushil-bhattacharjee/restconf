import sys, requests, urllib3, json
from rich import print

# c8000v-1 Credentials
URL = 'https://192.168.0.59:443/restconf/data/native/interface/'
USER = 'admin'
PASS = 'C1sco12345'

# Headers required for RESTCONF
headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}

# Disable warnings
urllib3.disable_warnings()

# Function to retrieve the device's IP address
def get_ip_address():
    url_ge1 = URL + 'GigabitEthernet=3/ip/address'
    response = requests.get(url=url_ge1, auth=(USER, PASS), headers=headers, verify=False)
    print("\n[blue]PRINT IP ADDRESS BEFORE CHANGE[/blue]")
    print(response.text)

# Function to update the IP address
def update_ip_address():
    url_ge3 = URL + 'GigabitEthernet=3/ip/address/primary/address'
    ip_address = {"address": "192.168.0.88", "mask": "255.255.255.0"}
    response_change = requests.put(url=url_ge3, auth=(USER, PASS), headers=headers, 
                                   verify=False, data=json.dumps(ip_address))
    print("\n[green]Response Status Code: [/green]", response_change.status_code)

# Main method
def main():
    # Uncomment the function you want to execute
    get_ip_address()
    # update_ip_address()

if __name__ == '__main__':
    main()
