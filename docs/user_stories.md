# User Stories - Travel Assistant Chatbot

> **Document de Spécification des Besoins Utilisateurs**
>
> Ce document transforme les items du backlog en User Stories détaillées avec critères d'acceptation clairs pour guider le développement.

---

## 📋 Priorités MVP (Minimum Viable Product)

Les User Stories suivantes constituent le **socle fondamental** du Travel Assistant Chatbot et doivent être développées en priorité.

---

## 🏗️ US-001 : Configuration du Projet Python (INFRA-001)

### User Story

**En tant que** développeur,  
**Je veux** un projet Python correctement structuré avec un environnement virtuel et des dépendances gérées,  
**Afin de** poser les bases techniques du chatbot et faciliter le développement futur.

### Priorité

🔴 **CRITIQUE** - Prérequis pour toutes les autres fonctionnalités

### Critères d'Acceptation

✅ **CA-001.1** : Le projet possède une structure de répertoires organisée

- Répertoire `src/` pour le code source
- Répertoire `tests/` pour les tests
- Répertoire `docs/` pour la documentation
- Répertoire `data/` pour les données (si nécessaire)

✅ **CA-001.2** : Un environnement virtuel Python est créé et activable

- Commande documentée pour créer l'environnement (ex: `python -m venv venv`)
- Instructions pour l'activation (Windows et Linux/Mac)

✅ **CA-001.3** : Fichier `requirements.txt` présent et fonctionnel

- Liste toutes les dépendances nécessaires
- Installation possible via `pip install -r requirements.txt`

✅ **CA-001.4** : Fichier `.gitignore` configuré correctement

- Exclut `venv/`, `__pycache__/`, `.env`, etc.

✅ **CA-001.5** : Fichier `README.md` contient les instructions de setup

- Instructions d'installation de l'environnement
- Liste des prérequis (version Python, etc.)
- Commandes de base pour démarrer

### Notes Techniques

- Version Python recommandée : 3.9+
- Dépendances potentielles initiaux : openai, google-generativeai, streamlit, python-dotenv

### Dépendances

Aucune - C'est le point de départ du projet

---

## 💬 US-002 : Interface Chatbot de Base (INFRA-002)

### User Story

**En tant qu'** utilisateur voyageur,  
**Je veux** pouvoir dialoguer avec le chatbot via une interface simple,  
**Afin de** communiquer mes besoins de voyage de manière naturelle.

### Priorité

🔴 **CRITIQUE** - Interface utilisateur fondamentale

### Critères d'Acceptation

✅ **CA-002.1** : Interface conversationnelle fonctionnelle

- L'utilisateur peut écrire des messages
- Les réponses du chatbot s'affichent clairement
- Historique de conversation visible

✅ **CA-002.2** : Choix de l'interface implementée

- **Option A** : CLI (Command Line Interface) pour prototype rapide, OU
- **Option B** : Interface web avec Streamlit ou Gradio

✅ **CA-002.3** : Gestion de session de base

- Une nouvelle conversation démarre proprement
- L'historique est maintenu pendant la session
- Option de réinitialiser la conversation

✅ **CA-002.4** : Interface réactive et facile d'utilisation

- Temps de réponse acceptable (< 3 secondes pour affichage)
- Messages d'erreur clairs si problème
- Instructions minimales pour l'utilisateur

✅ **CA-002.5** : Documentation d'utilisation

- Guide pour lancer l'interface
- Exemples de commandes/questions de base

### Notes Techniques

- Recommandation : Streamlit pour simplicité et rapidité de développement
- Alternative : Gradio si préférence pour interface plus customisable

### Dépendances

- US-001 (Configuration projet Python)

---

## 📄 US-003 : Traitement de Documents PDF (INFRA-008)

### User Story

**En tant qu'** utilisateur voyageur,  
**Je veux** pouvoir téléverser mes documents de voyage au format PDF (billets, réservations, guides),  
**Afin que** le chatbot puisse en extraire le contenu brut et l'utiliser pour contextualiser ses réponses.

### Priorité

🔴 **CRITIQUE** - Définie comme l'objectif central du Sprint 02 par le Product Owner.

### Critères d'Acceptation

✅ **CA-009.1** : Module de traitement indépendant
- La logique d'extraction est isolée dans un module dédié : `src/utils/document_processor.py` (modularité).
- Le module utilise la bibliothèque `pypdf` pour l'extraction de texte.

✅ **CA-009.2** : Fonction d'extraction de texte
- Le système peut lire avec succès le texte de fichiers PDF standard (contenant du texte sélectionnable).
- Le texte extrait est retourné sous forme de chaîne de caractères exploitable par le LLM.

✅ **CA-009.3** : Composant IHM de téléversement (Upload)
- L'interface utilisateur (Streamlit) dispose d'un widget permettant de sélectionner ou glisser-déposer un fichier PDF.
- L'interface indique clairement que le téléchargement est en cours / réussi.

✅ **CA-009.4** : Gestion des erreurs et validation
- Le système vérifie que le fichier fourni est bien un PDF.
- Si le PDF est illisible ou corrompu, une erreur claire est renvoyée à l'utilisateur sans faire planter l'application.

✅ **CA-009.5** : Tests unitaires
- Des tests unitaires valident l'extraction de texte via `document_processor.py` en utilisant des fichiers PDF de test (factice, vide, volumineux).

### Scénario de Test

```
Utilisateur : [Upload 'reservation_hotel.pdf' via l'interface Streamlit]
Système : [Indicateur de chargement] -> "Document 'reservation_hotel.pdf' chargé avec succès."
Vérification interne (Console/Logs) : Le module document_processor.py retourne correctement le texte extrait ("Réservation confirmée, Hôtel XYZ, du 10 au 15 juin...").
```

### Notes Techniques

- **Concept Clé :** Modularité extrême. L'interface (UI) ne doit appeler qu'une seule fonction publique provenant de `document_processor.py`.
- L'implémentation de la lecture devra gérer le nettoyage basique des chaînes de caractères (espaces superflus, sauts de ligne excessifs).

### Dépendances

- US-001 (Structure)
- US-002 (Interface Streamlit)

---

## 🤖 US-004 : Intégration LLM (INFRA-003)

### User Story

**En tant qu'** utilisateur voyageur,  
**Je veux** que le chatbot comprenne mes questions, analyse mes documents PDF fournis, et y réponde de manière intelligente,  
**Afin d'** obtenir des informations et conseils pertinents et hautement personnalisés sur mes voyages.

### Priorité

🔴 **CRITIQUE** - Définie comme l'objectif central du Sprint 03 par le Product Owner.

### Critères d'Acceptation

✅ **CA-004.1** : Connexion à l'API LLM (Google Gemini)
- Le système s'interface avec succès avec l'API Google Gemini (ex: `gemini-1.5-flash` ou `gemini-1.5-pro`).
- Une fonction dédiée permet d'envoyer un prompt et de récupérer la réponse textuelle.

✅ **CA-004.2** : Gestion Sécurisée des Clés Secrètes
- La clé d'API Google Gemini (`GEMINI_API_KEY`) est chargée de manière sécurisée depuis un fichier `.env`.
- Le code source (notamment sur Git) ne contient jamais la clé en dur (vérification du `.gitignore`).
- Le système lève une erreur claire au démarrage si la clé est manquante.

✅ **CA-004.3** : Robustesse et Retry Logic
- Le module d'appel à l'API implémente un mécanisme de relance (Retry Logic) pour gérer les instabilités réseau ou les limites de taux (Rate Limits) de l'API gratuite.
- Si le LLM ne répond pas après X tentatives, l'application ne plante pas mais renvoie un message courtois à l'utilisateur (ex: "Le service est momentanément surchargé, veuillez réessayer").

✅ **CA-004.4** : Intégration du Contexte PDF (Interopérabilité)
- Le Chatbot est capable de concaténer le texte brut extrait (issu de la feature US-003 / `document_processor.py`) au prompt utilisateur pour que Gemini puisse "lire" le document et répondre en fonction.

✅ **CA-004.5** : Scénarios de Test Unitaire
- L'appel au LLM est encapsulé de sorte qu'il peut être moqué (mocked) dans les tests unitaires pour tester la Retry Logic sans consommer de vrais quotas API.

### Scénario de Test

```
Utilisateur : [Upload 'billet_train.pdf'] -> "À quelle heure part mon train ?"
Système (Interne) : Extrait le texte via document_processor, l'injecte dans le prompt vers Gemini. Lance l'appel.
Système (API) : [Échec temporaire - Timeout] -> [Le système relance / Retry] -> [Succès]
Chatbot : "Votre train part à 14h35 de la Gare de Lyon, d'après le billet que vous avez fourni."
```

### Notes Techniques

- La librairie officielle `google-generativeai` doit être ajoutée aux dépendances.
- Recommandation pour le Retry : utiliser la librairie `tenacity` ou coder un backoff exponentiel simple.

### Dépendances

- US-001 (Configuration projet Python)
### Dépendances

- US-001 (Configuration projet Python)
- US-002 (Interface chatbot)
- US-003 (Traitement PDF - pour le contexte)

---

## 🎤 US-005 : Interaction Vocale (INFRA-004)

### User Story

**En tant qu'** utilisateur voyageur,  
**Je veux** pouvoir écouter les réponses du chatbot au format audio et potentiellement dicter mes requêtes,  
**Afin d'** interagir plus naturellement, notamment lorsque je suis en déplacement.

### Priorité

🔴 **CRITIQUE** - Définie comme l'objectif central du Sprint 04 par le Product Owner.

### Critères d'Acceptation

✅ **CA-005.1** : Synthèse Vocale (Text-to-Speech)
- Les réponses textuelles du chatbot (LLM) sont converties en fichiers audio.
- Utilisation d'une librairie externe (ex: `gTTS`).

✅ **CA-005.2** : Intégration à l'IHM
- L'interface Streamlit permet de lire l'audio généré avec un player audio standard intégré.

✅ **CA-005.3** : Transcription Audio (Speech-to-Text) - *Optionnel selon limites MVP*
- L'utilisateur peut enregistrer sa voix via un widget Streamlit (ex: `streamlit-webrtc` ou `audio_recorder_streamlit`).
- L'audio est transcrit en texte pour être envoyé au LLM.

✅ **CA-005.4** : Gestion des erreurs
- Si l'API vocale est inaccessible, le chatbot fonctionne toujours parfaitement en mode textuel.

### Scénario de Test

```
Utilisateur : [Saisit "Raconte moi une blague de voyage"]
Système : [Texte] "Pourquoi..." + [Lecteur Audio "Pourquoi..."]
Test : Clic sur play, la voix est intelligible.
```

### Notes Techniques
- Explorer le package `gTTS` pour la synthèse.
- Pour la capture micro sous Streamlit, attention au déploiement HTTPS requis.

### Dépendances

- US-002 (Interface Streamlit)

---

## 📈 US-006 : Analyse de Sentiment (UX-004)

### User Story

**En tant qu'** utilisateur voyageur,  
**Je veux** que le chatbot évalue l'humeur et le ton de nos échanges (ou le ton d'un document fourni), et affiche cette analyse visuellement,  
**Afin de** rendre l'expérience plus ludique, interactive et esthétique.

### Priorité

🟠 **HAUTE** - Objectif central du Sprint 05 (focus sur l'UX visuelle).

### Critères d'Acceptation

✅ **CA-006.1** : Évaluation du sentiment
- Le système analyse chaque retour (prompt ou texte de l'IA) ou document pour en extraire un score de sentiment (positif, neutre, négatif) via une analyse NLP (par LLM ou librairie métier).

✅ **CA-006.2** : Affichage esthétique et avancé
- Le composant `st.metric` de Streamlit doit être utilisé pour l'affichage précis du score.
- Le style doit être géré visuellement : ex. couleur verte et flèche vers le haut pour un sentiment *Positif*, et rouge avec flèche vers le bas pour *Négatif*.
- Facultatif mais encouragé : inclure une jauge de confiance (slider/graph) ou un petit graphique (chart) pour une UI "belle à regarder".

✅ **CA-006.3** : Complémentarité avec le LLM
- Le résultat d'analyse de sentiment peut se superposer ou s'insérer proprement à côté du fil de discussion sans casser l'interface du chatbot existant.

### Scénario de Test

```
Utilisateur : "Je suis super enthousiaste de partir à Rome !"
Système : [Répond au prompt] + [Affiche st.metric : "Ton: Positif 😊" en VERT]
Utilisateur : "Mon vol est annulé, je suis dégoûté..."
Système : [Répond au prompt] + [Affiche st.metric : "Ton: Négatif 😞" en ROUGE]
```

### Notes Techniques

- Focus obligatoire sur les composants avancés visuels Streamlit (st.metric, st.progress, etc.).
- L'analyse peut être requêtée "sous le capot" lors du passage du prompt.

### Dépendances

- US-002 (Interface Streamlit existante)


---

## ✨ US-007 : Interface Graphique Premium (UX-005)

### User Story

**En tant qu'** utilisateur voyageur,  
**Je veux** interagir avec une application au design premium (bannière attrayante, couleurs harmonieuses, animations subtiles, ergonomie soignée),  
**Afin de** vivre une expérience immersive, inspirante et digne d'une plateforme de voyage haut de gamme.

### Priorité

🟠 **HAUTE** - Objectif central du Sprint 06 (Design & Branding).

### Critères d'Acceptation

✅ **CA-007.1** : Identité Visuelle et Bannière
- L'application doit intégrer une bannière ou un espace d'en-tête (Header) attrayant, évoquant le voyage et l'évasion.
- Un logo ou une typographie soignée doit être mis en place pour le titre principal (abandon de la police système basique si possible).

✅ **CA-007.2** : Palette de Couleurs "Premium"
- Abandon des couleurs génériques ou thèmes par défaut au profit d'une palette sélectionnée (ex: dark mode élégant, ou couleurs épurées inspirées des applications de voyage de pointe).
- Le thème Streamlit (`.streamlit/config.toml`) et les injections CSS (`st.markdown`) doivent appliquer un jeu de couleurs cohérent et offrir une liseuse de haut niveau.

✅ **CA-007.3** : Amélioration de l'Ergonomie de Chat
- Aménager l'espacement et la structure visuelle des bulles de discussion (Avatars personnalisés : ex. icône valise/avion pour le Chatbot).
- Intégration harmonieuse des composants existants (lecteur audio, widget d'upload PDF, tags de sentiment) afin de ne pas casser le rendu global.

✅ **CA-007.4** : Dynamisme
- (Si faisable) Ajout de subtils effets de transition CSS (glassmorphism sur certains conteneurs) pour un rendu moderne.

### Scénario de Test

```
Testeur : Lance l'application.
Observation : L'écran d'accueil est immersif. Le thème sombre ou coloré s'affiche immédiatement. L'en-tête est "wow".
Testeur : Insère une demande.
Observation : Le chatbot répond. Les jauges de sentiment et boutons de voix sont intégrés de manière transparente au nouveau design et lisibles.
```

### Notes Techniques

- L'Architecte devra probablement concevoir l'injection stricte de CSS customisé (`<style>...</style>`) et suggérer la modification du fichier config TOML.
- Respecter l'impératif de "Visual Excellence" : l'interface ne doit pas ressembler à un POC Streamlit typique.

### Dépendances

- US-002 (Interface Streamlit existante)
- Compatible US-005, US-006 (garder audio et score visibles).

---

## 📊 Matrice de Priorisation

| ID     | User Story                  | Priorité    | Complexité | Valeur     | Sprint Suggéré |
| ------ | --------------------------- | ----------- | ---------- | ---------- | -------------- |
| US-001 | Configuration Projet Python | ✅ TERMINÉ  | Faible     | ⭐⭐⭐⭐⭐ | Sprint 1       |
| US-002 | Interface Chatbot           | ✅ TERMINÉ  | Moyenne    | ⭐⭐⭐⭐⭐ | Sprint 1       |
| US-003 | Traitement de Documents PDF | ✅ TERMINÉ  | Moyenne    | ⭐⭐⭐⭐⭐ | Sprint 2       |
| US-004 | Intégration LLM             | ✅ TERMINÉ  | Moyenne    | ⭐⭐⭐⭐⭐ | Sprint 3       |
| US-005 | Interaction Vocale          | 🔴 CRITIQUE | Moyenne    | ⭐⭐⭐⭐⭐ | Sprint 4       |
| US-006 | Analyse de Sentiment        | 🟠 HAUTE    | Moyenne    | ⭐⭐⭐⭐   | Sprint 5       |
| US-007 | Interface Premium           | 🟠 HAUTE    | Moyenne    | ⭐⭐⭐⭐⭐ | Sprint 6       |

---

## 🎯 Définition du MVP

Le **Minimum Viable Product** comprend les User Stories suivantes :

- ✅ US-001 : Configuration Projet
- ✅ US-002 : Interface Chatbot
- ✅ US-003 : Traitement de Documents PDF
- ✅ US-004 : Intégration LLM
- ✅ US-005 : Interaction Vocale (Sprint 04)
- 🚧 US-006 : Analyse de Sentiment (Sprint 05)

**Objectif MVP** : Un chatbot fonctionnel capable de dialoguer avec un utilisateur et générer un itinéraire de voyage personnalisé jour par jour.

---

## 📝 Notes Générales

### Prochaines User Stories à Raffiner


### Méthodologie

- Chaque User Story sera transformée en spécification technique par l'Architecte
- Les critères d'acceptation serviront de base aux tests
- Le QA vérifiera tous les critères avant validation

---

**Date de création** : 12 février 2026  
**Dernière mise à jour** : 02 avril 2026 (Ajout US-006)
**Version** : 1.1  
**Statut** : 7 User Stories MVP définies et prêtes pour planification technique
