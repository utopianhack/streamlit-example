import streamlit as st
import pandas as pd
from urllib.parse import urlparse

def get_tld(url):
    parsed = urlparse(url)
    domain = parsed.netloc.split('.')[-2:]
    return '.'.join(domain)

def plot_tld_histogram(data):
    tlds = data.apply(get_tld)
    tld_counts = tlds.value_counts()
    fig = px.histogram(tld_counts, x=tld_counts.index, y=tld_counts.values)
    st.plotly_chart(fig)

if __name__ == '__main__':
    st.title('TLD Histogram App')

    uploaded_file = st.file_uploader('Upload a CSV file', type='csv')
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        plot_tld_histogram(data)
