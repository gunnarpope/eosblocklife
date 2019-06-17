""" get_api.py
    by @gunnarpope on Telegram
	eossweden.org
	6/11/19
  
   	USAGE: find all the geographic locations for all BPs and plot them. 

# Note: use this to find all of the bps
cleos -u https://api.eossweden.org system listproducers -l 200 >> bp_list.txt

$ cleosu system listproducers -l 100
"""


def get_api(acct_url):
	"""Get the bp.json for an account
	INPUT: get_api('https://www.starteos.io')
    OUTPUT: a json formatted output"""

	api = json.loads(requests.get(acct_url + "/bp.json").text)
	pprint(api)
	return api 

if __name__ == "__main__":
	
	import requests
	import sys
	import json
	from pprint import pprint

	get_api('https://www.starteos.io')
