curl --location --request PUT 'https://10.1.10.61:443/restconf/data/native/ip/access-list/Cisco-IOS-XE-acl:extended=Prod10_Chpater06' \
--header 'Accept: application/yang-data+json' \
--header 'Content-Type: application/yang-data+json' \
--header 'Authorization: Basic Y2lzY286Y2lzY28=' \
--data '{
    "Cisco-IOS-XE-acl:extended": {
        "name": "Prod10_Chpater06",
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
}'

my_var=$(curl https://10.1.10.61:443/restconf/data/native/ip/access-list/Cisco-IOS-XE-acl:extended=Prod10_Chpater06 -k -H "accept: application/yang-data+json" -u cisco:cisco --silent | jq '."Cisco-IOS-XE-acl:extended"."access-list-seq-rule"[0]."ace-rule"."protocol"' -r)
echo "Protocol: $my_var"
my_var1=$(curl https://10.1.10.61:443/restconf/data/native/ip/access-list/Cisco-IOS-XE-acl:extended=Prod10_Chpater06 -k -H "accept: application/yang-data+json" -u cisco:cisco --silent | jq '."Cisco-IOS-XE-acl:extended"."access-list-seq-rule"[0]."ace-rule"."action"' -r)
echo "Action: $my_var1"