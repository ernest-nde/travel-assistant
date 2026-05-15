"""Configuration du projet"""

import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()


class Config:
    """Configuration centralisée de l'application"""

    # Version
    VERSION = "0.1.0"

    # API Keys
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

    # Chemins
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(ROOT_DIR, "data")

    # Debug mode
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    @classmethod
    def validate(cls):
        """Valide la configuration minimale"""
        if not cls.GEMINI_API_KEY and not cls.OPENAI_API_KEY:
            raise ValueError(
                "Au moins une clé API LLM doit être configurée "
                "(GEMINI_API_KEY ou OPENAI_API_KEY)"
            )
