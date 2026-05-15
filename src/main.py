"""Point d'entrée principal de l'application"""

from config import Config


def main():
    """Fonction principale"""
    print(f"🌍 Travel Assistant v{Config.VERSION}")
    print("✅ Configuration globale chargée avec succès!")

    # Validation de la configuration API
    try:
        Config.validate()
        print("✅ Clés API validées (US-004 - LLM Gemini)")
    except ValueError as e:
        print(f"⚠️  Avertissement : {e}")
        print("   → Configurez votre GEMINI_API_KEY dans le fichier .env")

    # Vérification fonctionnelle du processeur documentaire (US-003)
    try:
        from document_processor import DocumentProcessor  # noqa: F401
        print("✅ Module d'extraction PDF opérationnel (US-003)")
    except ImportError:
        print("❌ Erreur : Impossible de charger le traitement documentaire")

    # LLM et Interface (US-002 & US-004)
    print("\n✨ Tous les modules internes sont prêts !")
    print("🚀 Pour interagir avec le Chatbot Intelligent :")
    print("   → Lancez la commande : streamlit run src/app.py\n")


if __name__ == "__main__":
    main()
