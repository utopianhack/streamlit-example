import streamlit as st
import tldextract

st.title("TLD Extractor")

url = st.text_input("Enter a URL:")

if url:
    with st.spinner('Extracting TLD...'):
        extracted = tldextract.extract(url)
        st.success(f"The TLD of {url} is {extracted.suffix}")
