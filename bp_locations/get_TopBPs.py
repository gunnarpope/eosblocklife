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

top21bp = bps[:21]
print(len(top21bp))
print(top21bp[:5])

bot21bp = bps[21:]
print(len(bot21bp))
print(bot21bp[:5])

# get the url for each bp
urls = [ [x[0], x[2]] for x in top21bp]
print(urls)

# get the gps coordinates for each bp
bp_url = top21bp[0][2]
print(bp_url)

bp_list = []
bp_error= []
for bp in top21bp:
	bpname = bp[0]
	rank = bp[4]
	lat, lon, country, city = get_location(bp[2])
	if city != 'NULL':
		print(bpname, rank, lat, lon)	
		bp_list.append((bpname, rank, lat, lon))
	else:
		print(bpname, rank, 'NULL','NULL')
		bp_error.append(bpname)



# 
# rows = bps.split()
# print(rows[:3])
# 
# rows = []
# for line in bps:
# 	rows.append(line)
# 
# print( line[:3])
# split = output.strip('\n\t *')
# print(split)
# print('Length of output %i' % len(split))

