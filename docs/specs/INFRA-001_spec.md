# Spécification Technique : INFRA-001 - Configuration du Projet Python

> **User Story** : US-001 : Configuration du Projet Python  
> **ID Technique** : INFRA-001  
> **Architecte** : AI Assistant  
> **Date** : 2026-02-12  
> **Statut** : 📋 En Review

---

## 📝 Vue d'Ensemble

Cette spécification détaille l'implémentation de **US-001 : Configuration du Projet Python**, qui constitue le **prérequis fondamental** pour tous les développements futurs du Travel Assistant Chatbot.

### Objectif

Créer une base de projet Python professionnelle, structurée et maintenable avec :

- Une arborescence de fichiers claire et organisée
- Un environnement virtuel Python isolé
- Une gestion des dépendances via `requirements.txt`
- Une configuration Git appropriée
- Une documentation de démarrage complète

### Rappel des Critères d'Acceptation

- ✅ **CA-001.1** : Structure de répertoires organisée (src/, tests/, docs/, data/)
- ✅ **CA-001.2** : Environnement virtuel Python créé et activable
- ✅ **CA-001.3** : Fichier `requirements.txt` présent et fonctionnel
- ✅ **CA-001.4** : Fichier `.gitignore` configuré correctement
- ✅ **CA-001.5** : Fichier `README.md` avec instructions de setup

---

## 🏗️ Architecture Proposée

### Structure de Répertoires

La structure suivante sera créée dans le projet :

```
travel-assistant/
├── .env.example                 # ✅ EXISTE DÉJÀ
├── .gitignore                   # ✅ EXISTE DÉJÀ (à vérifier/compléter)
├── README.md                    # ✅ EXISTE DÉJÀ (à enrichir)
├── requirements.txt             # 🆕 À CRÉER
├── setup.py                     # 🆕 À CRÉER (optionnel mais recommandé)
├── backlog.md                   # ✅ EXISTE DÉJÀ
├── prompt_book.md              # ✅ EXISTE DÉJÀ
│
├── docs/                        # ✅ EXISTE DÉJÀ
│   ├── system_context.md       # ✅ EXISTE DÉJÀ
│   ├── user_stories.md         # ✅ EXISTE DÉJÀ
│   ├── specs/                  # ✅ EXISTE DÉJÀ
│   ├── reports/                # ✅ EXISTE DÉJÀ
│   ├── governance/             # ✅ EXISTE DÉJÀ
│   └── archive/                # ✅ EXISTE DÉJÀ
│
├── src/                         # ✅ EXISTE DÉJÀ (à structurer)
│   ├── __init__.py             # 🆕 À CRÉER
│   ├── main.py                 # 🆕 À CRÉER (point d'entrée)
│   ├── config.py               # 🆕 À CRÉER (configuration)
│   ├── chatbot/                # 🆕 À CRÉER (module chatbot)
│   │   └── __init__.py         # 🆕 À CRÉER
│   ├── llm/                    # 🆕 À CRÉER (module LLM)
│   │   └── __init__.py         # 🆕 À CRÉER
│   └── utils/                  # 🆕 À CRÉER (utilitaires)
│       └── __init__.py         # 🆕 À CRÉER
│
├── tests/                       # 🆕 À CRÉER
│   ├── __init__.py             # 🆕 À CRÉER
│   ├── test_config.py          # 🆕 À CRÉER
│   └── README.md               # 🆕 À CRÉER (guide tests)
│
├── data/                        # 🆕 À CRÉER (données)
│   ├── .gitkeep                # 🆕 À CRÉER
│   └── README.md               # 🆕 À CRÉER
│
└── venv/                        # 🆕 À CRÉER (environnement virtuel)
    └── (généré par Python)
```

### Justification de la Structure

- **`src/`** : Code source séparé des tests et docs (bonne pratique Python)
- **`tests/`** : Tests unitaires et d'intégration isolés
- **`docs/`** : Documentation et spécifications déjà existante
- **`data/`** : Données locales, fichiers de configuration, exports
- **`venv/`** : Environnement virtuel (sera exclu du versioning)

---

## 📦 Fichiers à Créer/Modifier

### 1. 🆕 CRÉER : `requirements.txt`

**Objectif** : Déclarer toutes les dépendances Python du projet

**Contenu Initial** :

```txt
# Core dependencies
python-dotenv==1.0.0

# Future dependencies (commentées pour MVP)
# streamlit==1.31.0          # Interface web conversationnelle
# google-generativeai==0.4.0 # LLM Google Gemini (gratuit)
# langchain==0.1.9           # Framework conversationnel
# openai==1.12.0             # Alternative LLM OpenAI
# requests==2.31.0           # Appels API externes

# Testing
pytest==8.0.0
pytest-cov==4.1.0

# Code Quality
black==24.1.1
flake8==7.0.0
```

**Rationale** :

- `python-dotenv` : Nécessaire dès maintenant pour `.env` (clés API)
- Autres dépendances commentées : ajoutées au fur et à mesure des US suivantes
- `pytest` : Framework de test standard Python
- `black` et `flake8` : Qualité et formatage du code

---

### 2. 🆕 CRÉER : `setup.py`

**Objectif** : Permettre l'installation du package en mode développement

**Contenu** :

```python
from setuptools import setup, find_packages

setup(
    name="travel-assistant",
    version="0.1.0",
    description="Travel Assistant Chatbot - Assistant de voyage conversationnel",
    author="CCNB Student",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=[
        "python-dotenv>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=8.0.0",
            "pytest-cov>=4.1.0",
            "black>=24.1.1",
            "flake8>=7.0.0",
        ]
    },
)
```

**Rationale** :

- Installation en mode éditable : `pip install -e .`
- Facilite les imports entre modules
- Sépare dépendances production et développement

---

### 3. ✏️ MODIFIER : `.gitignore`

**Objectif** : S'assurer que tous les fichiers sensibles/temporaires sont exclus

**Contenu à Vérifier/Ajouter** :

```gitignore
# Environnement virtuel
venv/
env/
ENV/
.venv/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Variables d'environnement
.env
.env.local

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Tests
.pytest_cache/
.coverage
htmlcov/
.tox/

# OS
.DS_Store
Thumbs.db

# Données sensibles
data/*.csv
data/*.json
!data/README.md
```

**Action** : Vérifier le `.gitignore` existant et compléter si nécessaire

---

### 4. ✏️ ENRICHIR : `README.md`

**Objectif** : Documenter le setup et le démarrage du projet

**Sections à Ajouter/Compléter** :

````markdown
# Travel Assistant Chatbot 🌍✈️

Assistant de voyage conversationnel intelligent basé sur l'IA.

## 📋 Prérequis

- **Python** : Version 3.9 ou supérieure
- **pip** : Gestionnaire de paquets Python
- **Git** : Pour le versioning (optionnel)

## 🚀 Installation

### 1. Cloner le Projet (ou télécharger)

```bash
git clone <url-du-repo>
cd travel-assistant
```
````

### 2. Créer l'Environnement Virtuel

**Windows (PowerShell)** :

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (CMD)** :

```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**Linux/Mac** :

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les Dépendances

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configuration (Variables d'Environnement)

Copier le fichier `.env.example` en `.env` :

```bash
cp .env.example .env
```

Éditer `.env` et ajouter vos clés API (pour US-003) :

```
GEMINI_API_KEY=your_api_key_here
```

## 🧪 Tests

```bash
pytest
```

Avec couverture :

```bash
pytest --cov=src
```

## 📂 Structure du Projet

```
travel-assistant/
├── src/           # Code source
├── tests/         # Tests unitaires
├── docs/          # Documentation
├── data/          # Données locales
└── venv/          # Environnement virtuel (ignoré par Git)
```

## 📝 Documentation

- **Contexte Système** : `docs/system_context.md`
- **User Stories** : `docs/user_stories.md`
- **Spécifications** : `docs/specs/`

## 🤝 Contribution

Ce projet suit une méthodologie Agile avec 5 rôles :

- Business Analyst
- Architect
- Coder
- QA
- DevOps

Voir `prompt_book.md` pour les prompts de chaque rôle.

## 📄 Licence

Projet éducatif - CCNB AIIA1022

````

---

### 5. 🆕 CRÉER : Fichiers Python de Structure

#### `src/__init__.py`
```python
"""Travel Assistant Chatbot - Package principal"""
__version__ = "0.1.0"
````

#### `src/config.py`

```python
"""Configuration du projet"""
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()


class Config:
    """Configuration centralisée de l'application"""

    # Version
    VERSION = "0.1.0"

    # API Keys
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

    # Chemins
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(ROOT_DIR, "data")

    # Debug mode
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    @classmethod
    def validate(cls):
        """Valide la configuration minimale"""
        if not cls.GEMINI_API_KEY and not cls.OPENAI_API_KEY:
            raise ValueError(
                "Au moins une clé API LLM doit être configurée "
                "(GEMINI_API_KEY ou OPENAI_API_KEY)"
            )
```

#### `src/main.py`

```python
"""Point d'entrée principal de l'application"""
from config import Config


def main():
    """Fonction principale"""
    print(f"🌍 Travel Assistant v{Config.VERSION}")
    print("Configuration chargée avec succès!")

    # Validation de la configuration (sera utilisée avec US-003)
    try:
        Config.validate()
        print("✅ Configuration API validée")
    except ValueError as e:
        print(f"⚠️  Avertissement : {e}")
        print("   → Configurez vos clés API dans le fichier .env")

    print("\n🚧 Interface chatbot : À venir dans US-002")


if __name__ == "__main__":
    main()
```

#### `src/chatbot/__init__.py`, `src/llm/__init__.py`, `src/utils/__init__.py`

```python
"""Module [nom du module]"""
# Contenu initial vide, sera rempli dans les prochaines US
```

#### `tests/__init__.py`

```python
"""Tests du Travel Assistant"""
```

#### `tests/test_config.py`

```python
"""Tests de la configuration"""
import pytest
from src.config import Config


def test_config_version():
    """Vérifie que la version est définie"""
    assert Config.VERSION == "0.1.0"


def test_config_paths_exist():
    """Vérifie que les chemins de configuration sont valides"""
    assert Config.ROOT_DIR is not None
    assert Config.DATA_DIR is not None


def test_config_debug_mode():
    """Vérifie le mode debug"""
    assert isinstance(Config.DEBUG, bool)
```

#### `tests/README.md`

````markdown
# Tests - Travel Assistant

## Exécuter les Tests

```bash
# Tous les tests
pytest

# Tests avec verbosité
pytest -v

# Tests avec couverture
pytest --cov=src

# Un fichier spécifique
pytest tests/test_config.py
```
````

## Structure

- `test_*.py` : Tests unitaires
- Chaque module dans `src/` aura son fichier de test correspondant

````

#### `data/README.md`
```markdown
# Data Directory

Ce répertoire contient les données locales du projet :

- Fichiers de configuration supplémentaires
- Données de test
- Logs
- Exports d'itinéraires (à venir)

**Note** : Les fichiers de données sensibles sont exclus du versioning via `.gitignore`.
````

#### `data/.gitkeep`

```
# Fichier vide pour forcer Git à inclure le répertoire data/
```

---

## 📚 Nouvelles Librairies Nécessaires

### Dépendances Immédiates (US-001)

| Librairie       | Version | Objectif                             | Installation                       |
| --------------- | ------- | ------------------------------------ | ---------------------------------- |
| `python-dotenv` | 1.0.0   | Chargement variables d'environnement | `pip install python-dotenv==1.0.0` |
| `pytest`        | 8.0.0   | Framework de tests                   | `pip install pytest==8.0.0`        |
| `pytest-cov`    | 4.1.0   | Couverture de tests                  | `pip install pytest-cov==4.1.0`    |
| `black`         | 24.1.1  | Formatage de code                    | `pip install black==24.1.1`        |
| `flake8`        | 7.0.0   | Linter Python                        | `pip install flake8==7.0.0`        |

### Dépendances Futures (à venir dans prochaines US)

Ces dépendances seront ajoutées au fur et à mesure :

- **US-002** : `streamlit` (interface web)
- **US-003** : `google-generativeai` ou `openai` (LLM)
- **US-004** : `langchain`, `langchain-community` (gestion contexte)
- **US-005+** : `requests`, bibliothèques API externes

### Justification des Choix

- **python-dotenv** : Standard pour gestion des secrets et configuration
- **pytest** : Framework de test le plus populaire en Python
- **black** : Formatage automatique zéro-configuration
- **flake8** : Vérification du respect des conventions PEP8

---

## 🧪 Stratégie de Test

### Tests pour US-001

#### 1. Tests Automatisés

**Fichier** : `tests/test_config.py`

**Tests à implémenter** :

1. ✅ **test_config_version** : Vérifie que la version est définie
2. ✅ **test_config_paths_exist** : Vérifie que les chemins sont valides
3. ✅ **test_config_debug_mode** : Vérifie le mode debug
4. 🆕 **test_config_load_dotenv** : Vérifie le chargement du fichier `.env`

**Commande d'exécution** :

```bash
pytest tests/test_config.py -v
```

#### 2. Tests Manuels

**Checklist de Validation Manuelle** :

| #   | Test                               | Commande                          | Résultat Attendu                             |
| --- | ---------------------------------- | --------------------------------- | -------------------------------------------- |
| 1   | Création environnement virtuel     | `python -m venv venv`             | Répertoire `venv/` créé                      |
| 2   | Activation environnement (Windows) | `.\venv\Scripts\Activate.ps1`     | Prompt affiche `(venv)`                      |
| 3   | Installation dépendances           | `pip install -r requirements.txt` | Toutes les librairies installées sans erreur |
| 4   | Exécution point d'entrée           | `python src/main.py`              | Message de bienvenue affiché                 |
| 5   | Exécution tests                    | `pytest`                          | Tous les tests passent (vert)                |
| 6   | Vérification .gitignore            | `git status`                      | `venv/` et `.env` ne sont pas trackés        |
| 7   | Formatage code                     | `black src/ --check`              | Code déjà formaté ou formatage réussi        |
| 8   | Vérification linter                | `flake8 src/`                     | Aucune erreur PEP8                           |

#### 3. Critères de Succès

**US-001 est validée si** :

- ✅ Tous les répertoires sont créés
- ✅ Environnement virtuel fonctionne (activation/désactivation)
- ✅ `pip install -r requirements.txt` s'exécute sans erreur
- ✅ `python src/main.py` affiche le message de bienvenue
- ✅ `pytest` exécute tous les tests avec succès
- ✅ Le fichier `.gitignore` exclut bien `venv/` et `.env`
- ✅ Le `README.md` contient les instructions claires

---

## 📋 Instructions d'Implémentation (pour le CODER)

### Ordre d'Exécution Recommandé

1. **Créer les répertoires manquants** :

   ```bash
   mkdir -p tests data
   mkdir -p src/chatbot src/llm src/utils
   ```

2. **Créer les fichiers de structure** :
   - Tous les `__init__.py`
   - `src/config.py`
   - `src/main.py`
   - `data/README.md`, `data/.gitkeep`
   - `tests/README.md`, `tests/test_config.py`

3. **Créer `requirements.txt`**

4. **Créer `setup.py`**

5. **Mettre à jour `.gitignore`** (vérifier et compléter)

6. **Enrichir `README.md`** avec les instructions d'installation

7. **Créer l'environnement virtuel et tester** :
   ```bash
   python -m venv venv
   source venv/bin/activate  # ou .\venv\Scripts\Activate.ps1 sur Windows
   pip install --upgrade pip
   pip install -r requirements.txt
   python src/main.py
   pytest
   ```

---

## ⚠️ Points d'Attention

### Contraintes Techniques

- **Version Python** : Minimum 3.9+ (pour compatibilité avec librairies futures)
- **Système** : Compatible Windows, Linux, Mac
- **Encodage** : UTF-8 pour tous les fichiers

### Risques et Limitations

- **Risque** : Conflit de versions de librairies
  - **Mitigation** : Versions fixées dans `requirements.txt`
- **Risque** : Problème d'activation de `venv` sur Windows (politique d'exécution)
  - **Mitigation** : Instructions pour `Set-ExecutionPolicy` dans le README

- **Limitation** : Configuration minimale pour US-001
  - Les librairies LLM seront ajoutées dans US-003

### Dépendances Bloquantes

Aucune - US-001 est le point de départ du projet.

---

## 📅 Estimation

- **Complexité** : 🟢 Faible
- **Temps estimé** : 1-2 heures
- **Points de Story** : 2

---

## ✅ Checklist de Validation (pour le QA)

- [ ] Structure de répertoires créée et conforme
- [ ] Environnement virtuel fonctionne
- [ ] `requirements.txt` installe toutes les dépendances sans erreur
- [ ] `.gitignore` exclut bien `venv/`, `.env`, `__pycache__/`
- [ ] `README.md` contient instructions claires pour Windows et Linux/Mac
- [ ] `python src/main.py` s'exécute et affiche message de bienvenue
- [ ] `pytest` exécute les tests avec succès
- [ ] Fichier `.env.example` présent (déjà existant)
- [ ] `black` et `flake8` s'exécutent sans erreur

---

## 📊 Indicateurs de Réussite

- **Couverture de tests** : Minimum 80% pour `src/config.py`
- **Qualité de code** : 0 erreur `flake8`
- **Documentation** : README complet et testé

---

**Date de création** : 2026-02-12  
**Version** : 1.0  
**Statut** : 📋 En Review - Prêt pour validation Product Owner
