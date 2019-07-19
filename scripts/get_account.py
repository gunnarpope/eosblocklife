# eoscryptosys: towards a spoof-proof public key infastructure
# author: @gunnarpope
# date: 11/16/18

"""
This script retrieves account data from a variety of EOS nodes and
compares the sha256 HASH of all returned data for an added layer of
data validation.

Usage:
    $ python get_info.py account_name data_field
Example:
    $ python get_info.py eosio permissions
	$ python get_account.py eosblocklife voter_info
"""

import json
import requests
import hashlib
import secrets
import numpy as np
import sys

if (len(sys.argv) != 3):
    print("Usage: $ python get_info.py account_name data_field")
    print("Example: $ python get_info.py eosio permissions")
    exit()

account = sys.argv[1]
field   = sys.argv[2]

# add a random collection of api endpoints to check from
nodes = [
    "https://api.eossweden.org/",
]
print()
print("Node \t\t\t\t Hash")
hashlist = []
for node in nodes:

    try:
        url = node + "v1/chain/get_account"
        data = {"account_name":account}
        response = requests.request("POST", url, data=json.dumps(data))
        respjson = response.json()
        data = respjson[field]
        print( json.dumps(data))
    except:
        print("Failed: " + node)

print()


    # "https://api.eosmetal.io:18890/",
    # "https://eosapi.blockmatrix.network:443/",
    # "https://node2.eosphere.io/",
    # "https://eos.saltblock.io/",
    # "https://eos-api.worbli.io:443/",
    # "https://user-api.eoseoul.io:443/",
    # "https://node2.liquideos.com:8883/",
    # "https://api.eosuk.io:443/",
    # "https://api.eosio.cr:443/",
    # "https://eu1.eosdac.io:443/",
    # "https://api.main.alohaeos.com:443/",
    # "https://rpc.eosys.io/"
    # "https://fn.eossweden.se:443/",
    # "https://eos.greymass.com:443/"
