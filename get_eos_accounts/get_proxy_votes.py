""" get_proxy_votes.py
    by @gunnarpope at Telegram
	5/24/19
  
   	USAGE: find all the accounts voting for a certain proxy
	$ python get_proxy_votes.py brockpierce1 eosaccounts.txt 
	cryptoblueos brockpierce1
	$ cat brockpierce1_votes.txt 
	cryptoblueos

   where proxyname is the 12-character EOS account name 
"""

import requests
import sys
import json

accountname = 'cryptoblueos'
proxyname   = 'brockpierce1'
accountname = sys.argv[1]
filename    = sys.argv[2]
url = "https://api.eossweden.org/v1/chain/get_account"
 
headers = {
   'accept': "application/json",
   'content-type': "application/json"
   }

with open(filename,'r') as f:
	content = f.readlines()
 	
accounts = [ account.strip() for account in content]

proxyvoters = []

for accountname in accounts: 
	payload = "{\"account_name\":\"" + accountname + "\"}"
	
	response = requests.request("POST", url, data=payload, headers=headers)
	data = json.loads(response.text)
	try:
		proxyvote = data['voter_info']['proxy']
	
		if proxyvote == proxyname:
			print(data['account_name'], data['voter_info']['proxy'])
			proxyvoters.append(accountname)
	except:
		print(accountname, 'No voter data')

# write the output to file
with open(proxyname + '_votes.txt', 'w') as f:
	for voter in proxyvoters:
		f.write("%s\n" % voter)	
