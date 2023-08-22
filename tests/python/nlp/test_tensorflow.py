
import unittest
from src.python.nlp.tensorflow import TensorFlowModel

class TestTensorFlowModel(unittest.TestCase):
    def setUp(self):
        self.model = TensorFlowModel()

    def test_model_initialization(self):
        self.assertIsNotNone(self.model.model, "Model should be initialized")

    def test_model_training(self):
        data = ["This is a test sentence", "Another test sentence"]
        labels = [0, 1]
        self.model.train(data, labels)
        self.assertTrue(self.model.is_trained, "Model should be trained")

    def test_model_prediction(self):
        sentence = "This is a test sentence"
        prediction = self.model.predict(sentence)
        self.assertIn(prediction, [0, 1], "Prediction should be either 0 or 1")

if __name__ == '__main__':
    unittest.main()
