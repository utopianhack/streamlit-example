import streamlit as st
import re

def highlight_cves(text):
    cve_pattern = r'CVE-\d{4}-\d{4,7}'  # regular expression pattern for CVEs
    highlighted_text = re.sub(cve_pattern, r'<mark>\g<0></mark>', text)
    return highlighted_text

st.title('CVE Highlighter')

text = st.text_area('Enter text', '')

if st.button('Highlight CVEs'):
    highlighted_text = highlight_cves(text)
    st.markdown(highlighted_text, unsafe_allow_html=True)
