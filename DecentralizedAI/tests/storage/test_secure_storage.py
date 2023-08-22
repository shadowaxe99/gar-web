
import unittest
from src.storage.secure_storage import SecureStorage

class TestSecureStorage(unittest.TestCase):

    def setUp(self):
        self.secure_storage = SecureStorage()

    def test_store_data(self):
        data = "Test data"
        self.secure_storage.store_data(data)
        self.assertEqual(self.secure_storage.retrieve_data(), data)

    def test_retrieve_data(self):
        data = "Test data"
        self.secure_storage.store_data(data)
        retrieved_data = self.secure_storage.retrieve_data()
        self.assertEqual(retrieved_data, data)

    def test_delete_data(self):
        data = "Test data"
        self.secure_storage.store_data(data)
        self.secure_storage.delete_data()
        self.assertIsNone(self.secure_storage.retrieve_data())

if __name__ == '__main__':
    unittest.main()
