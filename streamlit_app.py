import pandas as pd
import spacy
import streamlit as st
import spacy_streamlit

catalog = pd.read_csv('https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv')
nlp = spacy.load('en_core_web_sm')

def app():
    st.title('CISA Known Exploited Vulnerabilities Catalog')
    st.write('This app highlights named entities in the shortDescription column.')
    spacy_streamlit.visualize_ner(
        nlp, 
        catalog['shortDescription'], 
        labels=nlp.get_pipe('ner').labels
    )

if __name__ == '__main__':
    app()
