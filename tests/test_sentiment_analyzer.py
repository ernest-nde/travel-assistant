import unittest
from utils.sentiment_analyzer import SentimentAnalyzer

class TestSentimentAnalyzer(unittest.TestCase):
    
    def test_positive_sentiment(self):
        text = "J'adore cette ville"
        result = SentimentAnalyzer.analyze(text)
        self.assertEqual(result["category"], "Positif")
        self.assertGreater(result["score"], 0)
        
    def test_negative_sentiment(self):
        text = "Erreur, je déteste ce voyage inutile"
        result = SentimentAnalyzer.analyze(text)
        self.assertEqual(result["category"], "Négatif")
        self.assertLess(result["score"], 0)
        
    def test_neutral_sentiment(self):
        text = "Je pars lundi"
        result = SentimentAnalyzer.analyze(text)
        self.assertEqual(result["category"], "Neutre")
        self.assertEqual(result["score"], 0)

if __name__ == "__main__":
    unittest.main()
