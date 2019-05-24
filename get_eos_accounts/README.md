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


## Find which proxy ACCOUNT_NAME is using: 

    $ cleos -u https://api.eossweden.org get account ACCOUNT_NAME | grep proxy
