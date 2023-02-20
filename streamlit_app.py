import streamlit as st
from urllib.parse import urlparse

st.title("Extract Domain from URL")

# Get URL input from user
url = st.text_input("Enter a URL:")

# Extract domain from URL
if url:
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    st.write("Domain:", domain)
