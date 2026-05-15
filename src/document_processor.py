"""Module de traitement et d'extraction de contenu documentaire"""

import io

from pypdf import PdfReader
from pypdf.errors import PdfReadError


class DocumentProcessor:
    """Classe utilitaire pour traiter les documents de voyage (ex: PDF)."""

    @staticmethod
    def extract_text_from_pdf(file_bytes: io.BytesIO) -> str:
        """
        Extrait le texte brut d'un fichier PDF et effectue
        un nettoyage de base.

        Args:
            file_bytes: Objet Bytestream du fichier
                (ex: issu d'un st.file_uploader)

        Returns:
            La chaîne de caractères nettoyée extraite du PDF.

        Raises:
            ValueError: Si le fichier est vide, illisible, corrompu
                ou d'un format non géré.
        """
        try:
            reader = PdfReader(file_bytes)

            if len(reader.pages) == 0:
                raise ValueError("Le document PDF ne contient aucune page.")

            extracted_text = []
            for num, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    extracted_text.append(text)

            full_text = "\n".join(extracted_text)

            if not full_text.strip():
                raise ValueError(
                    "Aucun texte lisible n'a pu être extrait. "
                    "Il s'agit peut-être d'une image scannée."
                )

            # Nettoyage de base
            cleaned_text = " ".join(full_text.split())
            return cleaned_text

        except PdfReadError as e:
            raise ValueError(
                f"Le fichier PDF est corrompu ou illisible: {str(e)}"
            )
        except Exception as e:
            raise ValueError(
                f"Erreur inattendue lors de la lecture du fichier: {str(e)}"
            )
