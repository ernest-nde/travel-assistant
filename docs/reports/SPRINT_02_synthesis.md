# Synthèse de la Rétrospective - Sprint 02

**Date de réalisation :** Mars 2026
**Objectif :** Traitement de Documents PDF (US-003 / INFRA-008)

## 1. Ce qui a bien fonctionné (Succès)
- **Efficacité de PyPDF :** L'intégration de la librairie standard et légère `pypdf` a répondu en tous points à l'objectif sans surcharger le projet de dépendances complexes (type lang-chain ou composants très lourds).
- **Propreté IO :** L'extraction du texte directement depuis la RAM (utilisation de `io.BytesIO` récupéré depuis le composant d'upload Streamlit) a permis d'éviter de manipuler l'infrastructure de fichiers de l'OS (pas de fichiers temporaires polluants).

## 2. Difficultés et Blocages (Défis)
- **Rétention des données extraites :** Il a fallu s'assurer que le contenu lu n'était pas re-traité ou écrasé lors du rerender très "capricieux" de l'interface dès lors qu'un second message était entré par l'utilisateur.

## 3. Plan d'Action pour la suite
- Découpling strict continu : le `DocumentProcessor` doit rester une classe utilitaire complètement aveugle de son interface appelante.