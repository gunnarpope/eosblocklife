import os
import requests
import json
from pprint import pprint

from get_api import *

# output = str(os.system('cleos -u https://api.eossweden.org system listproducers -l 100 > bp_list.txt'))

with open('bp_list.txt','r') as f:
	data = f.readlines()

# create a row entry for each BP
bps = [ row.strip().split() for row in data]



header = bps[0]
bps    = bps[1:] # strip the header


# print the top 21 BPs
for bp in bps[:21]:
	print(bp)

rank = 1
for i in range(len(bps)):
	# bp[i][3] = float(bp[i][3])
	bps[i].append(rank) 
	rank += 1


bp_list = []
bp_error= []
bpjson  = {}

for bp in bps:
	bpname = bp[0]
	rank = bp[-1]
	lat, lon, country, city = get_location(bp[2])
	if city != 'NULL':
		print(bpname, rank, lat, lon)	
		bp_list.append((bpname, rank, lat, lon))
		bpjson[bpname] = {'rank': rank, 'lat': lat, 'lon': lon}

	else:
		print(bpname, rank, 'NULL','NULL')
		bp_error.append(bpname)
		bpjson[bpname] = {'rank': rank, 'lat':'NULL', 'lon':'NULL'}


with open('bp_gps_locations.json','w') as f:
	f.write(json.dumps(bpjson))
