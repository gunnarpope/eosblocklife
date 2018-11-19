# eosblocklife
telegram: @gunnarpope

account: eosblocklife
# A Public Key Infastructure for EOS Users
"PKI: It's not dead, just sleeping." -Gutmann

telegram: @gunnarpope


The EOS blockchain is well suited to host a robust public key infastructure (PKI) capable of automating information security at the peer-to-peer level.

The `contract/pki` is designed to provide an infastructure to host the public encryption and signing keys for any account on the EOS network to enable all EOS applications to provide peer-to-peer encryption services.

This is a work in progress and your feedback is welcome!

## scripts/get_info.py
Data is not read from the blockchain with the same redundant, multi-signature verification that is used to write data to the blockchain. How can we validate data retrieved from an API endpoint across multiple network nodes? `get_info.py` provides a method to return account info from multiple an API endpoints and compares the SHA-256 hash of the data returned to insure data integrety across multiple endpoints. It would be even better if the endpoints would sign the data returned from a `cleos` call.


```
~/repos/eosblocklife/scripts $ python get_info.py eosblocklife permissions

Node 				 Hash
https://api.eosnewyork.io/ 	 e66106d6e1abc65f87a0f333b031bcfa985d808ae2081a1e83c315fe5ac45d60
https://api.eosdetroit.io:443/ 	 e66106d6e1abc65f87a0f333b031bcfa985d808ae2081a1e83c315fe5ac45d60
https://eos.greymass.com:443/ 	 e66106d6e1abc65f87a0f333b031bcfa985d808ae2081a1e83c315fe5ac45d60

****Data Validated From  3 API Endpoints*****

{'eosblocklife':'permissions'}
data:  [{'perm_name': 'active', 'parent': 'owner', 'required_auth': {'threshold': 1, 'keys': [{'key': 'EOS6CrvFdSEGGzUumMdncxmBiDXb3axst7pksjeuaHRHjjXhDnhVa', 'weight': 1}], 'accounts': [], 'waits': []}}, {'perm_name': 'owner', 'parent': '', 'required_auth': {'threshold': 1, 'keys': [{'key': 'EOS8RAgN2bxGnmmSdC8WSiq6iwGNjtWmM51WizAUw4ujCKmqSopE6', 'weight': 1}], 'accounts': [], 'waits': []}}]

```
