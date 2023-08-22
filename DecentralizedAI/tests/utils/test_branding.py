
import unittest
from src.utils import branding

class TestBranding(unittest.TestCase):

    def setUp(self):
        self.branding = branding.Branding()

    def test_set_brand_name(self):
        self.branding.set_brand_name("DecentralizedAI")
        self.assertEqual(self.branding.get_brand_name(), "DecentralizedAI")

    def test_set_brand_logo(self):
        self.branding.set_brand_logo("assets/images/logo.png")
        self.assertEqual(self.branding.get_brand_logo(), "assets/images/logo.png")

    def test_set_brand_icon(self):
        self.branding.set_brand_icon("assets/images/icon.png")
        self.assertEqual(self.branding.get_brand_icon(), "assets/images/icon.png")

if __name__ == '__main__':
    unittest.main()
