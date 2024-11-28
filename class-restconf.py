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
            
    def get_ip_address(self):
        """Retrieve the IP address of the interface."""
        try:
            url = f"{self.base_url}GigabitEthernet={self.intfno}/ip/address"
            print(f"[yellow]GET Request URL: {url}[/yellow]")  # For debugging
            response = requests.get(url=url, auth=self.auth, headers=self.headers, verify=False)
            #Raise an HTTPError for bad responses
            response.raise_for_status()
            print("\n[blue]PRINT IP ADDRESS BEFORE CHANGE:[/blue]")
            print(response.text)
        ##This catches network-related errors, such as DNS errors or invalid URLs.
        except requests.exceptions.RequestException as e: 
            print(f"[red]Error occured while getting IP address: {e}[/red]")
        #After each request, it checks whether the status code indicates an error (e.g., 400, 500). 
        # If it does, raise_for_status() raises an HTTPError.
        except Exception as e: 
            print(f"[red]Unexpected error: {e}[/red]")

    def update_ip_address(self, address, mask):
        """Update the IP address of the interface."""
        try:
            url = f"{self.base_url}GigabitEthernet={self.intfno}/ip/address/primary/address"
            payload = {"address": address, "mask": mask}
            print(f"[yellow]PUT Request URL: {url}[/yellow]")  # For debugging
            response = requests.put(url=url, auth=self.auth, headers=self.headers, verify=False, data=json.dumps(payload))
            # Raise an HTTPError for bad responses (e.g., 400, 500)
            response.raise_for_status()
            print("\n[green]Response Status Code:[/green]", response.status_code)
        except requests.exceptions.RequestException as e:
            print(f"[red]Error Occured while updating IP address: {e}[/red]")
        except Exception as e:
            print(f"[red]Unexpected error: {e}[/red]")

    def get_updated_ip_address(self):
        """Retrieve the IP address of the interface after update."""
        try:
            url = f"{self.base_url}GigabitEthernet={self.intfno}/ip/address"
            print(f"[yellow]GET Request URL: {url}[/yellow]")  # For debugging
            response = requests.get(url=url, auth=self.auth, headers=self.headers, verify=False)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            print("\n[red]PRINT THE UPDATED IP ADDRESS:[/red]")
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"[red]Error occurred while getting updated IP address: {e}[/red]")
        except Exception as e:
            print(f"[red]Unexpected error: {e}[/red]")

# Main execution
if __name__ == "__main__":
    # Initialize the interface manager
    manager = RestConfInterfaceManager(
        base_url='https://192.168.0.59/restconf/data/native/interface/',
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
        manager.update_ip_address(address="192.168.110.1", mask="255.255.255.0")
    elif function_name == "get_updated_ip_address":
        manager.get_updated_ip_address()
    else:
        print(f"Invalid function name: {function_name}")