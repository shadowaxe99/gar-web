
import unittest
from src.user.user_experience import UserExperience

class TestUserExperience(unittest.TestCase):

    def setUp(self):
        self.user_experience = UserExperience()

    def test_initialize(self):
        self.assertIsNotNone(self.user_experience)

    def test_localized_memory(self):
        self.user_experience.set_localized_memory("Test Memory")
        self.assertEqual(self.user_experience.get_localized_memory(), "Test Memory")

    def test_relationship_building(self):
        self.user_experience.set_relationship_building("Test Relationship")
        self.assertEqual(self.user_experience.get_relationship_building(), "Test Relationship")

    def test_no_internet_access_requirement(self):
        self.user_experience.set_no_internet_access_requirement(True)
        self.assertTrue(self.user_experience.get_no_internet_access_requirement())

if __name__ == '__main__':
    unittest.main()
