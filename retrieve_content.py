import streamlit as st
import readFunctions as rf

def retrieve_content_file_uploaded(file_uploaded):
    if file_uploaded is not None:
        extension_fichier = file_uploaded.name.split('.')[-1].lower()

        if extension_fichier in ["pdf", "docx"]:
            st.markdown("---")
                    
            if extension_fichier == "pdf":
                file_content = rf.lire_pdf(file_uploaded)
                return file_content
            
            else:
                file_content = rf.lire_docx(file_uploaded)
                return file_content
         
        else:
            st.markdown("---")
            st.error("⚠️ Seuls les fichiers PDF, DOCX, et PPTX sont acceptés.")