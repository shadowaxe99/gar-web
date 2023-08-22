
import unittest
from src.user.user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()

    def test_create_user(self):
        self.user.create_user('test', 'test@test.com', 'password')
        self.assertEqual(self.user.name, 'test')
        self.assertEqual(self.user.email, 'test@test.com')

    def test_authenticate_user(self):
        self.user.create_user('test', 'test@test.com', 'password')
        result = self.user.authenticate('test@test.com', 'password')
        self.assertTrue(result)

    def test_fail_authenticate_user(self):
        self.user.create_user('test', 'test@test.com', 'password')
        result = self.user.authenticate('test@test.com', 'wrongpassword')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
