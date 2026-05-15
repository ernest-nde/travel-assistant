# Spécification Technique - US-006 : Analyse de Sentiment Visuelle (INFRA-005)

## 1. Objectif
Enrichir l'expérience utilisateur (UX) du Travel Assistant en ajoutant une évaluation en temps réel du sentiment (humeur) des messages utilisateurs. Le résultat doit être communiqué via une interface hautement visuelle et native de Streamlit.

## 2. Piste de Solution Technique (NLP et UI)

### 2.1. Module d'Analyse NLP (Sentiment Analysis)
- **Choix Technologique** : Pour ne pas surcharger l'API payante LLM (Gemini) et réduire la latence, nous recommandons le calcul de sentiment en local. La bibliothèque `TextBlob` ou `VADER` (`nltk.sentiment.vader`) en Python est idéale car très rapide, légère, et suffisante pour catégoriser (Positif/Négatif/Neutre).
- **Architecture Modulaire** : Créer un fichier de service `src/utils/sentiment_analyzer.py`. Ce module exportera une unique fonction capable de prendre un texte en entrée, de calculer la polarité, et de renvoyer un dictionnaire de résultat avec un score (-1 à 1) et une catégorie ("Positif", "Négatif", "Neutre").

### 2.2. Intégration Visuelle Native Streamlit
- **Affichage Numérique (`st.metric`)** : Utiliser la brique avancée `st.metric(label, value, delta)`. 
  - La propriété `delta` colorera automatiquement en vert avec une flèche vers le haut un score positif, et en rouge vers le bas pour le négatif.
- **Barre Visuelle (`st.progress` / Jauge)** : Pour agrémenter le design, l'ajout conjonctif d'une barre de sentiment (`st.progress`) convertissant l'intervalle [-1, 1] en pourcentage [0%, 100%] rendra l'interface encore plus ludique.
- **Emplacement UI** : Ces métriques seront positionnées discrètement (ex. dans `st.sidebar` ou juste sous les bulles de l'utilisateur correspondantes) pour ne pas briser la fluidité de la conversation LLM standard.

## 3. Contraintes & Points d'Attention
- **Mise à jour d'Infrastructure** : Ajouter la librairie choisie (ex: `textblob`) au package du projet (`requirements.txt`) et initialiser les lexiques associés.
- **UX Non-intrusive** : L'analyse de sentiment ne doit pas bloquer la requête vers LLM. Ces actions peuvent être rendues de manière concurrente pour une UI réactive.

## 4. Stratégie de Validation (Tests)
- Le module `sentiment_analyzer` devra posséder trois tests unitaires couvrant les polarités : Positif ("J'adore cette ville"), Négatif ("Erreur, je déteste ce voyage") et Neutre ("Je pars lundi").
- Validation manuelle : Vérifier l'UI Streamlit et s'assurer que la fonction `st.metric` prend bien la couleur adéquate rouge/vert.
