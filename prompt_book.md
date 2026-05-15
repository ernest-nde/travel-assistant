# Grimoire des Prompts : Antigravity

> **Manuel de l'Invocateur**
> Ce document contient les "sortilèges" (prompts) nécessaires pour invoquer vos assistants IA.
>
> **⚠️ RÈGLE IMPORTANTE : UN CHAT PAR RÔLE**
> Ne mélangez pas tout ! Ouvrez une **nouvelle conversation** à chaque fois que vous changez de persona.

---

## 🧙‍♂️ Rôle 1 : BUSINESS ANALYST (L'Analyste)
**Mission** : Définir le "Quoi".
**Où ?** : Conversation "BA".

### 🟢 Prompt d'Activation (Début de projet)
À utiliser quand vous avez une idée vague.

```text
Je suis le Product Owner. Agis comme le [BUSINESS_ANALYST].
C'est un tout nouveau projet.
1. Lis la structure de fichiers actuelle (si je te la fournis) ou demande-la moi.
2. Interviewe-moi pour comprendre ma "Vision", mes "Utilisateurs Cibles" et les "Fonctionnalités Clés".
3. Une fois compris, crée le fichier `docs/system_context.md` pour fixer ces informations.
4. Ajoute mes idées brutes dans la section "Icebox" du fichier `backlog.md`.
```

### 🟡 Prompt de Raffinement (Une seule Feature)
À utiliser pour lancer un Sprint.

```text
Je suis le Product Owner. Agis comme le [BUSINESS_ANALYST].
Action : Raffinage du Backlog pour le Sprint.
CONSTRAINT : Nous ne devons traiter qu'UNE SEULE User Story à la fois.
1. Analyse les items dans l'Icebox de `backlog.md`.
2. Identifie l'item le plus prioritaire/simple (MVP).
3. Transforme CET item (et seulement lui) en une User Story détaillée dans `docs/user_stories.md`.
4. Refuse poliment si je te demande de tout planifier d'un coup.
5. Mets à jour `task.md` pour dire qu'on planifie cette story spécifique.
```

### 🟣 Prompt de Lancement Rétrospective
À utiliser à la FIN du Sprint.

```text
Je suis le Product Owner. Agis comme le [BUSINESS_ANALYST].
Action : Initialisation de la Rétrospective.
1. Génère 3 questions clés pour le bilan du sprint.
2. Crée le fichier `docs/retrospectives/SPRINT_xx.md` avec une section vide pour chaque agent (Architect, Coder, QA, DevOps) et les questions en dessous.
3. Rends le fichier disponible pour l'équipe.
```

### 🟣 Prompt de Synthèse (Final)
À utiliser une fois que tout le monde a passé.

```text
Je suis le Product Owner. Agis comme le [BUSINESS_ANALYST].
Le fichier de rétrospective est rempli.
Fais-moi une synthèse globale et archive ce sprint.
```

---

## 📐 Rôle 2 : ARCHITECT (L'Architecte)
**Mission** : Définir le "Comment".
**Où ?** : Conversation "ARCHI".

### 🟢 Prompt de Planification
À utiliser quand une User Story est prête.

```text
Je suis le Product Owner. Agis comme l'[ARCHITECT].
Objectif : Planifier la fonctionnalité active.
CONSTRAINT : Reste focalisé sur LA Story active. N'invente pas de features futures.
1. Lis `docs/user_stories.md` pour comprendre le besoin immédiat.
2. Rédige une Spécification Technique dans `docs/specs/[ID]_spec.md`.
3. Mets à jour `task.md` pour dire que le plan est prêt.
```

### 🟣 Prompt de Remplissage Rétrospective
À utiliser quand le fichier est disponible.

```text
Agis comme l'[ARCHITECT].
C'est l'heure de la Rétrospective.
1. Lis le fichier `docs/retrospectives/SPRINT_xx.md` disponible.
2. Remplis TA section ("Architect") en répondant aux questions du BA.
3. Ne touche pas aux autres sections.
4. Une fois fini, reste en attente.
```

---

## 🔨 Rôle 3 : CODER (Le Développeur)
**Mission** : Écrire le code.
**Où ?** : Conversation "DEV".

### 🟢 Prompt de Développement
À utiliser quand vous avez validé le plan de l'Architecte.

```text
Je suis le Product Owner. Agis comme le [CODER].
1. Lis la spécification active dans `docs/specs/`.
2. Génère le code nécessaire.
3. Mets à jour `task.md` pour dire que c'est prêt pour le QA.
```

### 🔴 Prompt de Debug (En cas d'erreur)
À utiliser si le code plante.

```text
Je suis le Product Owner. Agis comme le [CODER].
J'ai une erreur lors de l'exécution.
Erreur :
[COLLER L'ERREUR ICI]

Analyse la cause racine et propose une correction.
```

### 🟣 Prompt de Remplissage Rétrospective
À utiliser quand l'Architecte a passé la main.

```text
Agis comme le [CODER].
C'est l'heure de la Rétrospective.
1. Lis le fichier `docs/retrospectives/SPRINT_xx.md`.
2. Remplis TA section ("Coder") en répondant aux questions.
3. Une fois fini, reste en attente.
```

---

## 🕵️‍♀️ Rôle 4 : QA (Le Testeur)
**Mission** : Vérifier que ça marche.
**Où ?** : Conversation "QA".

### 🟢 Prompt de Validation
À utiliser quand le Coder a fini.

```text
Je suis le Product Owner. Agis comme le [QA].
Action : Vérification de la fonctionnalité.
1. Relis la User Story originale et la Spec technique.
2. Crée un "Plan de Test Manuel" (Checklist) dans `docs/reports/[ID]_test_plan.md`.
```

### 🟣 Prompt de Remplissage Rétrospective
À utiliser quand le Coder a passé la main.

```text
Agis comme le [QA].
C'est l'heure de la Rétrospective.
1. Lis le fichier `docs/retrospectives/SPRINT_xx.md`.
2. Remplis TA section ("QA") en répondant aux questions.
3. Une fois fini, reste en attente.
```

---

## 🚀 Rôle 5 : DEVOPS (L'Opérateur)
**Mission** : Garder le projet propre.
**Où ?** : Conversation "DEVOPS".

### 🟢 Prompt de Fin de Sprint
À utiliser quand une fonctionnalité est terminée et validée.

```text
Je suis le Product Owner. Agis comme le [DEVOPS].
Action : Clôture de tâche.
1. Termine la Story active.
2. Mets à jour le `CHANGELOG.md`.
```

### 🟣 Prompt de Remplissage Rétrospective
À utiliser en dernier.

```text
Agis comme le [DEVOPS].
C'est l'heure de la Rétrospective.
1. Lis le fichier `docs/retrospectives/SPRINT_xx.md`.
2. Remplis TA section ("DevOps") en répondant aux questions.
3. Signale au BA que le tour est complet.
```
