# Synthèse de la Rétrospective - Sprint 01

**Date de réalisation :** Février 2026
**Objectif :** Socle Technique et Interface Chatbot de base (US-001, US-002)

## 1. Ce qui a bien fonctionné (Succès)
- **Mise en place de l'infrastructure :** La configuration de l'arborescence Python, de l'environnement virtuel (`virtualenv`) et du fichier `requirements.txt` a permis un démarrage rapide et très propre de l'ensemble du projet.
- **Lancement de l'interface :** Le POC initial sous **Streamlit** a été concluant. La boucle de chat via `st.chat_message` et `st.chat_input` a été implémentée rapidement permettant une vraie interaction Homme-Machine immédiate.

## 2. Difficultés et Blocages (Défis)
- **Logique d'état Streamlit :** Le fonctionnement du moteur Streamlit, qui recharge entièrement la page à chaque interaction, a nécessité un temps de prise en main pour maîtriser `st.session_state` afin de conserver l'historique de la conversation ("mémoire" temporaire).

## 3. Plan d'Action pour la suite
- Prévoir la modularité absolue du code en isolant toujours les futures logiques lourdes hors de `app.py`.