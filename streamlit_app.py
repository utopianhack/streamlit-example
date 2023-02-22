import streamlit as st
import requests
from bs4 import BeautifulSoup, SoupStrainer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# define the SoupStrainer to parse only visible text
only_visible_tags = SoupStrainer(lambda tag: tag.name == 'p' and tag.text.strip() != '')

def get_text(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser', parse_only=only_visible_tags)
    text = soup.get_text()
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
