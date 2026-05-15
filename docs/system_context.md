# Contexte Système - Travel Assistant

## 📍 Vision du Projet

**Travel Assistant** est un **chatbot conversationnel intelligent** en Python conçu pour accompagner les voyageurs dans toutes les étapes de leur voyage. L'assistant dialogue avec l'utilisateur pour comprendre ses besoins, génère des itinéraires personnalisés jour par jour, et fournit des recommandations adaptées ainsi que des informations pratiques essentielles.

### Problème Résolu

Les voyageurs font face à plusieurs défis :

- Difficulté à planifier des itinéraires cohérents et optimisés
- Manque d'informations pratiques centralisées (budget, météo, formalités)
- Besoin d'assistance en temps réel pendant le voyage
- Incertitude sur la sécurité et les urgences locales

Travel Assistant résout ces problèmes en offrant un **compagnon de voyage conversationnel disponible 24/7**.

### Valeur Ajoutée

- **Interface Conversationnelle** : Interaction naturelle par dialogue, pas de formulaires complexes
- **Personnalisation Intelligente** : Adaptation dynamique selon le profil et les demandes de l'utilisateur
- **Assistance Continue** : Support avant ET pendant le voyage
- **Flexibilité** : Modification facile des itinéraires sur simple demande
- **Informations Complètes** : Budget, météo, sécurité, formalités regroupées en un seul endroit

---

## 👥 Utilisateurs Cibles

### Profils Principaux

1. **Voyageurs Occasionnels** (majeurs)
   - Partent 1 à 3 fois par an
   - Recherchent la simplicité et les bons plans
   - Sensibles au rapport qualité/prix

2. **Professionnels en Déplacement**
   - Voyages fréquents pour le business
   - Priorité : efficacité et rapidité
   - Besoin de flexibilité dans les réservations

3. **Aventuriers**
   - Recherchent des destinations hors des sentiers battus
   - Flexibles sur les dates et le budget
   - Valorisent les expériences authentiques

4. **Familles**
   - Voyagent avec enfants (tous majeurs dans le scope actuel)
   - Besoin de planification détaillée
   - Recherchent sécurité et confort

### Caractéristiques Communes

- **Âge** : Adultes majeurs (18+)
- **Compétences techniques** : Niveau basique à intermédiaire
- **Besoins** : Simplicité d'utilisation, fiabilité, transparence des prix

---

## 🎯 Fonctionnalités Clés

### 1. Génération d'Itinéraires Intelligents

- **Recherche et suggestion de destinations** selon critères (budget, climat, envies)
- **Création d'itinéraires détaillés jour par jour**
  - Planification structurée avec horaires et durées
  - Séquencement logique des activités
  - Prise en compte des distances et temps de déplacement
- **Adaptation au profil** : Solo, Couple, Famille, Business
- **Optimisation selon budget** et préférences utilisateur

### 2. Modification Dynamique d'Itinéraires

- **Modification sur demande conversationnelle**
  - Ajout/suppression d'activités
  - Changement de jour ou d'horaire
  - Remplacement de destinations
- **Réoptimisation automatique** après modifications

### 3. Recommandations Personnalisées

- **Activités** : Visites, excursions, expériences locales
- **Restaurants** : Suggestions selon cuisine et budget
- **Hébergements** : Hôtels, auberges, locations adaptées au profil
- **Moyens de transport locaux** : Options de déplacement sur place

### 4. Gestion des Transports et Vols

- **Suggestions de transport inter-villes** : vols, trains, et bus
- **Comparaison des prix** entre différentes options
- **Temps de trajet et correspondances** détaillés
- **Alertes de baisse de prix** pour optimiser le budget

### 5. Informations Pratiques Complètes

- **Budget estimé** détaillé par catégorie (transport, hébergement, restauration, activités)
- **Météo** : Prévisions et meilleures périodes
- **Formalités** : Visa, passeport, vaccinations requises
- **Conseils locaux** : Culture, pourboires, langue, coutumes

### 6. Assistance Avant et Pendant le Voyage

- **Phase pré-voyage** : Planification, préparation, checklist
- **Phase pendant voyage** : Assistance en temps réel, ajustements d'itinéraire
- **Support continu** via conversation naturelle

### 7. Sécurité et Urgences

- **Informations de sécurité** : Zones à risque, précautions
- **Numéros d'urgence** locaux (police, ambulance, pompiers)
- **Contacts utiles** : Ambassades, consulats, hôpitaux
- **Conseils de sécurité** adaptés à la destination

---

## 🛠️ Contraintes Techniques

### Architecture

- **Type d'application** : **Chatbot Conversationnel** (interface texte)
- **Langage principal** : **Python**
- **Nature** : Assistant de voyage basé sur l'IA conversationnelle

### Infrastructure Chatbot

- **Interface utilisateur** :
  - CLI (Command Line Interface) pour prototype
  - Interface web conversationnelle (Streamlit, Gradio, ou custom)
  - Potentiel : Intégration messagerie (Telegram, WhatsApp, Slack)
- **Moteur conversationnel** :
  - LLM (Large Language Model) : OpenAI GPT, Google Gemini, Anthropic Claude, ou modèles open-source
  - Framework de gestion de dialogue : LangChain, Haystack
  - Gestion de contexte et mémoire de conversation

### Intégrations API

**Principe** : Utilisation d'APIs gratuites et disponibles en ligne

- **Informations de voyage** :
  - API Météo (OpenWeatherMap, WeatherAPI)
  - API Géolocalisation (OpenStreetMap, Google Places)
  - API Devises (ExchangeRate-API, Fixer.io)
- **Données touristiques** :
  - TripAdvisor API (attractions, restaurants)
  - OpenTripMap (points d'intérêt)
  - Wikivoyage API (guides de voyage)
- **Transport** (si disponible gratuitement) :
  - APIs publiques de transport local
  - Amadeus Self-Service (version gratuite limitée)

- **Sécurité et formalités** :
  - Travel Advisory APIs (gouvernements)
  - API Visa requirements (si disponible)

### Technologies Potentielles

- **Framework chatbot** : Streamlit, Gradio, ChainLit
- **IA conversationnelle** : LangChain, LlamaIndex
- **Base de données** : SQLite (local), PostgreSQL (production)
- **Stockage conversation** : JSON, SQLite, ou base vectorielle (ChromaDB, Pinecone)
- **Déploiement** : Streamlit Cloud, Hugging Face Spaces, ou serveur local

---

## 📅 Date de Création

**12 février 2026**

---

## 🔄 Versions

| Version | Date       | Auteur           | Modifications                                              |
| ------- | ---------- | ---------------- | ---------------------------------------------------------- |
| 1.0     | 2026-02-12 | Business Analyst | Création initiale (web app planification)                  |
| 2.0     | 2026-02-12 | Business Analyst | **Pivot majeur** : Transition vers chatbot conversationnel |
