# Rétrospective - Sprint 05

**Objectif du Sprint :** Analyse de Sentiment Visuelle interactive (US-006)
**Date :** 02 avril 2026

---

## 🎯 Questions Clés du Bilan

1. **Qu'est-ce qui a bien fonctionné pendant ce sprint ?** (ex: la facilité d'usage des indicateurs Streamlit `st.metric`, le modèle NLP pour le sentiment, etc.)
2. **Quelles ont été les principales difficultés ou blocages rencontrés ?** (ex: contraintes visuelles imposées par le PO, performance du calcul du sentiment, etc.)
3. **Quelles actions concrètes pouvons-nous mettre en place pour nous améliorer au prochain sprint ?** (ex: adoption d'une convention plus claire, ajout d'un linter, etc.)

---

## 👥 Retours de l'Équipe

Merci à chaque membre de l'équipe de remplir sa section en répondant aux 3 questions clés ci-dessus en fin de sprint.

### Architect

**1. Qu'est-ce qui a bien fonctionné pendant ce sprint ?**
Le choix de déléguer l'analyse contextuelle de sentiment à un moteur NLP local (comme VADER/TextBlob) plutôt qu'au LLM principal a été une excellente décision architecturale. Cela a préservé les coûts API et drastiquement réduit la latence pour l'évaluation de l'interface qui doit rester fluide.

**2. Quelles ont été les principales difficultés ou blocages rencontrés ?**
L'alignement avec les précédents standards de nommage pour les spécifications (« UX-004 » proposé initialement avant rectification en « INFRA-005 »). Cette rigueur nous force à maintenir une grande discipline dans l'arborescence des cas d'usage.

**3. Quelles actions concrètes pouvons-nous mettre en place pour nous améliorer au prochain sprint ?**

- Veiller à bien encercler les tests de non-régression UI : `st.metric` et `st.progress` peuvent facilement casser le rendu Streamlit s'ils sont mal typés.
- Convenir systématiquement, et de façon irrévocable, d'une clé d'ingénierie commune (ex. la suite des `INFRA-`) avant la livraison des spécifications pour prévenir tout travail de renommage.

### Coder

**1. Qu'est-ce qui a bien fonctionné pendant ce sprint ?**
L'intégration de `textblob` couplé à l'extension `textblob-fr` a été extrêmement limpide. Le traitement asynchrone local remplit le cahier des charges d'une faible latence. De plus, exploiter les widgets natifs `st.metric` et `st.progress` a permis un rendu très professionnel en seulement quelques lignes de code sous chaque bulle utilisateur.

**2. Quelles ont été les principales difficultés ou blocages rencontrés ?**
Le test initial sur Moteur TextBlob standard classait les avis français en "Neutre" car son corpus est anglais. Il a fallu identifier, installer `textblob-fr`, et mapper le _PatternAnalyzer_ et _PatternTagger_ spécifiques pour que les tests unitaires TDD (Positif, Négatif, Neutre) passent sans appel intermédiaire à un traducteur ou à l'API LLM.

**3. Quelles actions concrètes pouvons-nous mettre en place pour nous améliorer au prochain sprint ?**
- Créer une suite de tests d'interface avec `streamlit.testing.v1.AppTest` ou Selenium pour vérifier que le `delta` coloré (vert/rouge) du composant `st.metric` a le comportement attendu.
- Garder une réflexion sur la surcharge cognitive de l'UI : avec l'Historique, le TTS, l'UI audio, et maintenant l'UI sentiment, vérifier qu'on ne "pollue" pas trop la zone principale de Chat.

### QA

**1. Qu'est-ce qui a bien fonctionné pendant ce sprint ?**
L'exécution de tous les cas de tests fonctionnels liés au rendu d'interface (`st.metric` delta vert/rouge). Les spécifications fournies par l'architecte étaient très explicites, ce qui a rendu la définition du plan de test (`INFRA-005_test_plan.md`) extrêmement fluide. La couverture de tests unitaires du Coder en amont nous a permis de nous concentrer exclusivement sur l'UX.

**2. Quelles ont été les principales difficultés ou blocages rencontrés ?**
L'exigence de cohabitation (Non-Régression) entre le nouveau composant de sentiment, l'historique et le widget de synthèse locale (TTS) demandait une vérification très soignée du cycle de rafraîchissement (rerun) de l'interface Streamlit pour certifier l'absence de conflit. L'outil d'automatisation natif (`AppTest`) a d'ailleurs timeouté sur certaines relances, forçant une rigoureuse évaluation hybride.

**3. Quelles actions concrètes pouvons-nous mettre en place pour nous améliorer au prochain sprint ?**
- Stabiliser et standardiser l'usage d'un outil end-to-end (E2E) fiable (comme `Playwright` ou forcer l'usage maîtrisé de `AppTest`) pour pouvoir rejouer ces tests d'UX massivement à chaque livraison future.
- Continuer à systématiser la rédaction de nos cas de test sous forme de Checklists Markdown.

### DevOps

**1. Qu'est-ce qui a bien fonctionné pendant ce sprint ?**
L'ajout de la bilbliothèque `textblob-fr` ne demande aucun service cloud externe, ni clés API supplémentaires ou images lourdes. C'est robuste et facile à empaqueter. Les processus de mise à un jour du `CHANGELOG.md` et de gestion des branches Git s'exécutent avec une bonne vélocité.

**2. Quelles ont été les principales difficultés ou blocages rencontrés ?**
Dès que nous accumulons des packages externes pour le NLP et du Web (Streamlit, LLM client, Audio, NLP stats), l'environnement commence à grossir. Sans outils CI (Continuous Integration), tester les conflits d'environnements restera une action fastidieuse. 

**3. Quelles actions concrètes pouvons-nous mettre en place pour nous améliorer au prochain sprint ?**
- Analyser la taille de l'environnement virtuel et potentiellement séparer les dépendances de dev et de production (avec un gestionnaire de type `poetry` ou des requirements distincts).
- Rédiger un fichier `Dockerfile` initial pour s'assurer que notre MVP se lance de manière isolée sans soucis de dépendance de l'OS hôte.
