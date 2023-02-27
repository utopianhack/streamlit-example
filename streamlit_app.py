import streamlit as st
import whois

st.title('Domain Name Lookup')

domain_name = st.text_input('Enter a domain name:')

if domain_name:
    st.write(f'Information for domain: {domain_name}')
    domain_info = whois.whois(domain_name)
    st.write(domain_info)
