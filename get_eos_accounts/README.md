## Get a list of EOS accounts
This script will import the snapshot data from the CSV file, filter it by account name, and print it out to the terminal.


    ~/eos-scripts $ python get_eos_accts.py > 20190501_accounts.txt
    ~/eos-scripts $ cat 20190501_accounts.txt | tail
    zzzzzzzzzzzr
    zzzzzzzzzzzu
    zzzzzzzzzzzs
    zzzzzzzzzzzq
    zzzzzzzzzzzt
    zzzzzzzzzzzv
    zzzzzzzzzzzx
    zzzzzzzzzzzw
    zzzzzzzzzzzy
    zzzzzzzzzzzz


## Find all the voters for a proxy 
	$ python get_proxy_votes.py brockpierce1 eosaccounts.txt 
	cryptoblueos brockpierce1

The output is saved to a file starting with the proxy name

	$ cat brockpierce1_votes.txt 
	cryptoblueos

