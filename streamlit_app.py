import streamlit as st
from urllib.parse import urlparse

def get_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.split('.')
    if len(domain) == 2:
        return domain[0], domain[1]
    elif len(domain) == 3:
        return domain[1], domain[2]
    else:
        return None, None

st.title("Domain Extractor")

url = st.text_input("Enter a URL")
if url:
    top_level_domain, second_level_domain = get_domain(url)
    st.write(f"Top Level Domain: {top_level_domain}")
    st.write(f"Second Level Domain: {second_level_domain}")
