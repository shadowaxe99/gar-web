
import unittest
from django.test import Client
from ai_assistant.models import AIAssistant

class TestAIAssistant(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.ai_assistant = AIAssistant.objects.create(name='Test Assistant')

    def test_ai_assistant_creation(self):
        self.assertEqual(self.ai_assistant.name, 'Test Assistant')

    def test_ai_assistant_list_view(self):
        response = self.client.get('/ai_assistant/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Assistant')

    def test_ai_assistant_detail_view(self):
        response = self.client.get(f'/ai_assistant/{self.ai_assistant.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Assistant')

if __name__ == '__main__':
    unittest.main()

This is a basic test suite for the AI Assistant model and its views. It tests the creation of an AI Assistant instance and the list and detail views.