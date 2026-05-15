# Rétrospective - SPRINT 02

**Date :** 11 mars 2026
**Thème du Sprint :** [Upload et Extraction de documents PDF (document_processor.py)]

---

## 🧐 Questions Clés du Bilan

1. **L'architecture modulaire choisie (document_processor.py) a-t-elle facilité l'intégration de pypdf ?** *(Efficacité de la conception conception)*
2. **Quelles ont été les principales difficultés rencontrées lors de l'extraction du texte brut à partir des PDF divers ?** *(Robustesse, cas limites)*
3. **Comment pouvons-nous améliorer le traitement des erreurs liées aux fichiers uploaddés pour une meilleure expérience utilisateur ?** *(Fiabilité de l'IHM)*

---

## 👥 Retours par Rôle

### 👔 [BA / Product Owner]
- **Réponses aux questions clés :**
  - **1. Efficacité de la conception :** L'ajout de cette fonctionnalité d'upload de PDF enrichit énormément la valeur de notre Assistant de Voyage, en permettant aux utilisateurs d'importer directement leurs billets, réservations, ou guides de voyage existants. L'approche modulaire promise est rassurante pour l'évolutivité.
  - **2. Obstacles :** Il a fallu s'assurer que le besoin métier était bien compris dès le départ : l'utilisateur s'attend à ce que le chatbot "lise" le PDF instantanément, ce qui implique une exécution performante.
  - **3. Amélioration IHM :** Il est crucial que l'utilisateur reçoive un feedback immédiat si le PDF est corrompu, illisible, ou s'il dépasse une certaine taille.
- **Commentaires sur la valeur métier :**
  - Cette fonctionnalité pivot nous rapproche d'un véritable "Compagnon" de voyage qui contextualise ses réponses avec les documents réels de l'utilisateur. C'est une excellente avancée.

### 📐 [ARCHITECT]
- **Réponses aux questions clés :**
  - **1. Efficacité de la conception :** Oui, le choix de créer un module indépendant `document_processor.py` découplé de l'interface Streamlit s'avère payant. Cela permet au CODER et au QA de tester la logique d'extraction `pypdf` de manière isolée sans avoir à lancer toute l'IHM.
  - **2. Obstacles :** La principale difficulté anticipée (et traitée dans l'architecture) est la variété des "faux" PDF (images scannées sans texte sélectionnable) ou des fichiers corrompus. La spécification exige de lever des `ValueError` distinctes pour que l'interface puisse les attraper proprement.
  - **3. Amélioration IHM :** L'architecture recommande de bloquer les erreurs au niveau fonctionnel et de renvoyer des messages clairs (st.error ou st.warning) plutôt que de laisser l'application "planter" face à l'utilisateur.
- **Commentaires techniques / architecture :**
  - La bibliothèque `pypdf` gère bien le texte standard, mais elle ne fait pas d'OCR (Reconnaissance Optique de Caractères). Il faudra être transparent avec le Product Owner sur le fait que les photos de passeports en PDF ne seront pas lues dans ce MVP.
  - La séparation claire entre le Bytestream (fourni par Streamlit) et le lecteur PDF garantit une bonne testabilité.

### 🔨 [CODER]
- **Réponses aux questions clés :**
  - **1. Efficacité de la conception :** Oui, la création du module `document_processor.py` a grandement simplifié l'intégration de `pypdf`. L'interface Streamlit (`app.py`) n'a besoin de connaître qu'une seule méthode (`extract_text_from_pdf`), ce qui garde le code UI propre et facilite l'ajout d'autres formats de documents à l'avenir.
  - **2. Obstacles :** La principale difficulté est venue du traitement des fichiers PDF contenant des images scannées (sans texte). J'ai dû implémenter des vérifications explicites pour s'assurer que le texte extrait n'est pas vide et renvoyer une `ValueError` informative le cas échéant. Se moquer de `pypdf` pour les tests unitaires a également demandé un peu de réflexion pour simuler correctement les différents états de fichiers sans nécessiter de vrais PDF sur le disque dur.
  - **3. Amélioration IHM :** Actuellement, le widget Streamlit `file_uploader` gère le téléversement, et les exceptions (`ValueError`) de notre processeur sont capturées avec des `st.error`. On pourrait améliorer l'expérience en ajoutant une prévisualisation basique du nom du fichier ou de sa taille avant le traitement, ou en offrant la possibilité de rejeter un document dont l'extraction aurait produit trop peu d'informations utiles pour le LLM.
- **Commentaires sur le développement / le code :**
  - Le module `document_processor` est couvert par des tests exhaustifs validant les succès d'extraction ainsi que les gestions d'erreurs (fichiers vides, corrompus, ou sans texte). L'architecture est stable et prête pour le LLM.

### 🕵️‍♀️ [QA]
- **Réponses aux questions clés :**
  - **1. Efficacité de la conception :** Oui, le découplage a été un énorme atout pour la phase de test. J'ai pu écrire et exécuter des tests unitaires (`pytest`) concentrés uniquement sur `document_processor.py`, atteignant ainsi une couverture de code de 100 % sur ce fichier, sans que Streamlit ne vienne interférer.
  - **2. Obstacles :** La validation de la robustesse face aux PDF invalides a nécessité la création dynamique de fichiers altérés (BytesIO) pour m'assurer que les exceptions `ValueError` remontaient bien avec les bons messages. Ce point a été parfaitement géré.
  - **3. Amélioration IHM :** L'interface actuelle (qui attrape les erreurs et affiche un beau `st.error` rouge) a pu être validée manuellement par le PO. Pour l'avenir, envisager des tests automatisés E2E capables de manipuler l'input de fichier (ce qui est limitant pour certains outils d'automatisation actuels) serait un plus.
- **Commentaires sur les tests / la qualité :**
  - Le plan de test manuel `INFRA-002_test_plan.md` a été brillamment exécuté. Le code livré par le Coder est propre, passe les validations de formatage (PEP8/Flake8), et l'application est très stable. L'US-003 est une franche réussite côté Qualité.

### 🚀 [DEVOPS]
- **Réponses aux questions clés :**
  - **1. Ce qui a bien fonctionné :** Le découplage du code (module `document_processor` isolé) a grandement facilité l'intégration continue et la validation des tests. Le workflow Git (commit/push) par Feature (INFRA-003) reste consistant et le CHANGELOG s'avère très utile pour suivre l'ajout de spécificités comme l'upload PDF.
  - **2. Obstacles :** La gestion des fichiers de tests (PDF valides, corrompus, fictifs) a requis de bien exclure ou organiser le dossier `tests/test_data/` pour ne pas alourdir le repo tout en permettant aux tests automatisés de s'exécuter localement. Un ajustement du `# Tests` dans le `.gitignore` a été pris en compte.
  - **3. Amélioration globale :** Valider formellement la mise en place d'une pipeline CI basique (sur GitHub Actions ou GitLab CI local) pour exécuter systématiquement `pytest` et `flake8` à chaque push, afin d'automatiser cette étape actuellement semi-manuelle.
- **Commentaires sur l'infrastructure / les outils :**
  - Ajout propre de `pypdf` dans `requirements.txt`. Le projet garde ses dépendances saines et modulaires.

---

## 🎯 Plan d'Action (Pour le prochain Sprint)

- [ ] **Action 1** : Mettre en place un outil de CI basique (ex: GitHub Actions) pour automatiser l'exécution de `pytest` et `flake8` à chaque push (Assigné à : [DEVOPS])
- [ ] **Action 2** : Ajouter une prévisualisation basique des infos du PDF avant traitement ou rejeter ceux peu riches en texte (Assigné à : [CODER] / [BA])
- [ ] **Action 3** : Explorer des tests automatisés E2E (End-to-End) capables de manipuler l'input d'upload de fichiers (Assigné à : [QA])

---

## 📊 Synthèse Globale du Sprint 02

**Bilan : 🟢 EXCELLENT**

Le Sprint 02, dédié au **Traitement de Documents PDF (US-003)**, s'achève sur une franche réussite technique et produit. 

**Points Forts :**
- **Architecture Décisive :** L'approche modulaire avec `document_processor.py` (isolé de Streamlit) a prouvé son immense valeur : elle a permis un développement et des tests unitaires à 100% de couverture indépendants de l'UI.
- **Fiabilité IHM :** La gestion propre des erreurs (fichiers vides, images scannées), transformées en `ValueError` et attrapées via `st.error`, montre une forte maturité face aux cas limites.
- **Valeur Métier :** Le chatbot dispose maintenant d'une porte d'entrée concrète pour lire le contexte personnel des voyageurs (billets, réservations), un pas de géant vers l'assistance contextuelle.

**Axes d'Amélioration :**
- L'équipe souligne qu'à ce stade, il devient pertinent d'automatiser complètement les workflows de qualité (CI) pour ne plus lancer `pytest` et `flake8` de manière semi-manuelle, et d'envisager des tests E2E complexes pour tester le widget d'upload Streamlit de bout en bout. De plus, `pypdf` a des limites (pas d'OCR sur les photos), ce qui devra être clairement documenté pour l'utilisateur.

**Décision :** Sprint 02 validé et archivé. L'infrastructure est prête, le terrain est dégagé pour attaquer le cerveau du système : l'Intégration du LLM.
