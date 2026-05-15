# Product Backlog - Travel Assistant (Chatbot)

> **Légende des statuts**
>
> - 📦 **Icebox** : Idées brutes, non priorisées
> - 🔜 **Backlog** : Fonctionnalités priorisées, prêtes à être raffinées
> - 🚧 **En cours** : En développement
> - ✅ **Terminé** : Implémenté et validé

---

## 📦 Icebox

_L'Icebox a été nettoyée pour ne conserver aucune idée hors-périmètre. Le fichier se concentre uniquement sur ce qui a déjà été accompli._

---

## 🔜 Backlog

_Fonctionnalités priorisées et prêtes à être développées_

_Section vide - Les items seront déplacés de l'Icebox après priorisation du Product Owner_

---

## 🚧 En Cours

_Fonctionnalités actuellement en développement_

_Section vide_

---

## ✅ Terminé

_Fonctionnalités implémentées et validées_

- [x] **DOC-001** : Contexte système établi (vision, utilisateurs, contraintes)
- [x] **DOC-002** : Backlog initial créé avec items Icebox
- [x] **INFRA-001** : Configuration du projet Python (structure, virtualenv, requirements.txt)
- [x] **INFRA-002** : Configuration de l'interface chatbot (Streamlit/Gradio/CLI)
- [x] **INFRA-003** : Intégration du LLM (Google Gemini via API)
- [x] **INFRA-004** : Interaction vocale (Synthèse gTTS Text-to-Speech)
- [x] **INFRA-008** : Traitement de Documents PDF - Permettre le téléversement et l'extraction de texte (document_processor.py)
- [x] **UX-004** : Analyse de sentiment visuelle et évaluation du ton (score de confiance, jauges)
- [x] **UX-005** : Refonte Premium de l'Interface Graphique (UI/UX) (bannière, couleurs harmonieuses, ergonomie avancée)

---

## 📝 Notes

### Dépendances Identifiées

1. **InfrastructureFirst** : INFRA-001 à INFRA-004 sont des prérequis pour toutes les autres fonctionnalités
2. **Génération avant Modification** : Les fonctionnalités de modification d'itinéraire (MODIF-xxx) dépendent de la génération (ITIN-001)
3. **APIs selon besoin** : Les intégrations API seront ajoutées progressivement selon les fonctionnalités développées

### Priorités à Définir

Le Product Owner doit identifier les **3-5 premières user stories** à développer pour le MVP (Minimum Viable Product).

**Suivi du MVP et Sprint** :

1. ✅ MVP Principal (US-001 à US-005) achevé avec succès. 
2. ✅ Sprint 05 : Amélioration UX avancée via Analyse de Sentiment (UX-004) achevée.

---

## 🔄 Changelog

### Version 2.0 - 2026-02-12

- **Pivot majeur** : Réorganisation complète du backlog pour architecture chatbot
- Ajout de 60+ items organisés en 9 catégories
- Focus sur conversation naturelle et assistance continue

### Version 1.0 - 2026-02-12

- Création initiale avec focus web app planification
- ~~Obsolète~~ - Remplacé par approche chatbot

---

**Dernière mise à jour** : 06 avril 2026 (v2.3 - Validation Sprint 06 - UI Premium)
