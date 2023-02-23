import streamlit as st
import tldextract

st.title('URL Domain and TLD Extractor')

url = st.text_input('Enter a URL:')

if url:
    extracted_url = tldextract.extract(url)
    domain = extracted_url.domain
    tld = extracted_url.suffix
    st.write(f'Domain: {domain}')
    st.write(f'TLD: {tld}')

if __name__ == '__main__':
    st.run_app()
