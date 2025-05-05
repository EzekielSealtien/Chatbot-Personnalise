import streamlit as st
import talk_with_server as tws
import retrieve_content as r_c
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain_openai.chat_models import ChatOpenAI


st.markdown("""
<style>
/* Overall Background */
.stApp {
    background: linear-gradient(135deg, #ccffcc, #99e699); /* Light green to soft green gradient */
    font-family: 'Arial', sans-serif;
}

/* Frames */
.frame {
    border: 1px solid #ccc;
    border-radius: 15px;
    padding: 20px;
    margin: 15px 0;
    background-color: white;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s ease-in-out;
}
.frame:hover {
    transform: scale(1.02);
    box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
}

/* Buttons */
.custom-button {
    background-color: #4CAF50;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s;
    width: 100%;
}
.custom-button:hover {
    background-color: #45a049;
    transform: scale(1.05);
}
.danger-button {
    background-color: #e74c3c;
}
.danger-button:hover {
    background-color: #c0392b;
}

/* Header Styling */
.header {
    text-align: center;
    color: #333;
    font-size: 2rem;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
}

/* Input Fields */
input[type="text"], textarea, input[type="file"] {
    width: 100%;
    padding: 10px;
    margin: 8px 0;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)


if "response_model" not in st.session_state:
    st.session_state.response_model=""

if "rapport_medical" not in st.session_state:
    st.session_state.rapport_medical=""


if "context" not in st.session_state:
    st.session_state.context=""

# File Upload and Report Input Section
st.markdown("<div class='frame'>", unsafe_allow_html=True)

file_uploaded = st.file_uploader("Téléverser votre document (Max size: 5MB)")
rapport_medical = st.text_area("Entrer manuellement vos infos/documents:", value="", placeholder="Crée ton context...")

# Process Text Input
if rapport_medical:
    st.session_state.rapport_medical = rapport_medical

# Process Uploaded File
if file_uploaded:
    if file_uploaded.size > 5 * 1024 * 1024:
        st.error("The file exceeds the 5MB size limit. Please upload a smaller file.")
    else:
        st.session_state.rapport_medical = r_c.retrieve_content_file_uploaded(file_uploaded)

# Save Report Button

if st.button("Traitement du document", key="save_report"):
    
    content=st.session_state.rapport_medical
    
    st.write(content)
    st.session_state.context=content
        
    user_query0="Hello world:)"
    result0 = tws.get_response_model(st.session_state.context, user_query0)

st.markdown("</div>", unsafe_allow_html=True)


with st.sidebar:
    # Ensure chat history is initialized
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage(content="Hey there, I am Cassandra. How can i help you?")
        ]

    # Display conversation messages in a container
    chat_container = st.container()

    # User input box at the bottom
    user_query = st.chat_input("How can i help?")

    # Render chat history inside the container
    with chat_container:
        for message in st.session_state.chat_history:
            if isinstance(message, AIMessage):
                with st.chat_message("AI"):
                    st.write(message.content)
            elif isinstance(message, HumanMessage):
                with st.chat_message("Human"):
                    st.write(message.content)

    # Handle new user input
    if user_query is not None and user_query != "":
        # Append user message to chat history
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        with chat_container:
            with st.chat_message("Human"):
                st.markdown(user_query)

        with chat_container:
            with st.chat_message("AI"):
                context1=""
                result = tws.get_response_model(context1, user_query)
                st.session_state.chat_history.append(AIMessage(content=result))
                st.markdown(result)

            
