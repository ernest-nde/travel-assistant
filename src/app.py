"""
Travel Assistant Chatbot - Application Principale
Interface Streamlit pour interaction conversationnelle
"""

import streamlit as st
import io
import uuid

# Import des modules internes
from chatbot.interface import ChatInterface
from config import Config
from utils.audio_manager import AudioManager
from utils.sentiment_analyzer import SentimentAnalyzer
import speech_recognition as sr

# Configuration de la page
# Configuration de la page
st.set_page_config(
    page_title="Travel Assistant",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
)

def load_css():
    """Charge le fichier CSS personnalisé pour le style de l'interface"""
    import os
    css_file = os.path.join(os.path.dirname(__file__), "assets", "styles.css")
    if os.path.exists(css_file):
        with open(css_file, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def initialize_session():
    """Initialise la session Streamlit si nécessaire"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.conversation_started = False
        st.session_state.session_id = str(uuid.uuid4())

        # Message de bienvenue
        welcome_message = ChatInterface.get_welcome_message()
        st.session_state.messages.append(welcome_message)
        st.session_state.conversation_started = True


def render_sidebar():
    """Rendu de la barre latérale"""
    with st.sidebar:
        st.title("⚙️ Configuration")

        # Section API (pour US-003)
        with st.expander("🔑 Clés API", expanded=False):
            st.info(
                "⚠️ Les clés API seront nécessaires pour US-003 "
                "(Intégration LLM). Pour l'instant, l'interface est "
                "en mode démo."
            )

        st.divider()

        # Section Documents de voyage (US-003)
        st.subheader("📄 Documents de voyage")
        uploaded_file = st.file_uploader(
            "Téléversez vos réservations, guides ou billets (PDF)", type=["pdf"]  # noqa: E501
        )

        if uploaded_file is not None:
            with st.spinner("Analyse du document en cours..."):
                try:
                    # Lecture via Streamlit retourne un objet BytesIO équivalent  # noqa: E501
                    pdf_bytes = io.BytesIO(uploaded_file.getvalue())

                    # Appel du module découplé
                    from document_processor import DocumentProcessor

                    extracted_text = DocumentProcessor.extract_text_from_pdf(pdf_bytes)  # noqa: E501

                    # Indication de succès
                    st.success(
                        f"Document '{uploaded_file.name}' lu avec succès ! "
                        f"({len(extracted_text)} caractères extraits)"
                    )

                    # Conserver en mémoire de session
                    if "uploaded_documents_text" not in st.session_state:
                        st.session_state.uploaded_documents_text = []

                    # Éviter les doublons basiques
                    if "uploaded_documents_names" not in st.session_state:
                        st.session_state.uploaded_documents_names = []

                    if (
                        uploaded_file.name
                        not in st.session_state.uploaded_documents_names
                    ):
                        st.session_state.uploaded_documents_text.append(extracted_text)  # noqa: E501
                        st.session_state.uploaded_documents_names.append(
                            uploaded_file.name
                        )

                except ValueError as ve:
                    st.error(f"Erreur de traitement : {str(ve)}")

        st.divider()

        # Section Session
        st.subheader("🗂️ Session")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("🆕 Nouveau", use_container_width=True):
                # Réinitialiser la conversation
                st.session_state.messages = ChatInterface.clear_history()
                st.session_state.conversation_started = False
                st.rerun()

        with col2:
            if st.button("🔄 Reset", use_container_width=True):
                # Réinitialiser complètement la session
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.rerun()

        st.divider()

        # Section Audio (US-005)
        st.subheader("🔊 Audio")
        enable_tts = st.toggle("Activer la voix de l'assistant", value=True, key="enable_tts")
        
        try:
            from audio_recorder_streamlit import audio_recorder
            st.caption("🎙️ Enregistrement vocal")
            # Utilisation d'une key fixe pour le composant, et ajustement des couleurs pour le Dark Mode
            recorded_audio = audio_recorder(
                text="Clic pour Démarrer/Arrêter", 
                icon_size="1x", 
                key="audio_recorder",
                neutral_color="#F8FAFC",  # Blanc pour visibilité en mode sombre
                recording_color="#00B4D8", # Cyan premium lors de l'enregistrement
                pause_threshold=2.0
            )
            
            if recorded_audio:
                audio_hash = hash(recorded_audio)
                # Vérifier si cet audio exact a déjà été traité
                if st.session_state.get("last_audio_hash") != audio_hash:
                    st.info("Audio capturé. Transcription en cours...")
                    try:
                        r = sr.Recognizer()
                        with sr.AudioFile(io.BytesIO(recorded_audio)) as source:
                            audio = r.record(source)
                        text = r.recognize_google(audio, language="fr-FR")
                        
                        # Marquer comme traité avant rerun
                        st.session_state["last_audio_hash"] = audio_hash
                        
                        if text:
                            st.session_state.pending_action = {"prompt": text, "task_type": "chat_normal"}
                            st.rerun()
                    except sr.UnknownValueError:
                        st.session_state["last_audio_hash"] = audio_hash
                        st.error("L'audio n'a pas pu être compris. Veuillez réessayer.")
                    except Exception as e:
                        st.session_state["last_audio_hash"] = audio_hash
                        st.error(f"Erreur de transcription : {str(e)}")
        except ImportError:
            st.warning("Module d'enregistrement manquant.")

        st.divider()

        # Informations
        st.subheader("ℹ️ Informations")
        st.caption(f"**Version** : {Config.VERSION}")
        st.caption(f"**Messages** : {len(st.session_state.messages)}")
        st.caption(f"**Session ID** : {st.session_state.session_id[:8]}...")

        st.divider()

        # Instructions
        with st.expander("📖 Guide d'utilisation"):
            st.markdown(
                """
            **Comment utiliser l'assistant :**

            1. Tapez votre question dans la zone de saisie
            2. Appuyez sur Entrée ou cliquez sur Envoyer
            3. L'assistant vous répondra

            **Exemples de questions :**
            - "Je veux visiter Paris pendant 3 jours"
            - "Quelles activités à Tokyo?"
            - "Quel budget pour l'Italie?"

            **Boutons :**
            - 🆕 **Nouveau** : Démarre une nouvelle conversation
            - 🔄 **Reset** : Réinitialise complètement l'application
            """
            )


def render_chat():
    """Rendu de la zone de chat"""
    # Conteneur pour l'historique de messages
    chat_container = st.container()

    # Mise en cache de la génération TTS pour éviter d'appeler l'API à chaque re-render
    @st.cache_data(show_spinner=False, max_entries=50)
    def cached_tts(text: str):
        return AudioManager.generate_tts_bytes(text)

    # Mise en cache de l'analyse de sentiment
    @st.cache_data(show_spinner=False, max_entries=100)
    def cached_sentiment(text: str):
        return SentimentAnalyzer.analyze(text)

    with chat_container:
        # Afficher tous les messages de l'historique
        for message in st.session_state.messages:
            role = message["role"]
            content = message["content"]

            # Déterminer l'avatar (Premium)
            avatar = "✈️" if role == "assistant" else "👨"

            with st.chat_message(role, avatar=avatar):
                st.markdown(content)
                
                # Ajout de l'Analyse de Sentiment pour les requêtes de l'utilisateur
                if role == "user":
                    sentiment = cached_sentiment(content)
                    if sentiment:
                        s_col1, s_col2 = st.columns([0.2, 0.8])
                        with s_col1:
                            delta_val = round(sentiment["score"], 2) if sentiment["score"] != 0 else None
                            st.metric(label="Sentiment", value=sentiment["category"], delta=delta_val, label_visibility="collapsed")
                        with s_col2:
                            prog_val = int(((sentiment["score"] + 1) / 2) * 100)
                            st.progress(prog_val, text="Barre de polarité")
                            
                # Ajout de l'audio TTS pour les messages de l'assistant
                elif role == "assistant" and st.session_state.get("enable_tts", True):
                    audio_bytes = cached_tts(content)
                    if audio_bytes:
                        st.audio(audio_bytes, format='audio/mp3')

    # Affichage des boutons d'actions rapides (seulement si des documents sont présents)
    if st.session_state.get("uploaded_documents_text") and "pending_action" not in st.session_state:
        st.write("") # Espacement
        st.caption("⚡ Actions rapides sur vos documents :")
        c1, c2, c3, c4 = st.columns(4)
        if c1.button("📝 Résumer voyage", use_container_width=True):
            st.session_state.pending_action = {"prompt": "Peux-tu me faire un résumé de ce voyage ?", "task_type": "resume_voyage"}
            st.rerun()
        if c2.button("🗺️ Itinéraire 3J", use_container_width=True):
            st.session_state.pending_action = {"prompt": "Génère un itinéraire de 3 jours à partir de ce document.", "task_type": "creer_itineraire"}
            st.rerun()
        if c3.button("💡 5 Activités secr.", use_container_width=True):
            st.session_state.pending_action = {"prompt": "Quelles sont les 5 meilleures activités secrètes pour cette destination ?", "task_type": "conseils_activites"}
            st.rerun()
        if c4.button("📄 Analyser pdf", use_container_width=True):
            st.session_state.pending_action = {"prompt": "Analyse ce document libre et fais-en une synthèse.", "task_type": "analyse_generique"}
            st.rerun()

    # Zone de saisie utilisateur
    user_input = st.chat_input("💬 Écrivez votre message ici...", key="chat_input")  # noqa: E501

    # Caching du client LLM pour éviter les réinitialisations
    @st.cache_resource
    def get_llm_client_v2():
        try:
            from llm.gemini_client import GeminiClient
            return GeminiClient()
        except ValueError as e:
            st.error(str(e))
            return None

    llm = get_llm_client_v2()

    # Traitement du message (manuel ou déclenché par une action rapide)
    if user_input or "pending_action" in st.session_state:
        # Déterminer la source de l'action
        if user_input:
            prompt = user_input
            task_type = "chat_normal"
        else:
            prompt = st.session_state.pending_action["prompt"]
            task_type = st.session_state.pending_action["task_type"]
            del st.session_state["pending_action"]

        # Ajouter le message utilisateur
        user_message = ChatInterface.format_message("user", prompt)
        st.session_state.messages.append(user_message)

        # Afficher le message utilisateur immédiatement
        with st.chat_message("user", avatar="👨"):
            st.markdown(prompt)

        if llm:
            with st.chat_message("assistant", avatar="✈️"):
                with st.spinner("L'assistant réfléchit..."):
                    # Récupérer les documents extraits du Session State (US-003)
                    context_docs = st.session_state.get("uploaded_documents_text", [])
                    
                    # Récupérer l'historique de conversation (les 6 derniers messages)
                    chat_history_list = []
                    # st.session_state.messages contient déjà le message utilisateur courant en dernier
                    history_msgs = st.session_state.messages[:-1][-6:]
                    for m in history_msgs:
                        role_str = "Utilisateur" if m["role"] == "user" else "Assistant"
                        chat_history_list.append(f"{role_str}: {m['content']}")
                    chat_history_text = "\n".join(chat_history_list) if chat_history_list else None
                    
                    # Appel à Gemini avec le type de tâche spécifié
                    response = llm.generate_response(
                        prompt, 
                        context_documents=context_docs, 
                        task_type=task_type,
                        chat_history=chat_history_text
                    )
                    st.markdown(response)

            # Ajouter la réponse à l'historique
            assistant_message = ChatInterface.format_message("assistant", response)
            st.session_state.messages.append(assistant_message)
            st.rerun()
        else:
            with st.chat_message("assistant", avatar="✈️"):
                error_msg = "L'assistant n'est pas configuré. Vérifiez votre clé d'API."
                st.error(error_msg)
            # Ajouter la réponse à l'historique
            assistant_message = ChatInterface.format_message("assistant", error_msg)
            st.session_state.messages.append(assistant_message)
            st.rerun()


def generate_demo_response(user_input: str) -> str:
    """
    Génère une réponse de démonstration (temporaire pour US-002)
    Sera remplacé par un vrai LLM dans US-003
    """
    user_lower = user_input.lower()

    # Détection de mots-clés simples
    if any(word in user_lower for word in ["paris", "france"]):
        return (
            "🗼 **Paris** est une destination merveilleuse! "
            "C'est la capitale de la France, connue pour la Tour Eiffel, "
            "le Louvre, et sa gastronomie exceptionnelle.\n\n"
            "_Note: Cette réponse est générée par un système de démonstration. "  # noqa: E501
            "L'intégration d'un vrai LLM arrivera avec US-003._"
        )
    elif any(word in user_lower for word in ["itinéraire", "planifier", "jours"]):  # noqa: E501
        return (
            "📅 Je peux vous aider à créer un itinéraire personnalisé! "
            "Pourriez-vous me préciser :\n"
            "- Votre destination\n"
            "- La durée de votre séjour\n"
            "- Vos centres d'intérêt (culture, nature, gastronomie...)\n\n"
            "_Note: La génération d'itinéraires sera disponible dans une future version._"
        )
    elif any(word in user_lower for word in ["budget", "coût", "prix"]):
        return (
            "💰 Je peux vous donner une estimation de budget pour votre voyage! "  # noqa: E501
            "Dites-moi votre destination et la durée de votre séjour.\n\n"
            "_Note: L'estimation de budget détaillée sera disponible dans une future version._"  # noqa: E501
        )
    else:
        return (
            "Je comprends votre question. "
            "Pour l'instant, je suis en mode démo (US-002). "
            "Les fonctionnalités conversationnelles avancées seront disponibles "  # noqa: E501
            "avec l'intégration du LLM (US-003).\n\n"
            "**Puis-je vous aider avec :**\n"
            "- Des informations sur une destination?\n"
            "- La planification d'un itinéraire?\n"
            "- Une estimation de budget?"
        )


def main():
    """Fonction principale de l'application"""
    # Initialiser la session
    initialize_session()
    
    # Charger le style Premium
    load_css()

    # Titre principal et Bannière
    st.image("https://images.unsplash.com/photo-1436491865332-7a61a109cc05?q=80&w=1200&auto=format&fit=crop", width=1200)
    st.title("✈️ Travel Assistant Chatbot")
    st.caption("Votre compagnon de voyage intelligent • _Premium Edition_")

    # Rendu de la sidebar
    render_sidebar()

    # Rendu du chat
    render_chat()

    # Footer
    st.divider()
    st.caption(
        "✨ Travel Assistant v"
        + Config.VERSION
        + " | Développé avec Streamlit | US-002 : Interface Chatbot"
    )


if __name__ == "__main__":
    main()
