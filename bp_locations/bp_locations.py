""" bp_locations.py
    by @gunnarpope on Telegram
	eossweden.org
	6/11/19
  
   	USAGE: find all the geographic locations for all BPs and plot them. 

# Note: use this to find all of the bps
cleos -u https://api.eossweden.org system listproducers -l 21 > bp_list.txt

$ cleosu system listproducers -l 100
"""

import requests
import sys
import json
from pprint import pprint


url = "https://api.eossweden.org/v1/chain/get_producers"

payload = "{\"limit\":\"10\",\"lower_bound\":\"1\",\"json\":true}"

headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

response = requests.request("POST", url,data=payload, headers=headers)

bps = json.loads(response.text)
pprint(bps)

total_vote_weight = float(bps['total_producer_vote_weight'])
print(total_vote_weight) # this works
print(bps.keys())  # dict_keys(['rows', 'total_producer_vote_weight', 'more'])

# print the json for each BP
# for prod in bps['rows']:
#	print('Next BP')
#	pprint(prod)


# names = [ [prod['owner'],prod['total_votes'], float(prod['total_votes'])/total_vote_weight ] for prod in bps['rows']]
names = [ prod['owner'] for prod in bps['rows']]
print(names)
# votes = [  float(prod['total_votes'])/total_vote_weight
# 
# 	row'relative_votes'] = float(row['total_votes'])/total_vote_weight
# 	pprint(row)
# namesrank = [ (prod['owner'], prod['votes']) for prod in bps['rows']]

#print(namesrank)
#print(names)

# # write the output to file
# with open(proxyname + '_votes.txt', 'w') as f:
# 	for voter in proxyvoters:
# 		f.write("%s\n" % voter)	
