import pandas as pd
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def load_data():
    df = pd.read_csv('CISA_Known_Exploited_Vulnerabilities.csv')
    return df

def generate_wordcloud(df):
    vendors = df['Vendor'].dropna()
    vendor_counts = vendors.value_counts()
    wordcloud = WordCloud(background_color='white').generate_from_frequencies(vendor_counts)
    return wordcloud

def main():
    st.title('CISA Known Exploited Vulnerabilities')
    st.subheader('Most Common Vendors Wordcloud')

    df = load_data()
    wordcloud = generate_wordcloud(df)

    st.image(wordcloud.to_array())

if __name__ == '__main__':
    main()
