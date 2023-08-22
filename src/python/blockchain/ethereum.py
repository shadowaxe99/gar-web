
import json
from web3 import Web3, HTTPProvider

class Ethereum:
    def __init__(self, contract_address, contract_abi, provider_url):
        self.web3 = Web3(HTTPProvider(provider_url))
        self.contract_address = Web3.toChecksumAddress(contract_address)
        self.contract_abi = json.loads(contract_abi)
        self.contract = self.web3.eth.contract(address=self.contract_address, abi=self.contract_abi)

    def get_balance(self, address):
        return self.web3.eth.getBalance(address)

    def send_transaction(self, from_address, to_address, amount):
        nonce = self.web3.eth.getTransactionCount(from_address)
        txn_dict = {
            'to': to_address,
            'value': amount,
            'gas': 2000000,
            'gasPrice': self.web3.toWei('40', 'gwei'),
            'nonce': nonce,
            'chainId': 3
        }
        signed_txn = self.web3.eth.account.signTransaction(txn_dict, private_key=from_address)
        txn_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return self.web3.toHex(txn_hash)
