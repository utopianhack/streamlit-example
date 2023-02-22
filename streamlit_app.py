import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(text):
    # Tokenize the text into words
    words = text.split()

    # Count the frequency of each word
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Generate the wordcloud
    wordcloud = WordCloud(width=800, height=800, background_color='white', max_words=50).generate_from_frequencies(word_counts)

    # Display the wordcloud
    plt.figure(figsize=(8,8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot()


st.title("Wordcloud Generator")

# Create a text input box for the user to input their text
input_text = st.text_input("Enter some text")

# When the user submits the text, generate and display the wordcloud
if st.button("Generate Wordcloud"):
    generate_wordcloud(input_text)
