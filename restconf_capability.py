#curl -k -s -u admin:password --location-trusted "https://<device-ip>/restconf/data/ietf-restconf-monitoring:restconf-state/capabilities" -X GET

import requests
from requests.auth import HTTPBasicAuth
import warnings
from urllib3.exceptions import InsecureRequestWarning

# Suppress SSL warnings
warnings.filterwarnings("ignore", category=InsecureRequestWarning)

# RESTCONF details
url = "https://10.1.10.11/restconf/data/ietf-restconf-monitoring:restconf-state/capabilities"
username = "cisco"
password = "cisco"

# Make the GET request
response = requests.get(
    url,
    auth=HTTPBasicAuth(username, password),
    verify=False  # Equivalent to `-k` in curl
)

# Check response
if response.status_code == 200:
    print("Response received:")
    print(response.text)
else:
    print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}")
    print("Response Content:")
    print(response.text)

