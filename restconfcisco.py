import sys, requests, urllib3, json
from rich import print

#c8000v-1 Credentials
URL  = 'https://192.168.0.59:443/restconf/data/native/interface/'
USER = 'admin'
PASS = 'C1sco12345'

# Headers required for RESTCONF
headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}

# Disable warnings
urllib3.disable_warnings()

# Main method
def main():
    ###########################################
    # Retrieve Device Configuration in Python #
    ###########################################
    # URL for API calls
    url_ge1 = URL + 'GigabitEthernet=3/ip/address'

    # GET call to c8000v-1, SSL checking turned off
    response = requests.get(url=url_ge1, auth=(USER, PASS), headers=headers, verify=False)
    # Print the returned JSON
    print("\n [blue]PRINT IP ADDRESS BEFORE CHNAGE")
    print(response.text)

    #####################################
    # Update Configuration Using Python #
    #####################################
    # URL for API calls
    url_ge3 = URL + 'GigabitEthernet=3/ip/address/primary/address'

    # New IP address
    ip_address = {"address": "192.168.0.88", "mask": "255.255.255.0"}
    
    # PUT call to c8000v-1, SSL checking turned off
    response_chnage = requests.put(url=url_ge3, auth=(USER, PASS), headers=headers,\
                                   verify=False, data=json.dumps(ip_address))

    # Print the response's status code
    print(response_chnage.status_code)

if __name__ == '__main__':
    main()