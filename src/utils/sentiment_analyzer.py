from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer

class SentimentAnalyzer:
    """Service gérant l'analyse de sentiment des textes."""

    @staticmethod
    def analyze(text: str) -> dict:
        """
        Analyse la polarité d'un texte et catégorise le sentiment.
        
        Args:
            text (str): Le texte à analyser.
            
        Returns:
            dict: { "score": float, "category": str }
                  score est compris entre -1.0 et 1.0.
                  category est "Positif", "Négatif" ou "Neutre".
        """
        if not text or not text.strip():
            return {"score": 0.0, "category": "Neutre"}

        # Utilisation de textblob-fr
        blob = TextBlob(text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
        score = blob.sentiment[0] # polarité entre -1.0 et 1.0
        
        if score > 0.1:
            category = "Positif"
        elif score < -0.1:
            category = "Négatif"
        else:
            category = "Neutre"
            
        return {"score": score, "category": category}
