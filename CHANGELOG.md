# Changelog - Travel Assistant

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

---

## [Non publié]

---

## [0.7.0] - 2026-04-06

### ✨ Interface Graphique Premium (US-007 / INFRA-006)

#### Module Principal
- Refonte visuelle complète de l'interface Streamlit (CSS personnalisé, Mode Sombre optimisé).
- Intégration d'une bannière et mise en page en bulles de chat design.
- Alignement amélioré pour les métriques de sentiment et le module vocal.

#### Tests et Qualité
- Validation complète de la non-régression et du responsive via `docs/reports/INFRA-006_test_plan.md`.
- Spécifications techniques documentées dans `docs/specs/INFRA-006_spec.md`.

---

## [0.6.0] - 2026-04-04

### 🎭 Analyse de Sentiment Visuelle (US-006 / INFRA-005)

#### Module Principal
- Intégration de `textblob-fr` pour l'analyse lexicale du sentiment des requêtes utilisateurs (score de polarité entre -1 et 1).
- Création d'une jauge visuelle colorée et d'emojis dynamiques dans l'interface Streamlit reflétant l'humeur de l'utilisateur (Positif, Neutre, Négatif).

#### Tests et Qualité
- Validation complète via le plan de test `docs/reports/INFRA-005_test_plan.md`.
- Rédaction des spécifications `docs/specs/INFRA-005_spec.md`.

---

## [0.5.0] - 2026-04-02

### 🗣️ Interaction Vocale et Synthèse (INFRA-004 / US-005)

#### Module Principal
- **src/audio/audio_manager.py** : Ajout du module de synthèse vocale (TTS) utilisant `gTTS` pour générer les réponses audio.
- **src/app.py** : Intégration de l'interaction vocale dans l'interface Streamlit.

#### Tests et Qualité
- Création du plan de test `docs/reports/INFRA-004_test_plan.md` (Interaction Vocale).
- Rédaction des spécifications `docs/specs/INFRA-004_spec.md`.

---

## [0.4.0] - 2026-03-23

### 🧠 Intégration LLM Google Gemini (INFRA-003)

#### Module Principal
- **src/llm/gemini_client.py** : Client pour interagir avec l'API Google Gemini, incluant une logique de `retry` (Tenacity) pour la résilience.

#### Tests et Qualité
- Ajout de tests unitaires : `tests/test_gemini_client.py`
- Ajout d'un script de diagnostic : `tests/diag_gemini.py`
- Création du plan de test `docs/reports/INFRA-003_test_plan.md` pour validation de la charge et des erreurs (timeouts).

---

## [0.3.0] - 2026-03-11

### 📄 Traitement de Documents PDF (INFRA-002)

#### Module Principal
- **src/document_processor.py** : Classe `DocumentProcessor` pour extraire et nettoyer le texte des fichiers PDF.
- **src/app.py** : Intégration globale ou point d'entrée pour l'application enrichie.

#### Tests et Qualité
- Ajout de tests unitaires : `tests/test_document_processor.py`, `tests/test_interface.py`
- Ajout de scripts de génération de tests : `tests/generate_test_pdfs.py` et données de test dans `tests/test_data/`
- Création du plan de test `docs/reports/INFRA-002_test_plan.md` pour l'interface Chatbot.

---

## [0.2.0] - 2026-02-26

### 🤖 Interface Chatbot (INFRA-002)

#### Web Interface

- Intégration de `streamlit` (v1.31.0) dans les dépendances (`requirements.txt`, `setup.py`)
- **src/chatbot/interface.py** : Gestionnaire d'interface de chat (formatage message, session, historique, remise à zéro)

#### Configuration Global

- Mise à jour de `.gitignore` et autre doc

---

## [0.1.0] - 2026-02-16

### 🏗️ Infrastructure du Projet (INFRA-001)

#### Structure du Projet

- **src/** : Module principal de code source
  - `__init__.py` : Package principal (v0.1.0)
  - `config.py` : Configuration centralisée avec support .env
  - `main.py` : Point d'entrée de l'application
  - `chatbot/__init__.py` : Module chatbot (préparé pour US-002)
  - `llm/__init__.py` : Module LLM (préparé pour US-003)
  - `utils/__init__.py` : Utilitaires

#### Tests

- **tests/** : Infrastructure de tests
  - `__init__.py` : Package de tests
  - `test_config.py` : Tests unitaires de configuration (3 tests)
  - `README.md` : Guide d'exécution des tests

#### Configuration Python

- `requirements.txt` : Dépendances du projet
  - python-dotenv==1.0.0
  - pytest==8.0.0, pytest-cov==4.1.0
  - black==24.1.1, flake8==7.0.0
- `setup.py` : Configuration du package Python (v0.1.0)
- `.gitignore` : Exclusions Git (venv/, .env, **pycache**, etc.)

#### Documentation

- **docs/specs/** : Spécifications techniques
  - INFRA-001 à INFRA-008 : Spécifications d'infrastructure complètes
- **docs/reports/** : Rapports et plans de test
  - `INFRA-001_test_plan.md` : Plan de test QA (12 tests détaillés)
- **docs/governance/** : Gouvernance du projet
  - `roles.md` : Définition des rôles Agile
  - `protocols.md` : Protocoles de développement
- `docs/system_context.md` : Contexte système et vision
- `docs/user_stories.md` : User stories du projet

#### Fichiers Projet

- `CHANGELOG.md` : ✨ Ce fichier (suivi des versions)
- `README.md` : Instructions d'installation et setup
- `backlog.md` : Backlog produit complet
- `prompt_book.md` : Guide des prompts pour les 5 rôles
- `.env.example` : Template de configuration

#### Données

- **data/** : Répertoire de données
  - `.gitkeep` : Maintien du répertoire dans Git
  - `README.md` : Documentation du répertoire data

### 🧪 Qualité et Tests

- Plan de test manuel QA avec 12 tests couvrant tous les critères d'acceptation
- Tests unitaires automatisés pour la configuration
- Support Black et Flake8 pour qualité de code

### 📝 Documentation

- Documentation complète d'installation (Windows, Linux, Mac)
- Structure de projet professionnelle et maintenable
- Spécifications techniques détaillées pour 8 composants d'infrastructure

### 🔧 DevOps

- Configuration Git complète avec .gitignore
- Premier commit et push vers dépôt distant
- Changelog initialisé selon Keep a Changelog

---

## Format de référence

### [Version] - YYYY-MM-DD

#### Ajouté

- Nouvelles fonctionnalités

#### Modifié

- Changements dans les fonctionnalités existantes

#### Déprécié

- Fonctionnalités qui seront bientôt retirées

#### Retiré

- Fonctionnalités retirées

#### Corrigé

- Corrections de bugs

#### Sécurité

- Changements liés à la sécurité

---

**Dernière mise à jour** : 02 avril 2026
