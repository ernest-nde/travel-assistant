# Spécification Technique - US-005 : Interaction Vocale (INFRA-009)

## 1. Objectif
Permettre à l'application Travel Assistant d'interagir par le son avec l'utilisateur. L'objectif principal de ce ticket est la synthèse vocale des réponses du chatbot (Text-to-Speech) afin d'offrir une expérience plus naturelle, avec potentiellement l'ajout de la dictée vocale (Speech-to-Text).

## 2. Approche Technique

### 2.1. Text-to-Speech (TTS) avec gTTS
- **Composant/Librairie** : Utilisation de la bibliothèque `gTTS` (Google Text-to-Speech) pour convertir le texte généré par notre intégration LLM (Gemini) en données audio (fichiers `.mp3` ou en octets `BytesIO`).
- **Création d'un service dédié** : Développer un utilitaire (ex: `src/utils/audio_manager.py`) qui expose une méthode de génération audio de façon asynchrone ou non-bloquante si possible. L'avantage d'utiliser un flux octet (`BytesIO`) est qu'il évite la création/suppression de multiples fichiers sur le disque dur.
- **Intégration Streamlit (IHM)** : Exploiter la méthode `st.audio()` de Streamlit dans le conteneur de message du "système/assistant". Cet afficheur de lecteur audio standard apparaîtra juste en dessous de la réponse textuelle.

### 2.2. Speech-to-Text (STT) - Aspect Optionnel (si intégration Streamlit possible)
- **Capture** : Utilisation d'un plugin Streamlit comme `audio_recorder_streamlit` pour créer un micro cliquable permettant à l'utilisateur de parler dans le navigateur.
- **Transcription** : Envoyer le fragment audio capturé soit à une API (ex: l'API Whisper, ou une capacité Gemini audio) soit un process local pour transcrire en texte. Le texte est ensuite traité comme un input régulier de l'utilisateur.
- *Note architecturale* : Cette étape est conditionnelle selon les difficultés de déploiement (le micro réclament souvent le https) et sera abordée après avoir sécurisé le TTS.

### 2.3. Gestion de la Résilience (Fallback textuel)
- La conversion TTS et les fonctions STT doivent être emballées dans des blocs `try/except` stricts.
- **Comportement attendu d'erreur** : Si l'API audio échoue, loggez l'erreur (pour les développeurs) et retournez au comportement nominal (le message s'affiche silencieusement en texte pour l'utilisateur sans rompre l'expérience).

## 3. Critères d'Acceptation Techniques & Dépendances
- Injection du paquet `gTTS` et (éventuellement) de `audio-recorder-streamlit` dans `requirements.txt`.
- Un mécanisme léger gérant la création audio est en place, sans laisser s'accumuler des centaines de MP3 inutiles sur le disque local de déploiement.

## 4. Tests d'Intégration / Cas d'Utilisation
- `Test TTS (Passant)` : Après la réponse de l'IA (ex: "Bienvenue à Paris"), l'interface Streamlit affiche le lecteur audio contenant la vocalisation de ce même texte.
- `Test TTS (Echec Réseau/API)` : La requête vers gTTS lève un Timeout -> Le composant audio Streamlit est masqué, le texte s'affiche quand même correctementement (Fallback Text).
