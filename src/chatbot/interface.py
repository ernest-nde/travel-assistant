"""Interface de chat - Gestion de l'affichage et de la session"""

from typing import List, Dict
from datetime import datetime


class ChatInterface:
    """
    Gestionnaire de l'interface de chat
    Centralise la logique d'affichage et de gestion de session
    """

    @staticmethod
    def format_message(role: str, content: str) -> Dict[str, str]:
        """
        Formate un message pour l'historique

        Args:
            role: 'user' ou 'assistant'
            content: Contenu du message

        Returns:
            Dictionnaire du message formaté
        """
        return {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(),
        }

    @staticmethod
    def get_welcome_message() -> Dict[str, str]:
        """Retourne le message de bienvenue standard"""
        return ChatInterface.format_message(
            role="assistant",
            content=(
                "🌍 **Bonjour et bienvenue dans Travel Assistant!**\n\n"
                "Je suis votre assistant de voyage personnel. "
                "Je peux vous aider à :\n"
                "- 📅 Planifier des itinéraires jour par jour\n"
                "- 🎯 Trouver des activités et recommandations\n"
                "- 💰 Estimer votre budget de voyage\n"
                "- ☀️ Connaître la météo de votre destination\n\n"
                "**Comment puis-je vous aider aujourd'hui?**"
            ),
        )

    @staticmethod
    def count_messages_by_role(messages: List[Dict]) -> Dict[str, int]:
        """
        Compte les messages par rôle

        Args:
            messages: Liste des messages

        Returns:
            Dictionnaire avec compteurs par rôle
        """
        counts = {"user": 0, "assistant": 0}
        for msg in messages:
            role = msg.get("role", "unknown")
            if role in counts:
                counts[role] += 1
        return counts

    @staticmethod
    def clear_history() -> List[Dict]:
        """
        Réinitialise l'historique avec uniquement le message de bienvenue

        Returns:
            Liste avec le message de bienvenue
        """
        return [ChatInterface.get_welcome_message()]
