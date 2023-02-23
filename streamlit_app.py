import streamlit as st
import pandas as pd
import tldextract

def get_domains(df):
    domains = set()
    for url in df['url']:
        ext = tldextract.extract(url)
        domain = ext.domain + '.' + ext.suffix
        domains.add(domain)
    return sorted(list(domains))

def main():
    st.title("Domain Name Extractor")
    st.write("Upload a .csv file to extract the domain names it contains.")

    # Upload file
    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        # Read file
        df = pd.read_csv(uploaded_file)

        # Extract domain names
        domains = get_domains(df)

        # Display domain names
        st.write("Domain names:")
        for domain in domains:
            st.write(domain)

if __name__ == "__main__":
    main()
