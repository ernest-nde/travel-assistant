"""Client d'intégration pour l'API Google Gemini."""

import os
import google.generativeai as genai
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

class GeminiAPIError(Exception):
    """Exception personnalisée pour les erreurs non récupérables de Gemini."""
    pass

class GeminiClient:
    """Client gérant les appels au modèle Gemini avec Retry Logic."""
    
    def __init__(self, model_name: str = "gemini-2.5-flash-lite"):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key or self.api_key == "your_gemini_api_key_here":
            raise ValueError("La clé GEMINI_API_KEY est introuvable ou invalide dans l'environnement.")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name)

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception_type(Exception),
        reraise=True
    )
    def _call_api(self, prompt: str) -> str:
        """Méthode interne d'appel avec Retry exponentiel (max 3 tentatives)."""
        response = self.model.generate_content(prompt)
        return response.text

    def generate_response(self, user_prompt: str, context_documents: list = None, task_type: str = "chat_normal", chat_history: str = None) -> str:
        """
        Génère une réponse LLM en injectant les documents si fournis.
        
        Args:
            user_prompt: La question de l'utilisateur.
            context_documents: Liste de textes extraits (ex: depuis les PDF).
            task_type: Le type de proactivité attendue ("chat_normal", "resume_voyage", "creer_itineraire", "conseils_activites").
            chat_history: L'historique récent de la conversation formaté en texte.
        """
        full_prompt = ""
        
        # 1. Injection du Persona (Prompt Engineering Proactif)
        if task_type == "resume_voyage":
            full_prompt += "INSTRUCTION SYSTÈME : Tu es un assistant de voyage expert. Ton rôle est d'analyser le document de voyage fourni et d'en extraire un résumé précis et organisé. Liste les dates clés, les lieux, les numéros de réservation et les coûts, sous forme de liste structurée élégante avec des émojis.\n\n"
        elif task_type == "creer_itineraire":
            full_prompt += "INSTRUCTION SYSTÈME : Tu es un créateur d'itinéraires de voyage renommé mondialement. Utilise le document fourni pour déduire la destination. Génère ensuite un itinéraire passionnant de 3 jours, étape par étape (Matin, Midi, Soir). Sois créatif et pratique.\n\n"
        elif task_type == "conseils_activites":
            full_prompt += "INSTRUCTION SYSTÈME : Tu es un guide touristique local passionné. À partir de la destination identifiée dans le document, dresse une liste des 5 meilleures activités secrètes ou restaurants incontournables. Ajoute des conseils pour éviter les pièges à touristes.\n\n"
        elif task_type == "analyse_generique":
            full_prompt += "INSTRUCTION SYSTÈME : Tu es un assistant analytique expert. Analyse le document fourni, identifie son sujet principal (même si ce n'est pas un voyage) et fais-en une synthèse claire, détaillée et neutre, structurée par points clés.\n\n"
        else:
            full_prompt += "INSTRUCTION SYSTÈME : Tu es un compagnon de voyage virtuel très utile et amical. Réponds à la question de l'utilisateur en te basant sur le contexte si fourni.\n\n"
        
        
        # Injection du contexte des documents uploadés
        if context_documents:
            full_prompt += "CONTEXTE À PRENDRE EN COMPTE (Documents fournis) :\n"
            for doc in context_documents:
                full_prompt += f"---\n{doc}\n---\n"
            full_prompt += "\n"
        
        full_prompt += f"QUESTION DE L'UTILISATEUR :\n{user_prompt}"

        # Injection de l'historique conversationnel
        if chat_history:
            full_prompt = f"HISTORIQUE RÉCENT DE LA CONVERSATION :\n{chat_history}\n\n" + full_prompt

        try:
            return self._call_api(full_prompt)
        except Exception as e:
            # Fallback gracieux après épuisement des retries
            return (
                "Je suis désolé, le service d'Intelligence Artificielle "
                "est momentanément indisponible ou surchargé. Veuillez réessayer dans quelques instants."
            )
