
import unittest
from src.python.blockchain.ethereum import Ethereum

class TestEthereum(unittest.TestCase):

    def setUp(self):
        self.ethereum = Ethereum()

    def test_create_block(self):
        block_data = {"transactions": [{"from": "address1", "to": "address2", "amount": 10}]}
        block = self.ethereum.create_block(block_data)
        self.assertEqual(block['data'], block_data)

    def test_validate_block(self):
        block_data = {"transactions": [{"from": "address1", "to": "address2", "amount": 10}]}
        block = self.ethereum.create_block(block_data)
        self.assertTrue(self.ethereum.validate_block(block))

    def test_validate_chain(self):
        block_data1 = {"transactions": [{"from": "address1", "to": "address2", "amount": 10}]}
        block_data2 = {"transactions": [{"from": "address2", "to": "address3", "amount": 5}]}
        self.ethereum.create_block(block_data1)
        self.ethereum.create_block(block_data2)
        self.assertTrue(self.ethereum.validate_chain())

if __name__ == '__main__':
    unittest.main()
