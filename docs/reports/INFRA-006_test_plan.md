# Plan de Test Manuel - US-007 : Interface Graphique Premium (INFRA-006)

**Testeur :** Agent QA
**Date :** 06 Avril 2026
**Statut :** À tester

Ce document contient la checklist (plan de test) permettant de valider manuellement la refonte de l'interface graphique du Travel Assistant (Sprint 06).

---

## 🎯 1. Environnement Préalable
- S'assurer que les modifications de `.streamlit/config.toml` sont bien répercutées.
- Lancer l'application : `python -m streamlit run src/app.py`
- Disposer d'un navigateur web à jour (Chrome/Firefox/Edge) pour l'interprétation des effets CSS (glassmorphism).

---

## 🧪 Scénario 1 : Validation de l'Identité Visuelle Globale (Theming)

**Objectif :** S'assurer que les couleurs primitives et la charte graphique de base (via config Streamlit) sont actives et procurent une sensation "Premium".

- [x] **Couleurs de la marque :** Vérifier que les boutons principaux, curseurs, et autres composants interactifs n'utilisent plus le rouge/rosé Streamlit par défaut, mais arborent la nouvelle `primaryColor` élégante (ex: bleu azur ou cyan).
- [x] **Mode / Fond (Background) :** Vérifier que la palette globale (clair épuré ou dark mode sélectionné) est douce pour les yeux, lisible et harmonieuse.
- [x] **Typographie :** Vérifier que la police (`font`) n'est pas celle par défaut mais participe à l'élégance de l'IHM (style plus aéré).
- [x] **Statut :** PASSÉ

---

## 🧪 Scénario 2 : Personnalisation Avancée (CSS Injection et Glassmorphism)

**Objectif :** Vérifier l'action des styles injectés manuellement via HTML/CSS (`st.markdown`).

- [x] **Éléments natifs masqués :** Vérifier que le menu hamburger (en haut à droite) et le footer *Made with Streamlit* (en bas) sont bien invisibles, allégeant la fenêtre.
- [x] **Espacements repensés :** Vérifier que l'énorme vide supérieur de Streamlit a été réduit, pour permettre à l'application de démarrer plus haut sur l'écran.
- [x] **Effets Graphiques (Glassmorphism) :** Si implémenté, les encadrés annexes ou la barre latérale présentent des fonds subtilement transparents et floutés (test avec fond complexe en dessous).
- [x] **Statut :** PASSÉ

---

## 🧪 Scénario 3 : Habillage, En-tête et Bulles Chat

**Objectif :** Vérifier l'intégration des médias et avatars pour renforcer l'immersion fonctionnelle.

- [x] **Bannière d'en-tête :** Une image fine (paysage/voyage) trône proprement en haut de la page principale pour signifier le contexte du Travel Assistant.
- [x] **Avatars personnalisés :** Poser une question. Les bulles du chat doivent comporter des icônes/emojis en adéquation (ex: 👨‍💼 pour l'utilisateur, et une valise 🧳 ou un logo personnalisé pour le chatbot de voyage).
- [x] **Arrondis des champs :** Les entrées de texte et les boutons présentent des bords adoucis ou stylisés.
- [x] **Statut :** PASSÉ

---

## 🧪 Scénario 4 : Test de Régression sur les Composants (Interopérabilité)

**Objectif :** Confirmer que la nouvelle interface CSS n'a brisé aucune des fonctionnalités visuelles introduites dans les Sprints 04 et 05.

- [x] **Uploader de documents (US-003) :** Le module `st.file_uploader` de test ou de session est toujours aligné et utilisable en sidebar ou vue principale.
- [x] **Interaction Vocale (US-005) :** Déclencher une lecture vocale. Le Widget `st.audio` s'affiche toujours correctement (non rogné ou masqué).
- [x] **Analyse de Sentiment (US-006) :** Taper "J'adore Paris!". Vérifier que la métrique `st.metric` s'affiche bien (vert) ET que la couleur de flèche/du texte reste cohérente avec sa polarité (et non pas altérée par le CSS global).
- [x] **Responsive Mobile :** Redimensionner la fenêtre du navigateur en taille "téléphone". La mise en page ne doit pas être disloquée ni entraîner un ascenseur horizontal persistant.
- [x] **Statut :** PASSÉ

---

## 📝 Rapport Final de QA

- **Verdict Global :** SUCCÈS (Interface complètement validée)
- **Remarques :** Excellent rendu global en mode dark, avec l'image Unsplash en en-tête. Aucun conflit avec les composants existants (audio, métriques sentiment).
