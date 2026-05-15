"""Tests pour le module d'interface de chat"""

import pytest
from datetime import datetime
from src.chatbot.interface import ChatInterface


def test_format_message():
    """Teste le formatage d'un message"""
    msg = ChatInterface.format_message("user", "Hello")

    assert msg["role"] == "user"
    assert msg["content"] == "Hello"
    assert "timestamp" in msg


def test_get_welcome_message():
    """Teste la génération du message de bienvenue"""
    welcome = ChatInterface.get_welcome_message()

    assert welcome["role"] == "assistant"
    assert "Bonjour" in welcome["content"]
    assert "Travel Assistant" in welcome["content"]


def test_count_messages_by_role():
    """Teste le comptage des messages par rôle"""
    messages = [
        {"role": "assistant", "content": "Bonjour"},
        {"role": "user", "content": "Salut"},
        {"role": "assistant", "content": "Comment ça va?"},
        {"role": "user", "content": "Bien!"},
    ]

    counts = ChatInterface.count_messages_by_role(messages)

    assert counts["user"] == 2
    assert counts["assistant"] == 2


def test_clear_history():
    """Teste la réinitialisation de l'historique"""
    history = ChatInterface.clear_history()

    assert len(history) == 1
    assert history[0]["role"] == "assistant"
    assert "Bonjour" in history[0]["content"]
