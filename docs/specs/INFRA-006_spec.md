# Spécification Technique - US-007 : Interface Graphique Premium (INFRA-006)

## 1. Objectif
Améliorer radicalement l'interface utilisateur (UI) et l'expérience (UX) du Travel Assistant. Le but est d'abandonner l'esthétique "par défaut" de Streamlit pour offrir un rendu premium, immersif, ergonomique, en adéquation avec les codes des applications de voyage modernes.

## 2. Approche Technologique (UI/UX)

La mise en forme se décomposera en deux axes principaux pour la customisation de Streamlit :

### 2.1. Theming Global (Streamlit Config)
- **Configuration** : Création du fichier `.streamlit/config.toml` pour définir le "Theme Base".
- **Attributs clés à surcharger** :
  - `primaryColor` : Couleur d'action (ex: un cyan ou bleu azur profond).
  - `backgroundColor` / `secondaryBackgroundColor` : Choix d'une palette élégante (mode sombre conseillé pour un "waouh" effect, ou mode clair très épuré).
  - `textColor` et `font` : Utilisation d'une fonte "sans serif" moderne.

### 2.2. Custom CSS & Glassmorphism
- **Injection CSS Dynamique** : Une fonction Python dédiée lira un fichier ou une chaîne CSS pour l'injecter au démarrage via `st.markdown("<style>...</style>", unsafe_allow_html=True)`.
- **Modifications visuelles poussées** :
  - Masquage des éléments natifs : Header de menu hamburger, le footer (`footer {visibility: hidden;}`).
  - **Glassmorphism** : Rendre certains éléments (comme la *sidebar*) semi-transparents avec un flou en arrière-plan (`backdrop-filter: blur(10px)`).
  - Ajustements structurels : Réduction des énormes marges par défaut (`padding-top: 2rem` au lieu de 6rem).
  - Arrondi (*border-radius*) customisé pour tous les boutons ou entrées texte existants.

### 2.3. Habillage & Médias
- **Bannière d'en-tête** : Afficher une image attrayante, fine et au format paysage, servant de header stylisé pour le bot.
- **Avatars Personnalisés** : La méthode `st.chat_message()` recevra des emojis ou de petites URLs vers des icônes customisés pour styliser les messages (ex: 👨 pour le testeur, ✈️ ou un robot pour le chatbot).

### 2.4. Intégration des composants préexistants
- Le CSS devra respecter (ne pas briser) la fonctionnalité du téléversement (`st.file_uploader`), le lecteur vocal de l'US-005 (`st.audio()`) et les badges d'analyse de sentiment de l'US-006 (`st.metric`).

## 3. Contraintes & Points d'Attention
- **Ciblage CSS capricieux** : Streamlit génère souvent des classes aléatoires (hash). Il faudra cibler les attributs `data-testid` ou l'agencement HTML structurel sans casser l'applicatif en cas de mise à jour légère de la librairie.
- **Support Mobile** : Conserver le côté "responsive" natif du framework. Le CSS ajouté ne doit pas imposer de largeurs fixes.

## 4. Stratégie de Validation (QA)
- **Test UX** : Validation manuelle reposant strictement sur l'effet esthétique.
- **Test d'affichage** : L'identité de marque (Brand Colors) est globalement appliquée (boutons + sidebar + fond) et la bannière s'affiche en permanence en tête des messages.
