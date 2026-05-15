"""Tests unitaires pour le composant Document Processor"""
import pytest
import io
import os
from src.document_processor import DocumentProcessor

def get_test_pdf_path(filename: str) -> str:
    """Retourne le chemin vers un fichier de test."""
    test_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(test_dir, 'test_data', filename)

def generate_valid_dummy_pdf() -> io.BytesIO:
    """Génère un faux PDF basique en mémoire via pypdf pour les tests.
    Comme on teste juste DocumentProcessor, on simule un bytestream."""
    from pypdf import PdfWriter
    writer = PdfWriter()
    writer.add_blank_page(width=200, height=200)
    # Pypdf a des fonctionnalités limitées pour écrire du texte, mais 
    # pour un test fonctionnel basique d'extraction, on va utiliser la structure d'un fichier réel ou simuler
    
    # Afin d'éviter de créer une vraie génération de PDF compliquée pour les tests,
    # le plus simple est de créer un mock ou de fournir un petit array d'octets valide.
    # Dans ce test un peu "light", si on ne fournit pas de vrai texte, pypdf retournera "" pour extract_text.
    outputStream = io.BytesIO()
    writer.write(outputStream)
    outputStream.seek(0)
    return outputStream

def test_extract_text_valid_pdf(monkeypatch):
    """Vérifier l'extraction correcte d'un texte simple.
    On mock pypdf pour simuler une lecture réussie."""
    class MockPage:
        def extract_text(self):
            return "Ceci est un test document."
            
    class MockReader:
        def __init__(self, stream):
            self.pages = [MockPage(), MockPage()]
            
    monkeypatch.setattr("src.document_processor.PdfReader", MockReader)
    
    fake_stream = io.BytesIO(b"fake_pdf_content_but_mocked")
    text = DocumentProcessor.extract_text_from_pdf(fake_stream)
    
    assert "Ceci est un test document." in text
    assert len(text.split()) > 0

def test_extract_text_handles_corrupted_file():
    """Vérifier qu'une exception ValueError claire est renvoyée pour des fichiers non-pdf/corrompus."""
    corrupted_bytes = io.BytesIO(b"Ceci n'est pas un pdf valide du tout, juste du texte.")
    with pytest.raises(ValueError) as exc:
        DocumentProcessor.extract_text_from_pdf(corrupted_bytes)
    assert "corrompu ou illisible" in str(exc.value)

def test_extract_text_handles_no_text_image_pdf(monkeypatch):
    """Vérifier le comportement face à un PDF sans texte sélectionnable."""
    class MockPageBlank:
        def extract_text(self):
            return ""
            
    class MockReaderBlank:
        def __init__(self, stream):
            self.pages = [MockPageBlank()]
            
    monkeypatch.setattr("src.document_processor.PdfReader", MockReaderBlank)
    
    fake_stream = io.BytesIO(b"fake_pdf_content_but_mocked")
    with pytest.raises(ValueError) as exc:
        DocumentProcessor.extract_text_from_pdf(fake_stream)
    assert "Aucun texte lisible n'a pu être extrait" in str(exc.value)

def test_extract_text_handles_empty_pdf(monkeypatch):
    """Vérifier le comportement face à un PDF avec zero pages."""
    class MockReaderEmpty:
        def __init__(self, stream):
            self.pages = []
            
    monkeypatch.setattr("src.document_processor.PdfReader", MockReaderEmpty)
    
    fake_stream = io.BytesIO(b"fake_pdf_content_but_mocked")
    with pytest.raises(ValueError) as exc:
        DocumentProcessor.extract_text_from_pdf(fake_stream)
    assert "Le document PDF ne contient aucune page" in str(exc.value)
