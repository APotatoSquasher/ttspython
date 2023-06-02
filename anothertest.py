import streamlit as st
from text_to_speech import save
st.set_page_config(page_title="Text To Speech Website",layout='wide',page_icon=":speaking_head:")
st.subheader("TTS Service")
g = st.text_area("Input your text here!","")
lang = st.text_input("Insert the language code. If no language code is put, the default language will be English. For references on this, visit [this Wikipedia article.](https://en.wikipedia.org/wiki/IETF_language_tag)","")
if(st.button('Submit')):
    
    if(lang == ""):
        lang = "en"
    save(g, lang, file="Hello-World.mp3")
    audio_file = open('Hello-World.mp3','rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes,format='audio/mp3')
    
    

st.write("Want to say something? [Click here!](https://github.com/APotatoSquasher/ttspython)")