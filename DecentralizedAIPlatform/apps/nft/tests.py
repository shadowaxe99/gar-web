
from django.test import TestCase
from .models import NFT

class NFTModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        NFT.objects.create(title='Test NFT', description='This is a test NFT')

    def test_title_content(self):
        nft = NFT.objects.get(id=1)
        expected_object_name = f'{nft.title}'
        self.assertEquals(expected_object_name, 'Test NFT')

    def test_description_content(self):
        nft = NFT.objects.get(id=1)
        expected_object_name = f'{nft.description}'
        self.assertEquals(expected_object_name, 'This is a test NFT')

class NFTViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        NFT.objects.create(title='Test NFT', description='This is a test NFT')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/nft/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('nft'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('nft'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'nft/index.html')
