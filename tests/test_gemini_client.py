"""Tests unitaires pour l'intégration de Gemini."""
import pytest
from unittest.mock import patch
from src.llm.gemini_client import GeminiClient

def test_missing_api_key(monkeypatch):
    """Le système doit refuser de s'initialiser sans clé."""
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    with pytest.raises(ValueError):
         GeminiClient()

def test_invalid_api_key(monkeypatch):
    """Refuser de s'initialiser si la clé est celle par défaut dans l'exemple."""
    monkeypatch.setenv("GEMINI_API_KEY", "your_gemini_api_key_here")
    with pytest.raises(ValueError):
         GeminiClient()

@patch('src.llm.gemini_client.genai.GenerativeModel.generate_content')
def test_successful_response(mock_generate, monkeypatch):
    """Test de réponse valide."""
    monkeypatch.setenv("GEMINI_API_KEY", "dummy_valid_key")
    
    # Mocking the response object structure
    class MockResponse:
        def __init__(self, text):
            self.text = text
            
    mock_generate.return_value = MockResponse("Il fera beau demain à Paris.")
    
    client = GeminiClient()
    response = client.generate_response("Quel temps fait-il à Paris ?")
    
    assert "Il fera beau" in response
    assert mock_generate.call_count == 1

@patch('src.llm.gemini_client.genai.GenerativeModel.generate_content')
def test_retry_logic_and_fallback(mock_generate, monkeypatch):
    """Teste que le système tente X fois puis retourne le fallback courtois."""
    monkeypatch.setenv("GEMINI_API_KEY", "dummy_valid_key")
    # Configurer le mock pour lever une Exception systématique
    mock_generate.side_effect = Exception("API Server Error")
    
    client = GeminiClient()
    feedback = client.generate_response("Test prompt")
    
    # Vérifier que le message de Fallback gracieux est bien retourné
    assert "momentanément indisponible" in feedback
    # Vérifier que la méthode a été appelée plusieurs fois (Retry de tenacity)
    # L'appel initial + retries (2)
    assert mock_generate.call_count == 3
