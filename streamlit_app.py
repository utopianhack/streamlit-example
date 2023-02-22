import streamlit as st
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud

def scrape_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = ' '.join([p.text for p in soup.find_all('p')])
    return text

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(text)
    return wordcloud.to_image()

# Set the title of the app
st.title('Web Scraper and Wordcloud Generator')

# Add a text input for the URL
url = st.text_input('Enter the URL of the webpage you want to scrape:')

# Add a button to start scraping
if st.button('Scrape'):
    # Call the scrape_text function to get the text
    text = scrape_text(url)

    # Generate the wordcloud and display it
    image = generate_wordcloud(text)
    st.image(image, use_column_width=True)
