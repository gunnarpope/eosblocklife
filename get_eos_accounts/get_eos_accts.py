"""get_eos_accounts.py
   author: gunnarpope on 5/24/19 
   @gunnarpope on Telegram 

   Get a snapshot of all the EOS accounts from a .CSV snapshot file
"""

import csv

accounts = []
with open('20190501_account_snapshot.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        accounts.append(row)

# print out the last 10 accounts
print(accounts[-10:]) 

# print out only the last 10 account names
print(accounts[-1][1]) 

names = [ x[1] for x in accounts]

# print out all account names in the terminal
for name in names:
    print(name)



