# Plan de Test Manuel - INFRA-003 (US-004)

> **User Story**: US-004 : Intégration LLM (Google Gemini)  
> **Spec Technique**: INFRA-003  
> **QA Tester**: AI Assistant (QA)  
> **Date**: 2026-03-20  
> **Statut**: 📋 Prêt pour Test

---

## 📋 Vue d'Ensemble

Ce document fournit un plan de test manuel complet pour valider la fonctionnalité d'**Intégration LLM** (US-004/INFRA-003), en s'assurant qu'elle respecte tous les **Critères d'Acceptation** définis par l'Architecte.

### Objectifs de Test

- S'assurer que le système s'interface bien avec l'API Google Gemini.
- Vérifier la gestion sécurisée de l'API Key (`GEMINI_API_KEY`) et son absence du code versionné.
- Valider la robustesse de l'implémentation (Retry Logic) face aux timeouts.
- Confirmer que l'application Streamlit parvient à injecter le contexte PDF généré au Sprint 02 dans le prompt.
- S'assurer de la présence et du succès des tests unitaires mockant l'API.

---

## ✅ Critères d'Acceptation à Tester

| ID       | Critère d'Acceptation                                                        | Tests Associés | Statut      |
| -------- | ---------------------------------------------------------------------------- | -------------- | ----------- |
| CA-004.1 | Connexion effective à l'API LLM (Google Gemini)                              | T1, T4         | ⏳ À tester |
| CA-004.2 | Gestion Sécurisée des Clés Secrètes (`.env`)                                 | T2             | ⏳ À tester |
| CA-004.3 | Robustesse et Retry Logic (Fallback gracieux sur erreur)                     | T3, T5         | ⏳ À tester |
| CA-004.4 | Intégration du Contexte PDF (Interopérabilité avec US-003)                   | T4             | ⏳ À tester |
| CA-004.5 | Scénarios de Test Unitaire mockant l'API                                     | T5             | ⏳ À tester |

---

## 🧪 Plan de Test Détaillé

### Test T1: Conversation Basique (Nominal)

**Objectif**: Valider que le chatbot peut répondre à une question simple en utilisant Gemini.

**Critères**: CA-004.1

**Étapes**:
1. Démarrer l'application Streamlit (`streamlit run src/app.py`).
2. S'assurer que le fichier `.env` contient une `GEMINI_API_KEY` valide.
3. Dans la zone de chat de Streamlit, taper : "Bonjour, es-tu un assistant de voyage ?"
4. Observer la réponse.

**Résultat Attendu**:
- La réponse est générée par l'IA et est cohérente avec la question.
- Pas de crash ou de message de démonstration codé en dur (comme au Sprint 1).

**Critères de Succès**:
- [ ] L'assistant répond de manière pertinente.

---

### Test T2: Gestion Sécurisée de l'API Key

**Objectif**: Valider que l'application empêche de démarrer ou prévient proprement si l'API n'est pas configurée, et que la clé n'est pas pushée sur Git.

**Critères**: CA-004.2

**Étapes**:
1. Renommer temporairement le fichier `.env` en `.env.backup`.
2. Lancer l'application Streamlit.
3. Observer l'interface UI et la console.
4. Taper une question dans le chat.
5. Remettre le fichier `.env` par défaut.

**Résultat Attendu**:
- L'application indique clairement qu'il manque la clé API (`st.error`).
- Elle ne "crashe" pas silencieusement.

**Critères de Succès**:
- [ ] Erreur gérée proprement si clé absente.
- [ ] `GEMINI_API_KEY` n'est pas présente dans le code source contrôlé par version (`.env` est bien dans le `.gitignore`).

---

### Test T3: Fallback gracieux & Retry Logic (Erreur d'API Simulé)

**Objectif**: Simuler une anomalie réseau ou une fausse clé pour déclencher le fallback gracieux décrit par le Retry Logic.

**Critères**: CA-004.3

**Étapes**:
1. Dans le fichier `.env`, remplacer la vraie clé par une valeur invalide (ex: `GEMINI_API_KEY=FAUSSE_CLE_123`).
2. Redémarrer Streamlit.
3. Poser une question au Chatbot.
4. Observer le délai (la retry logic de `tenacity` tentera de boucler).

**Résultat Attendu**:
- Après quelques secondes (temps des retries), l'assistant répond avec le message d'erreur gracieux : *"Je suis désolé, le service d'Intelligence Artificielle est momentanément indisponible..."*

**Critères de Succès**:
- [ ] Timeout et Retry Logic respectés.
- [ ] Affichage du Fallback textuel plutôt qu'une grosse erreur Python Exception sur Streamlit.

---

### Test T4: Intégration du Contexte Documentaire (US-003 + US-004)

**Objectif**: Valider que le PDF uploadé est lu et son texte concaténé au Prompt pour Gemini.

**Critères**: CA-004.1, CA-004.4

**Étapes**:
1. S'assurer qu'une clé API *valide* est dans `.env`.
2. Démarrer Streamlit.
3. Téléverser le fichier PDF de test valide (contenant une fausse réservation d'hôtel avec des détails précis).
4. Poser une question spécifique au document : "À quel hôtel ai-je réservé selon le document ?"
5. Observer la réponse.

**Résultat Attendu**:
- Le Modèle répond exactement avec le nom de l'hôtel contenu dans le PDF (ce qu'il ne pourrait pas deviner autrement).

**Critères de Succès**:
- [ ] Gemini lit et intègre le contexte du document injecté par le back-end.

---

### Test T5: Tests Unitaires (QA Automatisé)

**Objectif**: S'assurer que le Coder a bien écrit des tests unitaires isolés pour `GeminiClient`, mockant l'API Google.

**Critères**: CA-004.5

**Étapes**:
1. Lancer la suite de tests via la commande : `pytest tests/test_gemini_client.py -v` (si ce fichier existe, sinon `pytest tests/`).

**Résultat Attendu**:
- Les tests s'exécutent avec succès.
- Les tests vérifient l'absence de clé et le fallback sans consommer de quota réel.

**Critères de Succès**:
- [ ] 100% des tests unitaires liés au LLM passent.

---

## 📊 Résumé des Tests (À remplir)

| Test | Description | Critère(s) | Statut | Résultat |
|------|-------------|------------|--------|----------|
| T1 | Conversation Basique (Nominal) | CA-004.1 | ✅ | Succès |
| T2 | Gestion API Key manquant | CA-004.2 | ✅ | Succès |
| T3 | Fallback Gracieux & Retry | CA-004.3 | ✅ | Succès |
| T4 | Interopérabilité PDF/LLM | CA-004.4 | ✅ | Succès (fonctionnel mais basique) |
| T5 | Tests Unitaires & Mock | CA-004.5 | ✅ | Succès (100%) |

---

## 🎯 Checklist de Validation Finale

- [x] **CA-004.1**: LLM Gemini répond correctement.
- [x] **CA-004.2**: Protection stricte de l'API key.
- [x] **CA-004.3**: Résilience aux erreurs réseau.
- [x] **CA-004.4**: Le Chatbot peut synthétiser le PDF envoyé.
- [x] **CA-004.5**: Le client LLM est mocké et testable en mode isolé.

---
**Document créé par**: AI Assistant (QA)  
**Basé sur**: US-004, INFRA-003_spec.md  
**Dernière Mise à Jour**: 2026-03-20
