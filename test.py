import streamlit as st

from PyPDF2 import PdfReader
import docx


def lire_pdf(fichier):
    lecteur_pdf = PdfReader(fichier)
    texte = ""

    for page in lecteur_pdf.pages:
        page_text = page.extract_text()
        if page_text:  # évite None
            texte += page_text + "\n"

    return texte


file_uploaded = st.file_uploader("Téléverser votre document (Max size: 5MB)")
if st.button("Lire le contenu du fichier"):
    text=lire_pdf(file_uploaded)
    st.write(text)