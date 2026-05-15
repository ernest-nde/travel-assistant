"""Tests de la configuration"""
import pytest
from src.config import Config


def test_config_version():
    """Vérifie que la version est définie"""
    assert Config.VERSION == "0.1.0"


def test_config_paths_exist():
    """Vérifie que les chemins de configuration sont valides"""
    assert Config.ROOT_DIR is not None
    assert Config.DATA_DIR is not None


def test_config_debug_mode():
    """Vérifie le mode debug"""
    assert isinstance(Config.DEBUG, bool)
