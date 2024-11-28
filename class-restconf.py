import requests
import urllib3
import json
import sys
from rich import print
import os

# Disable warnings for unverified HTTPS requests
urllib3.disable_warnings()

class RestConfInterfaceManager:
    def __init__(self, base_url, intfno):
        self.base_url = base_url
        self.intfno = intfno
        
        #Get username and password from environment variables
        self.username = os.getenv('RESTCONF_USERNAME')
        self.password = os.getenv('RESTCONF_PASSWORD')
        if not self.username or not self.password:
            print("[red]Error: Username or password not set in environment variables![/red]")
            exit(1)

        self.auth = (self.username, self.password)
        self.headers = {
            'Content-Type': 'application/yang-data+json',
            'Accept': 'application/yang-data+json'
        }
            
    def get_ip_address():
        """Retrieve the IP address of the interface."""
        url = f"{self.base_url}GigabitEthernet={self.intfno}/ip/address"
        response = requests.get(url=url, auth=self.auth, headers=self.headers, verify=False)
        print("\n[blue]PRINT IP ADDRESS BEFORE CHANGE:[/blue]")
        print(response.text)

    def update_ip_address(self, address, mask):
        """Update the IP address of the interface."""
        url = f"{self.base_url}GigabitEthernet={self.intfno}/ip/address/primary/address"
        payload = {"address": address, "mask": mask}
        response = requests.put(
            url=url,
            auth=self.auth,
            headers=self.headers,
            verify=False,
            data=json.dumps(payload)
        )
        print("\n[green]Response Status Code:[/green]", response.status_code)

    def get_updated_ip_address(self):
        """Retrieve the IP address of the interface after update."""
        url = f"{self.base_url}GigabitEthernet={self.intfno}/ip/address"
        response = requests.get(url=url, auth=self.auth, headers=self.headers, verify=False)
        print("\n[red]PRINT THE UPDATED IP ADDRESS:[/red]")
        print(response.text)


# Main execution
if __name__ == "__main__":
    # Initialize the interface manager
    manager = RestConfInterfaceManager(
        base_url='https://192.168.0.59:443/restconf/data/native/interface/',
        intfno= 3,
    )

    # Get the command-line argument (function name)
    if len(sys.argv) != 2:
        print("Usage: python <script_name> <function_name>")
        print("Available functions: get_ip_address, update_ip_address, get_updated_ip_address")
        sys.exit(1)

    function_name = sys.argv[1]  # This is the function to call
    # '''
    # python .\class-restconf.py get_ip_address
    # python .\class-restconf.py update_ip_address
    # python .\class-restconf.py get_updated_ip_address
    # '''
    # Call the specified function
    if function_name == "get_ip_address":
        manager.get_ip_address()
    elif function_name == "update_ip_address":
        manager.update_ip_address(address="192.168.90.1", mask="255.255.255.0")
    elif function_name == "get_updated_ip_address":
        manager.get_updated_ip_address()
    else:
        print(f"Invalid function name: {function_name}")