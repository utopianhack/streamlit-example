import pandas as pd
import streamlit as st
import tldextract
import matplotlib.pyplot as plt

def extract_urls(df):
    urls = []
    for index, row in df.iterrows():
        urls_in_row = tldextract.extract(row[0])
        urls.append(urls_in_row.domain + '.' + urls_in_row.suffix)
    return urls

def count_tlds(urls):
    tlds = pd.Series(urls).value_counts()
    return tlds

def display_histogram(tlds):
    plt.bar(tlds.index, tlds.values)
    plt.xticks(rotation=90)
    st.pyplot()

def main():
    st.title("URL TLD Histogram")
    file = st.file_uploader("Upload file", type="csv")
    if file is not None:
        df = pd.read_csv(file)
        urls = extract_urls(df)
        tlds = count_tlds(urls)
        display_histogram(tlds)

if __name__ == "__main__":
    main()
