import streamlit as st
import re

def defang_text(text):
    # Define regular expressions for domains, URLs, and IP addresses
    domain_regex = r"(?<!\S)((?:[a-zA-Z0-9_-]+\.)+[a-zA-Z]{2,})(?!\S)"
    url_regex = r"(?P<url>https?://[^\s]+)"
    ip_regex = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

    # Replace matching patterns with their defanged equivalents
    defanged_text = re.sub(domain_regex, r"\1[.]com", text)
    defanged_text = re.sub(url_regex, r"\g<url> [.]com", defanged_text)
    defanged_text = re.sub(ip_regex, r"[IP ADDRESS]", defanged_text)
    return defanged_text

st.title("Defang Text App")

text_input = st.text_input("Enter text to defang:")
if text_input:
    defanged_text = defang_text(text_input)
    st.write(defanged_text)
