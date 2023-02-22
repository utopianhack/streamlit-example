import streamlit as st
import tldextract
import pandas as pd
import matplotlib.pyplot as plt


st.title("Extract URLs and plot their TLDs")

# Take text input
text = st.text_area("Enter text", height=200)

# Extract URLs and plot TLDs
if st.button("Extract URLs"):
    urls = []
    for line in text.split('\n'):
        urls += re.findall("(?P<url>https?://[^\s]+)", line)
    tlds = [tldextract.extract(url).suffix for url in urls]
    tld_counts = pd.Series(tlds).value_counts()
    st.bar_chart(tld_counts)
