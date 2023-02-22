import streamlit as st
import spacy

nlp = spacy.load('en_core_web_sm')

def extract_organizations(text):
    doc = nlp(text)
    organizations = [ent.text for ent in doc.ents if ent.label_ == 'ORG']
    return organizations

st.title('Organization Extractor')
text = st.text_input('Enter some text')
if text:
    organizations = extract_organizations(text)
    st.write('Organizations:', organizations)
