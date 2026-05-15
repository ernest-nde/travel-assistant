# Synthèse de la Rétrospective - Sprint 03

**Date de réalisation :** Mars 2026
**Objectif :** Intégration du LLM - API Google Gemini (US-004 / INFRA-003)

## 1. Ce qui a bien fonctionné (Succès)
- **Robustesse de la connexion :** Le couplage au LLM via le module Python `google-generativeai` s'est effectué avec un grand succès.
- **Sécurité et Retry Logic :** La configuration `python-dotenv` empêche formellement de committed la clef API, et l'implémentation algorithmique d'un retry pattern encaisse très bien les timeouts du réseau ou limitations quotas (429 Too Many Requests).

## 2. Difficultés et Blocages (Défis)
- **Latence de réponse :** Le temps qu'il faut à l'API LLM pour répondre à un long document est un défi asynchrone dans un éco-système Streamlit très synchrone.
- **Gestion fine du Prompts :** Insérer le contexte (le texte du PDF éventuel) dans la requête Gemini de manière systématisée pour générer des réponses expertes de voyage exigeait de jongler avec la concaténation complexe de chaînes.

## 3. Plan d'Action pour la suite
- Conserver une très forte compartimentisation du wrapper LLM pour qu'une migration potentielle (vers OpenAI, HuggingFace ou un autre modèle) n'ait aucun impact sur l'interface graphique.