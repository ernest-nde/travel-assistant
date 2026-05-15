# Plan de Test Manuel - US-005 : Interaction Vocale (TTS)

## 1. Objectif
Le système doit être capable de synthétiser vocalement les réponses textuelles du chatbot à l'aide de Google Text-to-Speech (gTTS) afin d'offrir une expérience utilisateur améliorée, tout en assurant un comportement résilient (fallback textuel) en cas de panne de l'API vocale.

## 2. Prérequis
- Le serveur Streamlit est en cours d'exécution.
- La bibliothèque `gTTS` est installée (et potentiellement les dépendances liées au micro).
- Périphérique de lecture audio activé.

## 3. Scénarios et Cas de Test (Checklist)

### 3.1. Test Nominal - Génération Vocale (Passant)
- [x] **Action :** Envoyer un message au chatbot pour provoquer une réponse (ex: "Bonjour" ou "Dis-moi une information sur Paris").
- [x] **Résultat Attendu :** L'interface affiche la réponse sous forme de texte ET présente un lecteur audio en dessous. Cliquer sur 'Play' déclenche la lecture audio de la réponse. La génération n'encombre pas le disque dur si `BytesIO` est bien utilisé.
- [x] **Statut :** Succès

### 3.2. Test de Résilience - Échec API / Déconnexion Réseau (Fallback)
- [x] **Action :** Provoquer une erreur dans l'agent TTS (soit en coupant le réseau au moment de la synthèse, soit en injectant une exception volontaire dans le code de génération de la voix `gTTS`).
- [x] **Résultat Attendu :** L'application ne "crashe" pas (pas de traceback Streamlit visible par l'utilisateur). Le widget audio est simplement ignoré et la réponse s'affiche uniquement sous forme textuelle de façon transparente.
- [x] **Statut :** Succès

### 3.3. Test de Flux Mémoire (Vérification stockage)
- [x] **Action :** Effectuer plusieurs requêtes TTS successives.
- [x] **Résultat Attendu :** Le dossier de l'application ou /tmp ne se remplit pas avec d'innombrables fichiers `.mp3`, validant le flux transitoire `BytesIO`.
- [x] **Statut :** Succès

### 3.4. (Optionnel) Test Speech-to-Text STT (Si activé par les développeurs)
- [x] **Action :** Cliquer sur le composant microphone dans l'IHM et dicter "Quelle est la capitale de l'Italie?".
- [x] **Résultat Attendu :** Le son est pris, transformé en texte, et envoyé au chatbot. La réponse du chatbot est normale et synthétisée vocalement. (Cette section ne sera testée que si le composant a été intégré).
- [x] **Statut :** Succès
