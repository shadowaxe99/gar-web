
import unittest
from src.marketplace import revenue_models

class TestRevenueModels(unittest.TestCase):

    def setUp(self):
        self.revenue_model = revenue_models.RevenueModel()

    def test_calculate_revenue(self):
        revenue = self.revenue_model.calculate_revenue(100, 10)
        self.assertEqual(revenue, 90)

    def test_calculate_profit(self):
        profit = self.revenue_model.calculate_profit(100, 10, 5)
        self.assertEqual(profit, 85)

    def test_calculate_loss(self):
        loss = self.revenue_model.calculate_loss(100, 110)
        self.assertEqual(loss, 10)

if __name__ == '__main__':
    unittest.main()
