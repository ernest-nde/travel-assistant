# Spécification Technique : INFRA-003 - Intégration LLM

> **User Story** : US-004 : Intégration LLM (Google Gemini)  
> **ID Technique** : INFRA-003  
> **Architecte** : AI Assistant  
> **Date** : 2026-03-20  
> **Statut** : 📋 En Review

---

## 📝 Vue d'Ensemble

Cette spécification détaille l'implémentation de la **US-004 : Intégration LLM**. L'objectif est de connecter l'application au modèle Google Gemini, de gérer l'injection du texte extrait des PDF (US-003) en tant que contexte, et d'assurer une robustesse maximale face aux erreurs réseau via une *Retry Logic*.

### Rappel des Critères d'Acceptation

- ✅ **CA-004.1** : Connexion à l'API Google Gemini (ex: `gemini-1.5-flash`).
- ✅ **CA-004.2** : Gestion sécurisée de la clé `GEMINI_API_KEY` via le fichier `.env`.
- ✅ **CA-004.3** : Retry Logic pour pallier aux timeouts et limites de taux de requêtes (Rate Limits), avec fallback gracieux.
- ✅ **CA-004.4** : Concaténation du texte brut des documents PDF extraits avec le prompt utilisateur.
- ✅ **CA-004.5** : Tests unitaires mockant l'API pour valider la Retry Logic en toute sécurité.

---

## 🏗️ Architecture Proposée

L'intégration sera modularisée via un client dédié. Le client abstrait les appels à l'API Google et expose une interface propre à l'application Streamlit.

```text
┌───────────────────────────┐
│     Interface Utilisateur │ 
│     (src/app.py)          │
│  - Prompt utilisateur     │
│  - Documents PDF (texte)  │
└─────────────┬─────────────┘
              │ 
              ▼
┌───────────────────────────┐
│  LLM Client Module        │
│ (src/llm/gemini_client.py)│
│  - Retry Logic (@retry)   │
│  - Formatage du Prompt    │
│  - Fallback Handler       │
└─────────────┬─────────────┘
              │ (google-generativeai)
              ▼
┌───────────────────────────┐
│     Google Gemini API     │
└───────────────────────────┘
```

---

## 📦 Fichiers à Créer/Modifier

### 1. ✏️ MODIFIER : `requirements.txt`

Ajout des librairies nécessaires pour le LLM et la gestion des retries de manière professionnelle.

```txt
# LLM & Robustesse (US-004)
google-generativeai==0.4.0
tenacity==8.2.3
```

---

### 2. ✏️ MODIFIER : `.env.example` (et configurer `.env`)

Ajout de la clé d'API. Le `.gitignore` bloque déjà `.env`, garantissant que seules les variables d'exemple sont versionnées.

```env
# Google Gemini API
GEMINI_API_KEY=your_gemini_api_key_here
```

---

### 3. 🆕 CRÉER : `src/llm/__init__.py` et `src/llm/gemini_client.py`

Création du contrôleur d'API gérant la robustesse de l'appel LLM.

```python
"""Client d'intégration pour l'API Google Gemini."""

import os
import google.generativeai as genai
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

class GeminiAPIError(Exception):
    """Exception personnalisée pour les erreurs non récupérables de Gemini."""
    pass

class GeminiClient:
    """Client gérant les appels au modèle Gemini avec Retry Logic."""
    
    def __init__(self, model_name: str = "gemini-1.5-flash"):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("La clé GEMINI_API_KEY est introuvable dans l'environnement.")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name)

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception_type(Exception),
        reraise=True
    )
    def _call_api(self, prompt: str) -> str:
        """Méthode interne d'appel avec Retry exponentiel (max 3 tentatives)."""
        response = self.model.generate_content(prompt)
        return response.text

    def generate_response(self, user_prompt: str, context_documents: list[str] = None) -> str:
        """
        Génère une réponse LLM en injectant les documents si fournis.
        
        Args:
            user_prompt: La question de l'utilisateur.
            context_documents: Liste de textes extraits (ex: depuis les PDF).
        """
        full_prompt = ""
        
        # Injection du contexte des documents uploadés
        if context_documents:
            full_prompt += "CONTEXTE À PRENDRE EN COMPTE (Documents fournis) :\n"
            for doc in context_documents:
                full_prompt += f"---\n{doc}\n---\n"
            full_prompt += "\n"
        
        full_prompt += f"QUESTION DE L'UTILISATEUR :\n{user_prompt}"

        try:
            return self._call_api(full_prompt)
        except Exception as e:
            # Fallback gracieux après épuisement des retries
            return (
                "Je suis désolé, le service d'Intelligence Artificielle "
                "est momentanément indisponible ou surchargé. Veuillez réessayer dans quelques instants."
            )
```

---

### 4. ✏️ MODIFIER : `src/app.py`

Intégration du LLM dans la boucle de chat et transmission du texte des documents uploaddés.

```python
# Importations
from src.llm.gemini_client import GeminiClient

# Initialisation du client LLM (à mettre en cache via st.cache_resource)
@st.cache_resource
def get_llm_client():
    try:
        return GeminiClient()
    except ValueError as e:
        st.error(str(e))
        return None

llm = get_llm_client()

# Dans la boucle principale (gestion du st.chat_input)
if user_input := st.chat_input("Votre message..."):
    # Affichage prompt utilisateur... (déjà géré dans US-002)

    if llm:
        with st.chat_message("assistant"):
            with st.spinner("L'assistant réfléchit..."):
                # Récupérer les documents extraits du Session State (US-003)
                context_docs = st.session_state.get("uploaded_documents_text", [])
                
                # Appel à Gemini
                response = llm.generate_response(user_input, context_documents=context_docs)
                st.markdown(response)
                
                # Sauvegarde mémoire...
    else:
        st.error("L'assistant n'est pas configuré. Vérifiez votre clé d'API.")
```

---

### 5. 🆕 CRÉER : `tests/test_gemini_client.py`

Tests mockant l'API Google pour vérifier la création de l'objet, la levée de `ValueError` si clé absente, et le mécanisme de Retry.

```python
"""Tests unitaires pour l'intégration de Gemini."""
import pytest
from unittest.mock import patch
from src.llm.gemini_client import GeminiClient

def test_missing_api_key(monkeypatch):
    """Le système doit refuser de s'initialiser sans clé."""
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    with pytest.raises(ValueError):
         GeminiClient()

@patch('src.llm.gemini_client.genai.GenerativeModel.generate_content')
def test_successful_response(mock_generate, monkeypatch):
    """Test de réponse valide."""
    monkeypatch.setenv("GEMINI_API_KEY", "dummy_key")
    # Mocking standard...
    # Vérification d'un retour correct sans lever d'exception.

@patch('src.llm.gemini_client.genai.GenerativeModel.generate_content')
def test_retry_logic_and_fallback(mock_generate, monkeypatch):
    """Teste que le système tente X fois puis retourne le fallback courtois."""
    monkeypatch.setenv("GEMINI_API_KEY", "dummy_key")
    # Configurer le mock pour lever une Exception systématique
    mock_generate.side_effect = Exception("API Server Error")
    
    client = GeminiClient()
    feedback = client.generate_response("Test prompt")
    
    # Vérifier que le message de Fallback gracieux est bien retourné
    assert "momentanément indisponible" in feedback
    # Vérifier que la méthode a été appelée plusieurs fois (Retry de tenacity)
    assert mock_generate.call_count == 4 # 1 appel initial + 3 retries max
```

---

## 🧪 Stratégie de Test & Assurance Qualité (QA)

### 1. Tests Automatisés
- Commande : `pytest tests/test_gemini_client.py -v`
- Valide directement la logique complexe (`tenacity` retries et exceptions) **sans coût API**.

### 2. Validation IHM (Tests Manuels)
- **Scénario Nominal :** Démarrer l'app avec une clé API *valide*. Poser une question générale. Vérifier la réponse.
- **Scénario Documentaire (US-003 + US-004) :** Envoyer un PDF factice (par ex. un faux billet de train), puis poser la question "À quelle heure part mon train ?". L'assistant doit répondre correctement d'après le PDF (l'API prend quelques secondes pour réfléchir).
- **Scénario Erreur d'API :** Retirer la connexion internet temporairement ou mettre une fausse clé API. Taper un message. L'utilisateur doit voir le *Fallback gracieux*.

---

## 📅 Estimation

- **Complexité** : 🟡 Moyenne (Mélange de LLM pur et de résilience réseau).
- **Temps estimé** : 2.5 heures
- **Points de Story** : 5

---
**Version** : 1.0  
**Validité P.O** : En attente
