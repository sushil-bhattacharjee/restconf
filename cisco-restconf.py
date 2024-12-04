import sys, requests, urllib3, json
from rich import print

#CSR1000v
URL = 'https://10.1.10.11/restconf/data/native/interface/'
USER = 'cisco'
PASS = 'cisco'

#Headers required for RESTCONF
headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}

#Disable warnings
urllib3.disable_warnings()

#Main method
def main():
    #################################################################
    #Retrive Device Configuration in Python #
    #################################################################
    # URL for API calls
    url_get1 = URL + 'GigabitEthernet=4/ip/address'
    
    #GET call to CSR1000v, SSL checking turned off
    response = requests.get(url_get1, auth=(USER, PASS), headers=headers, verify=False)
    #Print the returned JSON
    print(response.text)
    
    
    ##################################################################
    # Update Configuration Using Python #
    ##################################################################
    # URL for API calls
    url_update = URL + 'GigabitEthernet=4/ip/address/primary/address'
    
    
    # New IP address
    ip_address = {"address": "192.168.0.88", "mask": "255.255.255.0"}
    # PUT call to CSR1000v, SSL checking turned off
    response_change = requests.put(url_update, auth=(USER, PASS), headers=headers, verify=False,
                                   data=json.dumps(ip_address))
    
    # Print the response's status code
    print(response_change.status_code)
if __name__ == '__main__':
    main()