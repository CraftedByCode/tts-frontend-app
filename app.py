import streamlit as st
import requests

st.title(" Text To Speech ")

# Add custom CSS to style the text input
st.markdown(
    """
    <style>
    .stTextInput input {
        font-size: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create the text input field
dialogue = st.text_input("Enter a dialogue/talk here")
language = st.selectbox(
    "language(dialogue/speech language)",
    ("ta", "en", "fr"),
    index=None,
    key=str,
    placeholder="Select language",
)

if st.button("Generate"):
    if not dialogue:
        st.markdown('<span style="color:red">Text feild not be Empty</span>', unsafe_allow_html=True)
    
    response = requests.post(
        "https://tts-app-bay.vercel.app/convert", json={"dialogue": dialogue, "language": language}
    )
    if response.status_code == 201:
        res_audio = requests.get("https://tts-app-bay.vercel.app/retrive")
        
        if res_audio.status_code == 200:
            st.markdown("<span style=color:cyan>Audio file is Generated!</span>",unsafe_allow_html=True)
            st.audio(res_audio.content, format="audio/mp3")
