import streamlit as st
from wordcloud import WordCloud
import pandas as pd

# Set the app title
st.title("Character Wordcloud Generator")

# Add a text input field
text = st.text_input("Enter your text here:")

# Create a function to generate the wordcloud
def generate_wordcloud(text):
    # Count the frequency of each character
    char_count = pd.Series(list(text)).value_counts().to_dict()
    # Create a wordcloud
    wordcloud = WordCloud(width=800, height=800, background_color="white").generate_from_frequencies(char_count)
    # Display the wordcloud
    st.image(wordcloud.to_array())

# Call the generate_wordcloud function with the input text
if text:
    generate_wordcloud(text)
