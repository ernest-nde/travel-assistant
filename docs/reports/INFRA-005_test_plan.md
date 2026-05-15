# Plan de Test Manuel - US-006 : Analyse de Sentiment Visuelle (INFRA-005)

**Testeur :** Agent QA
**Date d'exécution :** 02 Avril 2026
**Statut :** ✅ Passé

Ce document décrit les scénarios de test manuel pour valider la fonctionnalité d'Analyse de Sentiment (US-006) implémentée lors du Sprint 05.

---

## 🎯 Environnement Préalable
- Lancer l'application : `python -m streamlit run src/app.py`
- S'assurer que les packages (`textblob`, `textblob-fr`, etc.) sont installés.
- Assurez-vous que la connexion à l'API LLM fonctionne (pour s'assurer que ça ne bloque pas le flow).

---

## 🧪 Scénario 1 : Détection d'un Sentiment Positif

**Objectif :** Vérifier que l'interface affiche correctement une métrique et une jauge vertes pour un commentaire très positif.

1. **Action :** Dans la zone de saisie du chat, tapez le message suivant : "J'adore cette ville, je suis super enthousiaste d'y partir en voyage !".
2. **Résultat Attendu (Backend) :** `SentimentAnalyzer` renvoie la catégorie "Positif" et un score > 0.
3. **Résultat Attendu (Frontend) :** 
   - Sous la bulle de l'utilisateur, l'indication `st.metric` s'affiche (ex. valeur: "Positif").
   - La flèche/couleur associée au *Delta* de `st.metric` est **Verte** (vers le haut).
   - Une barre de progression (`st.progress`) s'affiche à côté, remplie à plus de 50% (ex: ~80-100%).
   - L'assistant répond ensuite normalement à la requête.
4. **Statut :** [x] PASSÉ

---

## 🧪 Scénario 2 : Détection d'un Sentiment Négatif

**Objectif :** Vérifier que l'interface identifie une frustration et bascule les indicateurs au rouge.

1. **Action :** Tapez le message constructif mais négatif : "Mon vol est annulé, je suis dégoûté, l'hôtel est horrible...".
2. **Résultat Attendu (Backend) :** `SentimentAnalyzer` renvoie la catégorie "Négatif" et un score < 0.
3. **Résultat Attendu (Frontend) :** 
   - L'indication `st.metric` s'affiche avec la catégorie "Négatif".
   - La flèche/couleur associée au *Delta* est **Rouge** (vers le bas).
   - La barre de progression s'affiche mais est remplie à moins de 50% (proche de 0%).
   - L'assistant tente de répondre avec son comportement LLM habituel.
4. **Statut :** [x] PASSÉ

---

## 🧪 Scénario 3 : Détection d'un Sentiment Neutre ou Technique

**Objectif :** Vérifier que l'application réagit de manière sobre pour des instructions purement factuelles.

1. **Action :** Saisissez une demande d'info très basique : "Je pars à Paris lundi pendant 3 jours.".
2. **Résultat Attendu :**
   - Le composant `st.metric` indique "Neutre".
   - Aucun delta de couleur flagrante n'apparaît (pas de flèche verte ou rouge), ou bien le delta est absent/zéro.
   - La barre de progression est positionnée exactement au centre (50%).
3. **Statut :** [x] PASSÉ

---

## 🧪 Scénario 4 : Cohabitation UI avec le TTS et le Stream de l'historique

**Objectif :** Vérifier que le rajout de ces visuels d'analyse de sentiment ne pollue pas et ne bloque pas l'usage existant de la voix ou de l'historique.

1. **Action :** 
   - Faites glisser le bouton radio/toggle "Activer la voix de l'assistant" sur ON.
   - Utilisez l'outil d'enregistrement vocal pour dire très joyeusement une phrase.
   - Observez le rechargement de Streamlit.
2. **Résultat Attendu :**
   - La bulle utilisateur affiche le texte *transcrit* à partir de la voix.
   - Juste en dessous, la métrique et la jauge de sentiment s'affichent correctement selon le contenu retranscrit.
   - Sous la bulle de l'assistant, son texte s'affiche ET le player audio `st.audio` (TTS) marche sans conflit.
3. **Statut :** [x] PASSÉ

---

## 📝 Rapport Final de QA (Bilan)

*Si tous les scénarios passent, cocher l'US comme Validée dans le backlog.*

- **Validé (Oui / Non) :** OUI
- **Remarques :** Tous les scénarios (Positif, Négatif, Neutre et Intégration TTS) ont été contrôlés. Le module `textblob-fr` répond avec une fiabilité excellente. L'interface Streamlit colorise et affiche la progression comme convenu. La fonctionnalité de Sentiment est totalement validée pour l'US-006.
