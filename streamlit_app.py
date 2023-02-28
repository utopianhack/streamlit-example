import re
import pandas as pd
import streamlit as st

def highlight_iocs(text):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    ip_regex = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    cve_regex = r'\bCVE-\d{4}-\d{4,7}\b'
    asn_regex = r'\bAS\d+\b'
    
    email_matches = re.findall(email_regex, text)
    ip_matches = re.findall(ip_regex, text)
    cve_matches = re.findall(cve_regex, text)
    asn_matches = re.findall(asn_regex, text)
    
    for match in email_matches:
        text = text.replace(match, f'<span style="background-color: #ffff00">{match}</span>')
        
    for match in ip_matches:
        text = text.replace(match, f'<span style="background-color: #ff00ff">{match}</span>')

    for match in cve_matches:
        text = text.replace(match, f'<span style="background-color: #00ff00">{match}</span>')

    for match in asn_matches:
        text = text.replace(match, f'<span style="background-color: #0000ff">{match}</span>')
        
    return text

def main():
    st.title('IOC Highlighter')
    input_text = st.text_area('Enter text:', height=200)
    
    if input_text:
        output_text = highlight_iocs(input_text)
        st.markdown(output_text, unsafe_allow_html=True)
        
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        ip_regex = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
        cve_regex = r'\bCVE-\d{4}-\d{4,7}\b'
        asn_regex = r'\bAS\d+\b'
        
        email_matches = [(match, 'Email') for match in re.findall(email_regex, input_text)]
        ip_matches = [(match, 'IP Address') for match in re.findall(ip_regex, input_text)]
        cve_matches = [(match, 'CVE') for match in re.findall(cve_regex, input_text)]
        asn_matches = [(match, 'ASN') for match in re.findall(asn_regex, input_text)]
        
        data = {'Type': [match[1] for match in email_matches + ip_matches + cve_matches + asn_matches],
                'Value': [match[0] for match in email_matches + ip_matches + cve_matches + asn_matches]}
        
        df = pd.DataFrame(data)
        st.write(df)

if __name__ == '__main__':
    main() 
