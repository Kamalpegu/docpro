import streamlit as st
import utils
import docgenerator

st.title("Document Generator")

text_input = st.text_area("Enter Text:", height=200)
keywords = st.text_input("Enter Keywords (comma-separated):")
document_type = st.text_input("Enter Document Type:")

if st.button("Generate Document"):
    cleaned_text = utils.clean_text(text_input)
    structured_content = docgenerator.generate_structured_content(cleaned_text, keywords, document_type)
    st.markdown(structured_content)
