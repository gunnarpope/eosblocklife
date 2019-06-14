""" bp_locations.py
    by @gunnarpope on Telegram
	eossweden.org
	6/11/19
  
   	USAGE: find all the geographic locations for all BPs and plot them. 

# Note: use this to find all of the bps
cleos -u https://api.eossweden.org system listproducers -l 200 >> bp_list.txt

"""

import requests
import sys
import json
from pprint import pprint


url = "https://api.eossweden.org/v1/chain/get_producers"

payload = "{\"limit\":\"100\",\"lower_bound\":\"1\",\"json\":true}"

headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

response = requests.request("POST", url,data=payload, headers=headers)

bps = json.loads(response.text)
pprint(bps)
pprint(bps['total_producer_vote_weight'])

print(bps.keys()) 
# # write the output to file
# with open(proxyname + '_votes.txt', 'w') as f:
# 	for voter in proxyvoters:
# 		f.write("%s\n" % voter)	
