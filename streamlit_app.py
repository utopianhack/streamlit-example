import streamlit as st
import pandas as pd
from tldextract import extract

st.title("Extract Domain Names and TLDs from CSV")

# Create file uploader
uploaded_file = st.file_uploader("Choose a file", type=["csv"])
if uploaded_file is not None:
    # Read CSV file
    df = pd.read_csv(uploaded_file)
    
    # Extract domain names and TLDs
    domains = []
    tlds = []

    for index, row in df.iterrows():
        domain = extract(row['Website']).domain
        tld = extract(row['Website']).suffix
        domains.append(domain)
        tlds.append(tld)

    # Create new dataframe and display in Streamlit app
    new_df = pd.DataFrame({'Domain': domains, 'TLD': tlds})
    st.write(new_df)
