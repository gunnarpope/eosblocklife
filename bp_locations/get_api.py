""" get_api.py
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

def get_api(acct_url):
	"""Get the bp.json for an account
	INPUT: get_api('https://www.starteos.io')
    OUTPUT: a json formatted output"""
	try:
		api = json.loads(requests.get(acct_url + "/bp.json").text)
	except:
		api = {'error'}
	return api 

def get_location(acct_url):
	return get_api(acct_url)['org']['location']

def get_country(acct_url):
	return get_api(acct_url)['org']['location']['country']

def get_latitude(acct_url):
	return get_api(acct_url)['org']['location']['latitude']

def get_longitude(acct_url):
	return get_api(acct_url)['org']['location']['longitude']

def get_city(acct_url):
	return get_api(acct_url)['org']['location']['name']

def get_acctname(acct_url):
	return get_api(acct_url)['producer_account_name']

def get_location(acct_url):
	api     =   get_api(acct_url)
	try:
		lat		= 	api['org']['location']['latitude']
		lon		= 	api['org']['location']['longitude']
		country = 	api['org']['location']['country']
		city 	=  	api['org']['location']['name']
	except:
 		lat, lon, country, city = (0,0,0,0)		

	return lat, lon, country, city

if __name__ == "__main__":
	

	# pprint( get_api('https://www.starteos.io'))
	# pprint( get_acctname('https://www.starteos.io'))
	# pprint( get_location('https://www.starteos.io'))
	# pprint( get_country('https://www.starteos.io'))
	# pprint( get_latitude('https://www.starteos.io'))
	# pprint( get_longitude('https://www.starteos.io'))
	# pprint( get_city('https://www.starteos.io'))
	# pprint( get_acctname('https://www.starteos.io'))
	pprint( get_location('https://www.starteos.io'))
