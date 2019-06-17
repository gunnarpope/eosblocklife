import os

output = str(os.system('cleos -u https://api.eossweden.org system listproducers -l 21 > bp_list.txt'))

with open('bp_list.txt','r') as f:
	data = f.readlines()

bps = [ row.strip().split() for row in data]

for bp in bps[:3]:
	print(bp)
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

