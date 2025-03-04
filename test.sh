#!/bin/bash

# Device Information
DEVICE_IP="10.1.10.61"
USERNAME="cisco"
PASSWORD="cisco"

# ACL Name
ACL_NAME="Pod10_Chapter06"

# RESTCONF URL for ACL Configuration (PUT Request)
URL="https://$DEVICE_IP/restconf/data/Cisco-IOS-XE-native:native/ip/access-list"

# JSON Payload for Replacing the ACL
PAYLOAD=$(cat <<EOF
{
    "Cisco-IOS-XE-acl:extended": {
        "name": "$ACL_NAME",
        "access-list-seq-rule": [
            {
                "sequence": "5",
                "ace-rule": {
                    "action": "permit",
                    "protocol": "udp",
                    "host": "198.51.100.1",
                    "dst-host": "203.0.113.2",
                    "dst-eq": 123
                }
            }
        ]
    }
}
EOF
)

# Replace ACL using HTTP PUT Request
curl -k -X PUT "$URL" \
  -u "$USERNAME:$PASSWORD" \
  -H "Content-Type: application/yang-data+json" \
  -H "Accept: application/yang-data+json" \
  -d "$PAYLOAD"

# RESTCONF URL for Getting the ACL Entry (GET Request)
GET_URL="https://$DEVICE_IP/restconf/data/Cisco-IOS-XE-native:native/ip/access-list/Cisco-IOS-XE-acl:extended=$ACL_NAME/access-list-seq-rule=5/ace-rule"

# Fetch ACL Entry and Extract Protocol & Action
response=$(curl -k -s -X GET "$GET_URL" \
  -u "$USERNAME:$PASSWORD" \
  -H "Accept: application/yang-data+json" | jq -r '."Cisco-IOS-XE-acl:ace-rule"')

protocol=$(echo "$response" | jq -r '."protocol"')
action=$(echo "$response" | jq -r '."action"')

# Display Protocol and Action
echo "Protocol: $protocol"
echo "Action: $action"
