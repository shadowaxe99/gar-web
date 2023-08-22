
import unittest
from src.marketplace import Marketplace

class TestMarketplace(unittest.TestCase):

    def setUp(self):
        self.marketplace = Marketplace()

    def test_add_item(self):
        item = {"name": "Test Item", "price": 100}
        self.marketplace.add_item(item)
        self.assertIn(item, self.marketplace.items)

    def test_remove_item(self):
        item = {"name": "Test Item", "price": 100}
        self.marketplace.add_item(item)
        self.marketplace.remove_item(item)
        self.assertNotIn(item, self.marketplace.items)

    def test_update_item(self):
        item = {"name": "Test Item", "price": 100}
        updated_item = {"name": "Test Item", "price": 200}
        self.marketplace.add_item(item)
        self.marketplace.update_item(item, updated_item)
        self.assertIn(updated_item, self.marketplace.items)
        self.assertNotIn(item, self.marketplace.items)

if __name__ == '__main__':
    unittest.main()
