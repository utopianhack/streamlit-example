import streamlit as st
import tldextract

# Set up the Streamlit app
st.title("URL Domain Extractor")
url = st.text_input("Enter a URL")

# Extract the domain and TLD using tldextract
extracted = tldextract.extract(url)
domain = extracted.domain
tld = extracted.suffix

# Display the domain and TLD
if url:
    st.write(f"Domain: {domain}")
    st.write(f"TLD: {tld}")
