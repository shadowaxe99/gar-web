
import unittest
from django.test import TestCase
from blockchain.models import Transaction

class BlockchainModelTest(TestCase):

    def setUp(self):
        self.transaction = Transaction.objects.create(
            sender='sender_address',
            recipient='recipient_address',
            amount=10
        )

    def test_transaction_creation(self):
        self.assertEqual(self.transaction.sender, 'sender_address')
        self.assertEqual(self.transaction.recipient, 'recipient_address')
        self.assertEqual(self.transaction.amount, 10)

    def test_string_representation(self):
        self.assertEqual(str(self.transaction), self.transaction.sender + ' sent ' + str(self.transaction.amount) + ' to ' + self.transaction.recipient)

if __name__ == '__main__':
    unittest.main()
