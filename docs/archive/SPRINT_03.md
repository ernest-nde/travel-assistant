# Rétrospective - SPRINT 03

**Date :** 20 mars 2026
**Thème du Sprint :** [Intégration du LLM, gestion des clés d'API et Retry Logic]

---

## 🧐 Questions Clés du Bilan

1. **La gestion sécurisée des clés secrètes (via le fichier `.env`) a-t-elle posé des difficultés lors du déploiement ou des tests locaux par l'équipe ?** *(Sécurité et Opérationnel)*
2. **La logique de "Retry" (relance en cas d'échec ou de timeout de l'API) s'est-elle avérée suffisamment robuste pour garantir une bonne expérience utilisateur ?** *(Robustesse)*
3. **Le format du texte extrait du PDF au sprint précédent s'est-il révélé optimal pour être digéré par l'API du LLM, ou a-t-il nécessité des ajustements (nettoyage) inattendus ?** *(Interopérabilité des modules)*

---

## 👥 Retours par Rôle

### 👔 [BA / Product Owner]
- **Réponses aux questions clés :**
  - **1. Sécurité :** L'approche via fichiers locaux `.env` ignorés par Git est le standard attendu, et protège nos quotas et coûts. C'est crucial pour la pérennité du MVP.
  - **2. Robustesse :** Le confort de l'utilisateur final dépend de cette tolérance aux pannes. Si le modèle ne répond pas de suite, l'utilisateur ne doit pas voir de code d'erreur brutal, mais avoir un délai géré proprement.
  - **3. Interopérabilité :** Le couplage de notre extracteur PDF avec la partie LLM représente le "cerveau" de l'application. Savoir que ces deux briques communiquent bien ensemble valide le choix architectural du sprint précédent.
- **Commentaires sur la valeur métier :**
  - Connecter l'application à un "vrai" modèle d'Intelligence Artificielle marque une énorme étape. Notre Chatbot passe du statut de simple interface à un véritable *Assistant de Voyage* intelligent. 

### 📐 [ARCHITECT]
- **Réponses aux questions clés :**
  - **1. Sécurité :** L'architecture reposant sur un fichier `.env` local exclus par Git (`.gitignore`) a parfaitement rempli son rôle. Le choix de lever une `ValueError` claire au démarrage du `GeminiClient` si la clé est manquante empêche les comportements imprévisibles de l'application.
  - **2. Robustesse :** L'intégration de la librairie `tenacity` comme décorateur (`@retry`) a permis de séparer la logique de résilience de la logique métier. Le système gagne en robustesse face aux quotas de l'API gratuite Gemini sans complexifier le code.
  - **3. Interopérabilité :** L'architecture modulaire du sprint précédent s'est avérée extrêmement bénéfique. Le texte brut nettoyé et renvoyé par le `document_processor.py` a pu être injecté nativement et sans transformation complexe directement dans le contexte du prompt envoyé au LLM.
- **Commentaires techniques / architecture :**
  - Le découplage strict entre l'interface Streamlit, le traitement PDF et le client LLM prouve l'efficacité de nos choix architecturaux initiaux. L'application reste hautement testable.

### 🔨 [CODER]
- **Réponses aux questions clés :**
  - **1. Sécurité :** L'approche `.env` combinée à la librairie native de gestion d'environnement fonctionne très bien. La vérification stricte au lancement de la classe `GeminiClient` garantit qu'on ne crashe pas silencieusement avec une erreur d'authentification tardive.
  - **2. Robustesse :** L'utilisation de `tenacity` a rendu le code d'appel API extrêmement élégant : quelques instructions décoratives suffisent pour gérer le "exponential backoff". Pour m'assurer que l'utilisateur voit bien le message de fallback gracieux après 3 échecs (sans pour autant consommer les quotas de Google), j'ai écrit un test mock complet qui simule l'erreur.
  - **3. Interopérabilité :** Le texte brut nettoyé en amont par le `DocumentProcessor` s'intègre parfaitement. J'ai simplement concaténé ce texte sous une balise textuelle "CONTEXTE À PRENDRE EN COMPTE (Documents fournis) :" avant la question utilisateur. Le LLM le digère très bien.
- **Commentaires sur le développement / le code :**
  - L'intégration de Gemini via le SDK officiel Python s'est faite vite. La couverture de tests avec les mocks (`test_gemini_client.py`) donne une grande confiance dans le système.

### 🕵️‍♀️ [QA]
- **Réponses aux questions clés :**
  - **1. Sécurité :** L'absence de clé a été interceptée avec succès lors de nos tests manuels (Test T2). L'alerte claire sur l'UI ("L'assistant n'est pas configuré") offre une excellente boucle de feedback sans exposer la stack trace à l'utilisateur final. L'utilisation du `.env` en local est parfaitement maîtrisée.
  - **2. Robustesse :** La logique de "Retry" couplée au message de repli a fait ses preuves (Test T3). Lors de l'erreur 404 rencontrée avec le modèle initial, l'application n'a pas planté : le fallback gracieux s'est affiché. J'ai même pu injecter l'erreur brute temporairement dans l'UI pour aider au débogage, confirmant la modularité du code d'erreur.
  - **3. Interopérabilité :** L'extraction brute de texte (issue du Sprint 2) est miraculeusement bien digérée par Gemini. Le Test T4 a confirmé que l'injection en contexte fonctionnait. L'ajout des boutons de Prompt Engineering proactifs ("Itinéraire 3J") démontre que le format texte extrait est optimal pour l'API.
- **Commentaires sur les tests / la qualité :**
  - Le plan de test manuel (`INFRA-003_test_plan.md`) est à 100% au vert. Tester l'UI Streamlit de manière automatisée par un sous-agent navigateur (qui téléverse un PDF physique et capture une capture d'écran de l'itinéraire généré) a apporté la preuve irréfutable de la qualité du livrable. Le projet est solide.

### 🚀 [DEVOPS]
- **Réponses aux questions clés :**
  - **1. Sécurité :** Le `.gitignore` a parfaitement filtré le `.env` local. La mise en place du fichier `.env.example` formalise proprement le "contrat d'environnement" pour qu'un nouveau dev puisse s'installer en sécurité. C'est une excellente validation du process `DevOps` initial.
  - **2. Robustesse :** L'intégration de la librairie `tenacity` a pu être gérée nativement via une simple mise à jour du `requirements.txt`. Cette approche de résilience (Retry et Fallback gracieux) diminue les risques d'alertes serveur (panics) sur notre future infrastructure de production, soulageant ainsi les besoins en monitoring.
  - **3. Interopérabilité :** Le footprint réseau pour transférer le texte extrait au LLM est minime. L'architecture actuelle (Upload en RAM -> Extraction -> Envoi API Text) est performante et n'exige pas de ressources cloud CPU ou mémoire importantes, gardant les coûts d'hébergement du MVP très bas.
- **Commentaires sur l'infrastructure / les outils :**
  - Ajout maîtrisé des librairies `google-generativeai` et `tenacity` au fichier `requirements.txt`. Les tests des différents clients maintiennent la base de code très saine sans complexité DevOps additionnelle.

---

## 🎯 Plan d'Action (Pour le prochain Sprint)

- [ ] Action 1 (Assigné à : )
- [ ] Action 2 (Assigné à : )
