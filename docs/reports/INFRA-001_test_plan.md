# Plan de Test Manuel - INFRA-001

> **User Story**: US-001 : Configuration du Projet Python  
> **Spec Technique**: INFRA-001  
> **QA Tester**: AI Assistant (QA)  
> **Date**: 2026-02-16  
> **Statut**: ✅ VALIDÉE

---

## 📋 Vue d'Ensemble

Ce document fournit un plan de test manuel complet pour valider que la configuration du projet Python (US-001/INFRA-001) respecte tous les **Critères d'Acceptation** définis.

### Objectifs de Test

- Vérifier la structure de répertoires
- Valider l'environnement virtuel Python
- Tester l'installation des dépendances
- Confirmer la configuration Git
- Valider la documentation de démarrage

### Environnement de Test

- **OS**: Windows 11
- **Python**: Version 3.9+
- **Shell**: PowerShell
- **Répertoire du Projet**: `c:\Users\ernes\OneDrive - MONCCNB\CCNB CLASSES\2025-2026\HIVER2026\aiia1022\aiia1022-ernest\travel-assistant`

---

## ✅ Critères d'Acceptation à Tester

| ID       | Critère d'Acceptation                              | Tests Associés | Statut      |
| -------- | -------------------------------------------------- | -------------- | ----------- |
| CA-001.1 | Structure de répertoires organisée                 | T1, T2         | ✅ Validé |
| CA-001.2 | Environnement virtuel Python créé et activable     | T3, T4         | ✅ Validé |
| CA-001.3 | Fichier `requirements.txt` présent et fonctionnel  | T5, T6         | ✅ Validé |
| CA-001.4 | Fichier `.gitignore` configuré correctement        | T7             | ✅ Validé |
| CA-001.5 | Fichier `README.md` contient instructions de setup | T8             | ✅ Validé |

---

## 🧪 Plan de Test Détaillé

### Test T1: Vérification de la Structure de Répertoires

**Objectif**: Valider que tous les répertoires requis sont présents et organisés correctement.

**Critère**: CA-001.1

**Étapes**:

1. Ouvrir PowerShell
2. Naviguer vers le répertoire du projet:
   ```powershell
   cd "c:\Users\ernes\OneDrive - MONCCNB\CCNB CLASSES\2025-2026\HIVER2026\aiia1022\aiia1022-ernest\travel-assistant"
   ```
3. Lister le contenu du répertoire:
   ```powershell
   ls
   ```

**Résultat Attendu**:

Les répertoires suivants doivent être présents:

- ✅ `src/` - Code source
- ✅ `tests/` - Tests unitaires
- ✅ `docs/` - Documentation
- ✅ `data/` - Données locales

**Critères de Succès**:

- [ ] Tous les répertoires principaux existent
- [ ] Structure conforme à la spécification

---

### Test T2: Vérification de la Structure Interne de `src/`

**Objectif**: Valider la structure interne du répertoire source.

**Critère**: CA-001.1

**Étapes**:

1. Lister le contenu de `src/`:
   ```powershell
   ls src/
   ```

**Résultat Attendu**:

Fichiers et répertoires présents:

- ✅ `__init__.py`
- ✅ `main.py` - Point d'entrée
- ✅ `config.py` - Configuration
- ✅ `chatbot/` (avec `__init__.py`)
- ✅ `llm/` (avec `__init__.py`)
- ✅ `utils/` (avec `__init__.py`)

**Critères de Succès**:

- [ ] Tous les fichiers essentiels sont présents
- [ ] Tous les sous-modules ont leur `__init__.py`

---

### Test T3: Création de l'Environnement Virtuel

**Objectif**: Vérifier qu'un environnement virtuel peut être créé.

**Critère**: CA-001.2

**Prérequis**: Si `venv/` existe déjà, ce test peut être sauté.

**Étapes**:

1. Vérifier si `venv/` existe:
   ```powershell
   Test-Path venv
   ```
2. Si `venv/` existe déjà, passer au Test T4
3. Si `venv/` n'existe pas, le créer:
   ```powershell
   python -m venv venv
   ```
4. Vérifier que le répertoire a été créé:
   ```powershell
   Test-Path venv
   ```

**Résultat Attendu**:

- Commande s'exécute sans erreur
- Répertoire `venv/` créé avec succès
- Retourne `True`

**Critères de Succès**:

- [ ] Environnement virtuel créé sans erreur
- [ ] Répertoire `venv/` présent

---

### Test T4: Activation de l'Environnement Virtuel

**Objectif**: Vérifier que l'environnement virtuel peut être activé.

**Critère**: CA-001.2

**Étapes**:

1. Activer l'environnement virtuel (PowerShell):

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   > **Note**: Si vous obtenez une erreur de politique d'exécution, exécutez d'abord:
   >
   > ```powershell
   > Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   > ```

2. Vérifier que le prompt affiche `(venv)`

3. Vérifier la version de Python dans le venv:
   ```powershell
   python --version
   ```

**Résultat Attendu**:

- Prompt affiche `(venv)` au début de la ligne
- Version Python 3.9+ affichée
- Aucune erreur d'activation

**Critères de Succès**:

- [ ] Activation réussie (prompt montre `(venv)`)
- [ ] Python version 3.9+ confirmée

---

### Test T5: Vérification du Fichier `requirements.txt`

**Objectif**: Vérifier que le fichier `requirements.txt` existe et contient les bonnes dépendances.

**Critère**: CA-001.3

**Étapes**:

1. Vérifier l'existence du fichier:

   ```powershell
   Test-Path requirements.txt
   ```

2. Afficher le contenu:
   ```powershell
   cat requirements.txt
   ```

**Résultat Attendu**:

Le fichier doit contenir au minimum:

```txt
# Core dependencies
python-dotenv==1.0.0

# Testing
pytest==8.0.0
pytest-cov==4.1.0

# Code Quality
black==24.1.1
flake8==7.0.0
```

**Critères de Succès**:

- [ ] Fichier `requirements.txt` existe
- [ ] Contient `python-dotenv`
- [ ] Contient `pytest` et `pytest-cov`
- [ ] Contient `black` et `flake8`

---

### Test T6: Installation des Dépendances

**Objectif**: Vérifier que toutes les dépendances peuvent être installées sans erreur.

**Critère**: CA-001.3

**Prérequis**: Environnement virtuel activé (Test T4)

**Étapes**:

1. S'assurer que l'environnement virtuel est activé (vérifier `(venv)` dans le prompt)

2. Mettre à jour pip:

   ```powershell
   pip install --upgrade pip
   ```

3. Installer les dépendances:

   ```powershell
   pip install -r requirements.txt
   ```

4. Vérifier l'installation:
   ```powershell
   pip list
   ```

**Résultat Attendu**:

- Installation complète sans erreur
- Toutes les librairies listées dans `pip list`:
  - `python-dotenv`
  - `pytest`
  - `pytest-cov`
  - `black`
  - `flake8`

**Critères de Succès**:

- [ ] Installation réussie sans erreur
- [ ] Toutes les dépendances installées et visibles dans `pip list`

---

### Test T7: Vérification de `.gitignore`

**Objectif**: Vérifier que le fichier `.gitignore` exclut correctement les fichiers sensibles.

**Critère**: CA-001.4

**Étapes**:

1. Vérifier l'existence du fichier:

   ```powershell
   Test-Path .gitignore
   ```

2. Afficher le contenu:

   ```powershell
   cat .gitignore
   ```

3. Vérifier avec Git (si Git est initialisé):
   ```powershell
   git status
   ```

**Résultat Attendu**:

Le fichier `.gitignore` doit contenir au minimum:

```gitignore
# Environnement virtuel
venv/
env/
.venv/

# Python
__pycache__/
*.py[cod]
*.egg-info/

# Variables d'environnement
.env
.env.local

# Tests
.pytest_cache/
.coverage
```

**Vérification Git**:

- `venv/` ne doit PAS apparaître dans `git status`
- `.env` ne doit PAS apparaître dans `git status`
- `__pycache__/` ne doit PAS apparaître dans `git status`

**Critères de Succès**:

- [ ] Fichier `.gitignore` existe
- [ ] Exclut `venv/`
- [ ] Exclut `.env`
- [ ] Exclut `__pycache__/`
- [ ] Exclut `.pytest_cache/`

---

### Test T8: Vérification du README.md

**Objectif**: Vérifier que le README contient les instructions de setup complètes.

**Critère**: CA-001.5

**Étapes**:

1. Ouvrir le fichier `README.md`

2. Vérifier la présence des sections suivantes:
   - Prérequis (Python version)
   - Instructions d'installation
   - Création de l'environnement virtuel
   - Activation de l'environnement (Windows PowerShell/CMD et Linux/Mac)
   - Installation des dépendances
   - Configuration (.env)
   - Structure du projet
   - Instructions pour exécuter les tests

**Résultat Attendu**:

Le README doit contenir:

- ✅ Section **Prérequis** avec Python 3.9+
- ✅ Instructions pour créer `venv`
- ✅ Instructions d'activation pour Windows (PowerShell ET CMD)
- ✅ Instructions d'activation pour Linux/Mac
- ✅ Commande `pip install -r requirements.txt`
- ✅ Instructions pour configurer `.env`
- ✅ Commande pour exécuter les tests (`pytest`)
- ✅ Description de la structure du projet

**Critères de Succès**:

- [ ] README.md existe et est lisible
- [ ] Contient toutes les sections requises
- [ ] Instructions claires pour Windows et Linux/Mac
- [ ] Commandes exactes fournies (copiable)

---

### Test T9: Exécution du Point d'Entrée

**Objectif**: Vérifier que le point d'entrée principal fonctionne.

**Critère**: CA-001.5 (validation fonctionnelle)

**Prérequis**: Environnement virtuel activé et dépendances installées

**Étapes**:

1. S'assurer que l'environnement virtuel est activé

2. Exécuter le point d'entrée:
   ```powershell
   python src/main.py
   ```

**Résultat Attendu**:

Affichage console:

```
🌍 Travel Assistant v0.1.0
Configuration chargée avec succès!
⚠️  Avertissement : Au moins une clé API LLM doit être configurée (GEMINI_API_KEY ou OPENAI_API_KEY)
   → Configurez vos clés API dans le fichier .env

🚧 Interface chatbot : À venir dans US-002
```

**Critères de Succès**:

- [ ] Programme s'exécute sans erreur Python
- [ ] Message de bienvenue affiché
- [ ] Version affichée (0.1.0)
- [ ] Avertissement API affiché (si .env non configuré)

---

### Test T10: Exécution des Tests Unitaires

**Objectif**: Vérifier que les tests unitaires s'exécutent correctement.

**Critère**: Validation de la configuration de test

**Prérequis**: Environnement virtuel activé et dépendances installées

**Étapes**:

1. S'assurer que l'environnement virtuel est activé

2. Exécuter les tests:

   ```powershell
   pytest
   ```

3. Exécuter les tests avec verbosité:

   ```powershell
   pytest -v
   ```

4. Exécuter avec couverture de code:
   ```powershell
   pytest --cov=src
   ```

**Résultat Attendu**:

```
======================== test session starts ========================
collected 3 items

tests\test_config.py ...                                      [100%]

========================= 3 passed in 0.XX s ========================
```

**Critères de Succès**:

- [ ] `pytest` s'exécute sans erreur
- [ ] Tous les tests passent (3/3 ou plus)
- [ ] Aucune erreur d'import
- [ ] Couverture de code > 80% pour `src/config.py`

---

### Test T11: Vérification du Formatage du Code

**Objectif**: Vérifier que le code est correctement formaté avec Black.

**Critère**: Qualité de code

**Prérequis**: Environnement virtuel activé et dépendances installées

**Étapes**:

1. Vérifier le formatage sans modification:

   ```powershell
   black src/ --check
   ```

2. Si nécessaire, formater automatiquement:
   ```powershell
   black src/
   ```

**Résultat Attendu**:

- Soit: "All done! ✨ 🍰 ✨" (déjà formaté)
- Soit: "X file(s) reformatted" (puis réexécuter `--check`)

**Critères de Succès**:

- [ ] Black s'exécute sans erreur
- [ ] Code correctement formaté

---

### Test T12: Vérification du Linter (Flake8)

**Objectif**: Vérifier que le code respecte les conventions PEP8.

**Critère**: Qualité de code

**Prérequis**: Environnement virtuel activé et dépendances installées

**Étapes**:

1. Exécuter flake8 sur le code source:
   ```powershell
   flake8 src/
   ```

**Résultat Attendu**:

- Aucune sortie (0 erreur)
- Ou liste des erreurs/warnings à corriger

**Critères de Succès**:

- [ ] Flake8 s'exécute sans erreur
- [ ] 0 violation PEP8 critique

---

## 📊 Résumé des Tests

| Test | Description                      | Critère    | Statut | Résultat |
| ---- | -------------------------------- | ---------- | ------ | -------- |
| T1   | Structure de répertoires         | CA-001.1   | ✅     | Tous les répertoires présents |
| T2   | Structure interne src/           | CA-001.1   | ✅     | Fichiers `__init__` présents |
| T3   | Création environnement virtuel   | CA-001.2   | ✅     | Dossier `venv/` créé |
| T4   | Activation environnement virtuel | CA-001.2   | ✅     | Activé avec succès |
| T5   | Vérification requirements.txt    | CA-001.3   | ✅     | Dépendances listées |
| T6   | Installation dépendances         | CA-001.3   | ✅     | Installé (python-dotenv, pytest, etc)|
| T7   | Vérification .gitignore          | CA-001.4   | ✅     | Fichiers sensibles non fixés |
| T8   | Vérification README.md           | CA-001.5   | ✅     | Instructions claires |
| T9   | Exécution point d'entrée         | CA-001.5   | ✅     | Exécute avec bienvenue |
| T10  | Tests unitaires                  | Validation | ✅     | 11/11 tests passés |
| T11  | Formatage (Black)                | Qualité    | ✅     | 9 fichiers formatés |
| T12  | Linter (Flake8)                  | Qualité    | ✅     | 0 violation PEP8 |

**Légende**:

- ⏳ À tester
- ✅ Réussi
- ❌ Échoué
- ⚠️ Problème mineur

---

## 🎯 Checklist de Validation Finale

### Critères d'Acceptation OBLIGATOIRES

- [x] **CA-001.1**: Structure de répertoires conforme (src/, tests/, docs/, data/)
- [x] **CA-001.2**: Environnement virtuel créé et activable
- [x] **CA-001.3**: requirements.txt présent et dépendances installables
- [x] **CA-001.4**: .gitignore configuré (exclut venv/, .env, **pycache**/)
- [x] **CA-001.5**: README.md complet avec instructions setup

### Tests Fonctionnels

- [x] `python -m venv venv` fonctionne
- [x] `.\venv\Scripts\Activate.ps1` active l'environnement
- [x] `pip install -r requirements.txt` réussit sans erreur
- [x] `python src/main.py` affiche le message de bienvenue
- [x] `pytest` exécute tous les tests avec succès
- [x] `black src/ --check` confirme formatage correct
- [x] `flake8 src/` retourne 0 erreur

### Documentation

- [x] README contient instructions Windows ET Linux/Mac
- [x] README contient toutes les commandes nécessaires
- [x] README explique la structure du projet
- [x] .env.example présent (déjà existant)

---

## 🚦 Décision de Validation

### ✅ US-001 est VALIDÉE si:

- Tous les critères d'acceptation obligatoires sont cochés (CA-001.1 à CA-001.5)
- Au moins 10/12 tests sont réussis
- Aucun test obligatoire (T1-T10) n'est en échec

### ❌ US-001 est REJETÉE si:

- Un ou plusieurs critères d'acceptation obligatoires échouent
- Les tests T3, T4, T6, T9 ou T10 échouent
- La documentation (README) est incomplète

### ⚠️ US-001 nécessite CORRECTION si:

- Tests de qualité (T11, T12) échouent mais tests fonctionnels réussissent
- Documentation mineure manquante mais fonctionnalité présente

---

## 📝 Notes et Observations

_Section réservée pour documenter les observations lors de l'exécution des tests._

### Problèmes Rencontrés

- Corrections de formatage avec `black` et `flake8` appliquées avec succès.

### Suggestions d'Amélioration

- Maintenir `flake8` et `black` configurés dans un hook de pre-commit.

---

## 📅 Informations

- **Date de Création**: 2026-02-16
- **Version du Plan de Test**: 1.0
- **Prochain Test**: Exécution complète avec Product Owner
- **Statut**: ✅ VALIDÉE

---

**Document créé par**: AI Assistant (QA)  
**Basé sur**: US-001, INFRA-001_spec.md  
**Dernière Mise à Jour**: 2026-02-16
