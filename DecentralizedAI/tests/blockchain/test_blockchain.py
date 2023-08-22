
import unittest
from src.blockchain.blockchain import Blockchain

class TestBlockchain(unittest.TestCase):

    def setUp(self):
        self.blockchain = Blockchain()

    def test_create_block(self):
        block = self.blockchain.create_block('data')
        self.assertEqual(block.data, 'data')

    def test_validate_chain(self):
        self.blockchain.create_block('data')
        self.assertTrue(self.blockchain.validate_chain())

    def test_validate_chain_with_invalid_chain(self):
        self.blockchain.create_block('data')
        self.blockchain.chain[1].data = 'tampered data'
        self.assertFalse(self.blockchain.validate_chain())

if __name__ == '__main__':
    unittest.main()
