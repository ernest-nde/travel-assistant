# Rétrospective - SPRINT 01

**Date :** 26 février 2026
**Thème du Sprint :** [Configuration et Socle du Projet (US-001)]

---

## 🧐 Questions Clés du Bilan

1. **Qu'est-ce qui a bien fonctionné et qu'on doit continuer à faire ?** _(Succès, bonnes pratiques)_
2. **Qu'est-ce qui a été difficile ou qui nous a ralentis ?** _(Obstacles, goulots d'étranglement)_
3. **Quelle est notre principale action d'amélioration pour le prochain sprint ?** _(Solution concrète)_

---

## 👥 Retours par Rôle

### 📐 [ARCHITECT]

- **Réponses aux questions clés :**
  - **1. Ce qui a bien fonctionné :** La création détaillée de la spécification technique (INFRA-001_spec.md) en amont a permis de lever les ambiguïtés sur la structure du projet, les dépendances et la stratégie de test. Le fait que le BA ait fourni des User Stories et un contexte système clairs a grandement facilité ce travail.
  - **2. Ce qui a été difficile :** L'ajustement aux nouvelles contraintes en cours de route (se focaliser uniquement sur l'US active sans extrapoler les dépendances futures dans les autres US). J'ai d'abord voulu tout planifier pour le MVP complet (US-001 à US-008), ce qui s'écartait de la demande ("Reste focalisé sur LA Story active").
  - **3. Amélioration pour le prochain sprint :** Suivre strictement la portée de l'US demandée par le PO sans anticiper sur les US ultérieures, sauf si une dépendance d'architecture le justifie obligatoirement à ce stade.
- **Commentaires techniques / architecture :**
  - L'US-001 pose une excellente base saine (environnement virtuel, linter, tests).
  - Il sera crucial que le CODER respecte cette base à la lettre, particulièrement au niveau du `.gitignore` pour éviter de polluer le repo avec le dossier `venv`.

### 🔨 [CODER]

- **Réponses aux questions clés :**
  - **1. Ce qui a bien fonctionné :** La création détaillée de la spécification a rendu claire la structure à mettre en place. Les outils en ligne de commande m'ont permis de générer rapidement la hiérarchie de fichiers et la configuration de base (requirements.txt, README.md, .gitignore).
  - **2. Ce qui a été difficile :** Rien de bloquant pour ce sprint initial. Cependant, la nécessité de valider la couverture de tests et le linting (black, flake8) dès à présent pour de très petits fichiers peut sembler verbeuse, bien que ce soit une bonne pratique sur le long terme.
  - **3. Amélioration pour le prochain sprint :** Continuer à s'appuyer strictement sur les spécifications générées par l'Architecte. Automatiser si possible la vérification des outils de qualité de code (black/flake8/pytest) dès la mise en place du code métier.
- **Commentaires sur le développement / le code :**
  - La structure de base (`src`, `tests`, `data`) est saine et prête pour le code métier de US-002.
  - Le `setup.py` et `requirements.txt` gèrent très bien la distinction entre les dépendances de prod et de dev.

### 🕵️‍♀️ [QA]

- **Réponses aux questions clés :**
  - **1. Ce qui a bien fonctionné :** La création d'un plan de test manuel précis, détaillé et traçable (`INFRA-001_test_plan.md`) directement à partir des critères d'acceptation de l'Architecte. Cela a donné une base complète et claire pour la validation de l'infrastructure du projet.
  - **2. Ce qui a été difficile :** Rien de bloquant. La seule petite difficulté était de s'assurer que toutes les commandes de test (pytest, flake8, black, environnement virtuel) soient explicitement détaillées et adaptées à chaque OS (Windows/Linux) pour que la validation par le Product Owner soit fluide.
  - **3. Amélioration pour le prochain sprint :** Continuer d'utiliser cette méthode de mapping direct 1-pour-1 entre Critères d'Acceptation et Scénarios de Test.
- **Commentaires sur les tests / la qualité :**
  - Le plan de test pour l'infrastructure est robuste. La validation manuelle couvre non seulement l'exécution du code, mais aussi l'hygiène du projet (le `.gitignore`, le formatage, le linting).
  - L'initiative d'inclure des tests automatisés dès la première User Story (US-001) garantit un bon niveau de qualité continue.

### 🚀 [DEVOPS]

- **Réponses aux questions clés :**
  - **1. Ce qui a bien fonctionné :** La systématisation de la clôture des tâches (mise à jour du `CHANGELOG.md`, nettoyage du `task.md`, vérifications Git) a permis de garder un dépôt propre. L'utilisation du format "Keep a Changelog" apporte beaucoup de clarté.
  - **2. Ce qui a été difficile :** Quelques petites alertes Git liées aux fins de ligne (LF vs CRLF) sous Windows, notamment sur le `.env.example`.
  - **3. Amélioration pour le prochain sprint :** S'assurer de maintenir la rigueur sur le format de commit (Conventional Commits) et potentiellement ajouter un fichier `.gitattributes` pour gérer la normalisation des sauts de ligne si le problème de CRLF persiste.
- **Commentaires sur l'infrastructure / les outils :**
  - Le cycle de commit/push de fin de Story est efficace et bien huilé. Le dépôt distant est synchronisé en parfaite cohérence avec le backlog.

## 🎯 Plan d'Action (Pour le prochain Sprint)

- [ ] **Action 1** : Rester strictement dans le périmètre de l'US active sans anticiper (Assigné à : [ARCHITECT])
- [ ] **Action 2** : Automatiser l'exécution des outils de qualité (black, flake8, pytest) (Assigné à : [CODER])
- [ ] **Action 3** : Maintenir le mapping 1-pour-1 entre Critères d'Acceptation et Scénarios de Test (Assigné à : [QA])
- [ ] **Action 4** : Ajouter un fichier `.gitattributes` pour gérer les fins de ligne CRLF/LF (Assigné à : [DEVOPS])

---

## 📊 Synthèse Globale du Sprint 01

**Bilan : 🟢 TRÈS POSITIF**

Le Sprint 01 (Configuration et Socle du Projet) a été un succès complet. L'équipe a réussi à livrer la **US-001** (Infrastructure Python) et la **US-002** (Interface Chatbot Streamlit) avec un haut niveau de qualité, posant des fondations solides pour le projet.

**Points Forts :**

- L'approche "Spec First" (Spécifications techniques détaillées avant de coder) a parfaitement fonctionné.
- La traçabilité entre les critères d'acceptation et les plans de test manuels garantit la qualité.
- L'hygiène du projet (versioning, environnement virtuel, linting) est excellente dès le départ.

**Axes d'Amélioration :**

- La principale friction est venue de la difficulté à restreindre la vision à une seule User Story à la fois, et quelques soucis mineurs d'OS (fins de ligne Git LF/CRLF sur Windows). Le plan d'action ci-dessus y remédie pour le prochain sprint.

**Décision :** Sprint 01 validé et archivé. Le projet est prêt à accueillir la logique métier (connexion LLM, etc.).
