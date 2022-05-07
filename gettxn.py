import web3



provider = web3.providers.HTTPProvider('http://127.0.0.1:8545')


w3 = web3.Web3(provider)

address = w3.toChecksumAddress('0xA43919ee67F7c25094Ec2b9119d97B9424842BF4')
count = w3.eth.getTransactionCount(address)
hash = w3.toHex(b'\xd8\xf3\x9a%\x0c\x9e\xacQ\x91f\xca\xab\x18C\x1a\xa1eO\xfd1\xa0\xaf*z.F\x17YR\xf6\x0b\x08')


txn_receipt = w3.eth.get_transaction_receipt(hash)

balance = w3.eth.get_balance(address)

print('count:', count, 'txn_receipt:', txn_receipt, 'address:', address, "balance:", balance)