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

Éditer `.env` et ajouter vos clés API (Obligatoire pour les fonctionnalités IA) :

```text
GEMINI_API_KEY=votre_cle_api_google_ici
```

## ▶️ Exécution

Puisqu'il s'agit d'une application Streamlit, lancez-la avec la commande suivante à la racine du projet :

```bash
streamlit run src/app.py
```
*(ou `python -m streamlit run src/app.py`)*

Un onglet s'ouvrira automatiquement dans votre navigateur par défaut à l'adresse `http://localhost:8501`.

### ⚠️ Notes de production importantes
- **Microphone (Speech-to-Text)** : Le widget d'enregistrement audio situé dans l'interface fonctionne très bien en local (`localhost`). Toutefois, en cas de déploiement Web, la plupart des navigateurs bloqueront l'accès au microphone si le serveur n'est pas sécurisé avec un certificat SSL (**HTTPS**).
- **Dépendances système (Linux)** : L'application utilise `SpeechRecognition`. Selon votre système d'exploitation, l'installation de bibliothèques C pour l'audio telles que `flac` ou `portaudio19-dev` peut être requise si une erreur de librairie externe survient.

## 🧪 Tests

```bash
pytest
```

Avec couverture :

```bash
pytest --cov=src
```