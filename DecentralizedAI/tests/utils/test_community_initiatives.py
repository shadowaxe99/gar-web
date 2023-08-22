
import unittest
from src.utils import community_initiatives

class TestCommunityInitiatives(unittest.TestCase):

    def setUp(self):
        self.initiatives = community_initiatives.CommunityInitiatives()

    def test_create_initiative(self):
        result = self.initiatives.create_initiative('Test Initiative', 'This is a test initiative')
        self.assertEqual(result, 'Test Initiative created successfully')

    def test_delete_initiative(self):
        self.initiatives.create_initiative('Test Initiative', 'This is a test initiative')
        result = self.initiatives.delete_initiative('Test Initiative')
        self.assertEqual(result, 'Test Initiative deleted successfully')

    def test_update_initiative(self):
        self.initiatives.create_initiative('Test Initiative', 'This is a test initiative')
        result = self.initiatives.update_initiative('Test Initiative', 'This is an updated test initiative')
        self.assertEqual(result, 'Test Initiative updated successfully')

if __name__ == '__main__':
    unittest.main()
