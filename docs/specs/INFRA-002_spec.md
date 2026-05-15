# Spécification Technique : INFRA-002 - Traitement de Documents PDF

> **User Story** : US-003 : Traitement de Documents PDF  
> **ID Technique** : INFRA-002 (anciennement INFRA-008)  
> **Architecte** : AI Assistant  
> **Date** : 2026-03-11  
> **Statut** : 📋 En Review

---

## 📝 Vue d'Ensemble

Cette spécification détaille l'implémentation de la **US-003 : Traitement de Documents PDF**, correspondant au besoin immédiat d'extraire le contenu des documents de voyage (réservations, billets, guides) pour ensuite nourrir le contexte du chatbot. 

### Rappel des Critères d'Acceptation

- ✅ **CA-009.1** : Logique d'extraction isolée dans le module `src/utils/document_processor.py`, utilisant `pypdf`.
- ✅ **CA-009.2** : Extraction réussie d'une chaîne de caractères exploitable par le LLM, texte nettoyé.
- ✅ **CA-009.3** : Widget Streamlit de téléversement (Upload) intégré avec indicateurs de succès/chargement.
- ✅ **CA-009.4** : Gestion des erreurs claires (Fichier illisible, corrompu, format non valide).
- ✅ **CA-009.5** : Tests unitaires robustes à l'aide de fichiers PDF de tests.

---

## 🏗️ Architecture Proposée

L'architecture s'appuie sur une approche **modulaire** et **découplée**, assurant que l'interface utilisateur n'ait connaissance que de l'API de haut niveau du module documentaire, sans se soucier du moteur d'extraction sous-jacent.

```text
┌───────────────────────────┐
│     Interface Utilisateur │ 
│     (src/app.py)          │
│  - Widget file_uploader   │
│  - Indicateurs st.spinner │
└─────────────┬─────────────┘
              │ File Object (BytesIO)
              ▼
┌───────────────────────────┐
│  Document Processor       │
│ (src/utils/               │
│   document_processor.py)  │
│  - extract_text_from_pdf()│
└─────────────┬─────────────┘
              │ pypdf PdfReader
              ▼
┌───────────────────────────┐
│        PDF File           │
│     (Parsing du texte)    │
└───────────────────────────┘
```

---

## 📦 Fichiers à Créer/Modifier

### 1. ✏️ MODIFIER : `requirements.txt`

**Ajout des dépendances pour le traitement PDF.**

```txt
# Traitement de documents (US-003)
pypdf==4.1.0
```

---

### 2. 🆕 CRÉER / MODIFIER : `src/utils/document_processor.py`

Création du module expert pour le nettoyage et l'extraction.

```python
"""Module de traitement et d'extraction de contenu documentaire"""

import io
from typing import Optional
from pypdf import PdfReader
from pypdf.errors import PdfReadError

class DocumentProcessor:
    """Classe utilitaire pour traiter les documents de voyage (ex: PDF)."""
    
    @staticmethod
    def extract_text_from_pdf(file_bytes: io.BytesIO) -> str:
        """
        Extrait le texte brut d'un fichier PDF et effectue un nettoyage de base.
        
        Args:
            file_bytes: Objet Bytestream du fichier (ex: issu d'un st.file_uploader)
            
        Returns:
            La chaîne de caractères nettoyée extraite du PDF.
            
        Raises:
            ValueError: Si le fichier est vide, illisible, corrompu ou d'un format non géré.
        """
        try:
            reader = PdfReader(file_bytes)
            
            if len(reader.pages) == 0:
                raise ValueError("Le document PDF ne contient aucune page.")
                
            extracted_text = []
            for num, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    extracted_text.append(text)
            
            full_text = "\n".join(extracted_text)
            
            if not full_text.strip():
                raise ValueError("Aucun texte lisible n'a pu être extrait. Il s'agit peut-être d'une image scannée.")
                
            # Nettoyage de base
            cleaned_text = " ".join(full_text.split())
            return cleaned_text
            
        except PdfReadError as e:
            raise ValueError(f"Le fichier PDF est corrompu ou illisible: {str(e)}")
        except Exception as e:
            raise ValueError(f"Erreur inattendue lors de la lecture du fichier: {str(e)}")
```

---

### 3. ✏️ MODIFIER : `src/app.py` (ou `src/chatbot/interface.py` selon délégation)

Ajout du composant de téléversement et gestion du fichier dans l'interface Streamlit existante.

```python
# À ajouter dans les imports 
from utils.document_processor import DocumentProcessor
import io

# Partie Interface Intégrée (ex: Sidebar ou zone de chat)
with st.sidebar: # Ou un expander dédié
    st.subheader("📄 Documents de voyage")
    uploaded_file = st.file_uploader(
        "Téléversez vos réservations, guides ou billets (PDF)", 
        type=["pdf"]
    )
    
    if uploaded_file is not None:
        with st.spinner('Analyse du document en cours...'):
            try:
                # Lecture via Streamlit retourne un objet BytesIO équivalent
                pdf_bytes = io.BytesIO(uploaded_file.getvalue())
                
                # Appel du module découplé
                extracted_text = DocumentProcessor.extract_text_from_pdf(pdf_bytes)
                
                # Indication de succès
                st.success(f"Document '{uploaded_file.name}' lu avec succès ! ({len(extracted_text)} caractères extraits)")
                
                # Conserver en mémoire de session
                if "uploaded_documents_text" not in st.session_state:
                    st.session_state.uploaded_documents_text = []
                
                # Éviter les doublons basiques
                if uploaded_file.name not in st.session_state.get("uploaded_documents_names", []):
                    st.session_state.uploaded_documents_text.append(extracted_text)
                    if "uploaded_documents_names" not in st.session_state:
                         st.session_state.uploaded_documents_names = []
                    st.session_state.uploaded_documents_names.append(uploaded_file.name)
                
            except ValueError as ve:
                st.error(f"Erreur de traitement : {str(ve)}")
```

---

### 4. 🆕 CRÉER : `tests/test_document_processor.py`

Mise en place des tests d'extraction et de gestion d'erreur.

```python
"""Tests unitaires pour le composant Document Processor"""
import pytest
import io
from src.utils.document_processor import DocumentProcessor

def generate_dummy_pdf(text: str) -> io.BytesIO:
    """Fonction utilitaire pour fabriquer un buffer PDF factice à la volée avec fpdf (si nécessaire) 
    Ou utiliser des fichiers statiques dans le dossier /tests/data/"""
    # Note au Coder : pour les tests, créer un dossier `tests/test_data/` contenant:
    # - sample_valid.pdf
    # - sample_empty.pdf
    # - sample_corrupted.pdf
    pass

def test_extract_text_valid_pdf():
    """Vérifier l'extraction correcte d'un texte simple."""
    # Instanciation de fichier bytes valide
    pass # Logique du test

def test_extract_text_handles_corrupted_file():
    """Vérifier qu'une exception ValueError claire est renvoyée pour des fichiers non-pdf/corrompus."""
    corrupted_bytes = io.BytesIO(b"Ceci n'est pas un pdf valide")
    with pytest.raises(ValueError) as exc:
        DocumentProcessor.extract_text_from_pdf(corrupted_bytes)
    assert "corrompu ou illisible" in str(exc.value)

def test_extract_text_handles_no_text_image_pdf():
    """Vérifier le comportement face à un PDF sans texte sélectionnable."""
    pass # Logique du test avec un PDF image
```

*(Note: Le CODER implémentera concrètement la génération ou l'import de mock PDF factices pour valider les assertions).*

---

## 🧪 Stratégie de Test & Assurance Qualité (Pour le QA)

### 1. Tests Automatisés
- Commande : `pytest tests/test_document_processor.py -v`
- Couverture attendue : 90% sur `document_processor.py` (Cas nominal + Cas d'erreur : Corrompu, Pas de texte, 0 pages).

### 2. Validation de l'IHM (Streamlit)
- Lancer l'app (`streamlit run src/app.py`).
- Mettre en ligne un **PDF Valide** : vérifier le spinner vert et message de succès.
- Mettre en ligne un **TXT renommé en PDF** : vérifier le message rouge élégant attrapant le `ValueError` sans crash console.
- Mettre en ligne un **PDF image scannée** (zéro texte) : vérifier le message "Aucun texte lisible".

---

## 📅 Estimation

- **Complexité** : 🟡 Moyenne (Mise en place de la brique Document + Streamlit uploaders)
- **Temps estimé** : 2-3 heures
- **Points de Story** : 5

---
**Versions** : 1.0  
**Validité P.O** : En attente
