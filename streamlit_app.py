import streamlit as st
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def get_text(url):
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)
    return text

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          min_font_size=10).generate(text)
    return wordcloud

st.title('Webpage Word Cloud Generator')
url = st.text_input('Enter the URL of the webpage you want to generate the word cloud for:')
if st.button('Generate Word Cloud'):
    text = get_text(url)
    text = ' '.join([t.strip() for t in text])
    wordcloud = generate_wordcloud(text)
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    st.pyplot()
