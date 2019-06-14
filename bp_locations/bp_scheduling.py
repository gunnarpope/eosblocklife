import json
import hashlib
""" bp_scheduling.py
	Randomize the BP scheduling for the top 32 block producers voted in

	Input: a JSON object holding the votes tally and the recent block number

	OUTPUT: the order that the BPs will produce blocks in the next round
"""

# construct the votes tally and include a recent block number to prevent replay
bpvotes = { "votes": {"bp1": 10,
				"bp2": 50,
				"bp3": 4},
			"block": 314159
		  }
print(json.dumps(bpvotes))

# Hash the bpvotes object to determine the order of BP production
h = hashlib.sha256(json.dumps(bpvotes).encode('utf-8')).hexdigest()
print("first index")
first = h[0:2] 
print(first)
even_num = [x for x in range(0,65) if x % 2 == 0]

order = [ h[i:i+2] for i in even_num]
print(order)

# determine the schedule from the hash
# for start in 

print(h[0:2])
for key in bpvotes["votes"]:
	print(bpvotes["votes"][key])


