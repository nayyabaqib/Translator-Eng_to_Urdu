import streamlit as st
import argostranslate.translate

# Streamlit setup
st.set_page_config(page_title="English to Urdu Translator", layout="centered")
st.title("English to Urdu Translator (Offline & Accurate)")
st.markdown("Enter English text below and get high-quality Urdu translation — works offline and handles long text easily.")

# Load installed languages
installed_languages = argostranslate.translate.get_installed_languages()
from_lang = next((lang for lang in installed_languages if lang.code == "en"), None)
to_lang = next((lang for lang in installed_languages if lang.code == "ur"), None)

# User Input
english_text = st.text_area(
    label="Enter English text here:",
    height=300,
    placeholder="something write here...."
)

# Translate Button
if st.button("Translate"):
    if not english_text.strip():
        st.warning(" Please enter some English text.")
    elif not from_lang or not to_lang:
        st.error(" Urdu model not installed. Please run install_model.py.")
    else:
        try:
            translated_text = from_lang.get_translation(to_lang).translate(english_text)
            st.success(" Urdu Translation:")
            st.text_area(label="", value=translated_text, height=300)
        except Exception as e:
            st.error(" An error occurred during translation.")
            st.exception(e)

# Footer
st.markdown("---")
st.caption("Built using Argos Translate | Offline | Grammar-safe | Accurate translation.")