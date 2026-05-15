# Synthèse de la Rétrospective - Sprint 05

**Date :** 04 avril 2026
**Objectif :** Analyse de Sentiment Visuelle interactive (US-006 / UX-004 / INFRA-005)

## 1. Ce qui a bien fonctionné (Succès)
- **Architecture Locale Performante :** Le choix de déléguer l'analyse NLP à une bibliothèque locale (`textblob` avec l'extension `textblob-fr`) pour l'exécution asynchrone a permis de préserver les coûts API du LLM et de garantir une faible latence.
- **Excellence UX/UI :** L'utilisation de widgets natifs Streamlit tels que `st.metric` (avec deltas colorés vert/rouge) et `st.progress` a offert un rendu très professionnel en peu de lignes tout en conservant la fluidité.
- **Processus de Test Efficace :** La couverture conjointe des tests unitaires par le Coder et des tests fonctionnels UX rigoureux (`INFRA-005_test_plan.md`) par le QA a grandement rationalisé la livraison.
- **Déploiement Allégé :** Ne pas requérir de nouveaux services cloud ou clés API externes maintient une intégration et livraison simples.

## 2. Difficultés et Blocages (Défis)
- **Barrière de Langue NLP :** Bloquage initial dû au corpus anglais du moteur NLP ; rapidement résolu grâce à l'incorporation d'analyseurs lexicaux français (`textblob-fr`).
- **Cohabitation d'Interface (Reruns) :** Gérer les rafraîchissements Streamlit (`st.rerun()`) est devenu particulièrement délicat avec le couplage Historique de Chat, Lecteur Audio (TTS), et UI contextuelle de sentiment sans timeout sur certains tests natifs.
- **Gestion des Conventions :** Quelques frictions mineures dans la nomenclature documentaire (`UX-004` vs `INFRA-005`), et le ballonnement asymptotique des packages de l'environnement Python global.

## 3. Plan d'Action pour le Sprint 06 (Améliorations Systémiques)
Pour soutenir la scale-up de l'application et sa robustesse, l'équipe s'engage sur les priorités d'amélioration continue suivantes :
1. **Tests E2E Automatisés :** Stabiliser un framework de test End-to-End (Playwright, Selenium ou la maîtrise avancée de l'`AppTest` natif) garantissant une non-régression UI automatisée, avant toute livraison.
2. **Hygiène de l'Environnement et Conteneurisation :** 
   - Rédiger un fichier `Dockerfile` pour préparer une isolation complète de l'application de son OS hôte.
   - Envisager la séparation des dépendances Dev vs. Prod (ou adopter un gestionnaire comme Poetry).
3. **Harmonisation :** Adopter de manière irrévocable une convention unique pour la numérotation des tickets et la charge cognitive de l'UI pour ne pas surcharger l'utilisateur.
