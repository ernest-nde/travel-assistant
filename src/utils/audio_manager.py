import io
import logging
from gtts import gTTS

logger = logging.getLogger(__name__)

class AudioManager:
    """Service gérant la synthèse vocale (Text-to-Speech)"""

    @staticmethod
    def generate_tts_bytes(text: str, lang: str = "fr") -> io.BytesIO:
        """
        Convertit un texte en données audio MP3 (en mémoire, BytesIO)
        """
        try:
            tts = gTTS(text=text, lang=lang, slow=False)
            audio_bytes = io.BytesIO()
            tts.write_to_fp(audio_bytes)
            audio_bytes.seek(0)
            return audio_bytes
        except Exception as e:
            logger.error(f"Erreur lors de la génération TTS: {str(e)}")
            return None
