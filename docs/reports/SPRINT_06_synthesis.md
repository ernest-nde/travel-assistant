# Synthèse de la Rétrospective - Sprint 06

**Date :** 06 avril 2026
**Objectif :** Refonte Premium de l'Interface Graphique (US-007 / UX-005)

## 1. Ce qui a bien fonctionné (Succès)
- **Architecture Hybride Élégante :** L'approche consistant à séparer la configuration globale de l'UI (`.streamlit/config.toml`) des ajustements précis (`src/assets/styles.css`) injectés via `unsafe_allow_html` s'est révélée excellente. Elle a permis un découplage total entre la logique métier et le "Glassmorphism" applicatif.
- **Effet "Wow" atteint :** L'interface a franchi un cap grâce à l'incorporation fluide d'un vrai Mode Sombre, d'avatars contextuels premium, et d'une bannière immersive, validant le cahier des charges avec un design qualitatif.
- **Déploiement Maintenu Simple :** Malgré ces ajouts esthétiques avancés, le lancement de l'application demeure aussi basique et rapide qu'avant (`streamlit run src/app.py`).

## 2. Difficultés et Blocages (Défis)
- **Fragilité du CSS Streamlit :** C'est le point central de friction. Cibler des éléments DOM dans Streamlit implique souvent de compter sur des noms de classes générés aléatoirement par le moteur (hash), qui peuvent changer d'une version à l'autre, exposant le design à de forts risques de régression.
- **Effets de bords du chargement :** L'image injectée en bannière a causé quelques décalages de scroll natif lors du premier rendu de page avant le chargement total.
- **Gestion du Cache Statique :** L'ajout de fichiers statiques (fichiers CSS isolés) révèle qu'il faudra, à l'avenir, penser à la gestion du cache navigateur ou configure web Nginx/Apache.

## 3. Plan d'Action pour les prochains sprints (Améliorations)
Pour pérenniser ces avancées esthétiques sans briser l'application aux prochaines mises à jour :
1. **Stratégie CSS robuste :** Bannir le ciblage des classes générées. Appliquer des règles CSS strictes en ciblant prioritairement les attributs inaltérables `data-testid="..."` et systématiser l'usage d'un unique fichier `styles.css`.
2. **Localité des Assets :** S'assurer de rapatrier nos images (ex: bannières Unsplash) en local ou sur un CDN pérenne pour permettre une exécution hors-ligne sans image brisée.
3. **Tests Visuels (Visual Regression Testing) :** Face aux surcharges CSS forcées (`!important`), l'intégration d'un outillage de non-régression visuelle devient indispensable pour éviter qu'une montée de version Streamlit ne casse toute l'UI existante.
4. **Cache Busting :** Gérer les stratégies de cache sur les assets statiques pour nos CI/CD.
