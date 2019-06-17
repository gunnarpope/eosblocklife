""" get_abi.py
    by @gunnarpope on Telegram
	eossweden.org
	6/11/19
  
   	USAGE: find all the geographic locations for all BPs and plot them. 

# Note: use this to find all of the bps
cleos -u https://api.eossweden.org system listproducers -l 200 >> bp_list.txt

$ cleosu system listproducers -l 100
"""

import requests
import sys
import json
from pprint import pprint

url = "https://www.starteos.io/" 
abi = url + "bp.json"


response = requests.get(abi)
print(response.text)

# bps = json.loads(response.text)
# pprint(bps)
