# Synthèse de la Rétrospective - Sprint 04

## 1. Ce qui a bien fonctionné (Succès)
- **Choix techniques optimaux** : L'utilisation de la bibliothèque légère `gTTS` avec une restitution directe en mémoire (`BytesIO`) a permis une intégration extrêmement rapide, non-destructrice, et a facilité le déploiement en évitant la gestion de fichiers temporaires sur le serveur.
- **Robustesse et Qualité** : L'architecture s'est avérée résiliente, notamment avec un comportement de dégradation gracieuse (*fallback* textuel évalué par la QA) qui empêche l'application de crasher si le service de synthèse venait à échouer.

## 2. Difficultés et Blocages (Défis)
- **Problème de Nomenclature** : La dualité et l'ambiguïté des identifiants existants (US-005 vs INFRA-004) ont généré de la friction lors de la rédaction documentaire et du suivi (historique Git, CHANGELOG).
- **Omission de Dépendances** : Un oubli d'ajouter `SpeechRecognition` au fichier `requirements.txt` a causé un crash initial (*ModuleNotFoundError*), soulevant des problèmes de rigueur dans l'environnement.
- **Limites de l'Interface UI (Streamlit)** : L'utilisation du composant `audio-recorder-streamlit` pour le **Speech-to-Text** s'est heurtée à des limitations d'UX (intégration difficile au *chat_input*) et à l'absence de vérification des certificats HTTPS (contrainte navigateur pour le micro).

## 3. Plan d'Action pour le Prochain Sprint
Afin de fluidifier le cycle de développement et pallier ces difficultés, les actions suivantes sont planifiées :
1. **Nomenclature** : Adopter une convention stricte et unique comme source de vérité (soit toujours `US-XX`, soit toujours `INFRA-XX`) pour les branches Git et la documentation (Architect/DevOps).
2. **Infrastructure et CI** :
   - Introduire une vérification automatique (CI ou hook pre-commit) pour valider que le `requirements.txt` est bien synchronisé (DevOps/QA).
   - Anticiper et préparer le contexte HTTPS requis pour faire fonctionner le composant d'enregistrement audio (Speech-to-Text) (Architect/DevOps).
3. **Tests et Code** :
   - Systématiser des "sanity checks" avant la soumission de paquets (Coder).
   - Développer des tests unitaires/d'intégration automatisés (mocks API via pytest) pour la classe `AudioManager` (Coder/QA).
   - Explorer des alternatives d'interface UI avancées (via des Streamlit Components personnalisés) pour parfaire l'expérience micro (Coder).
