import streamlit as st
import nltk
from nltk import ngrams
from collections import Counter
import matplotlib.pyplot as plt

def generate_ngrams(text, n):
    words = nltk.word_tokenize(text)
    n_grams = ngrams(words, n)
    return [ ' '.join(grams) for grams in n_grams]

st.title("N-gram Histogram")

text = st.text_area("Enter some text to analyze:", height=200)

n = st.slider("Select the length of the n-grams:", min_value=1, max_value=5, value=2)

if st.button("Generate Histogram"):
    ngram_list = generate_ngrams(text.lower(), n)
    ngram_counts = Counter(ngram_list)
    sorted_ngrams = sorted(ngram_counts.items(), key=lambda x: x[1], reverse=True)
    
    if ngram_list:
        st.write(f"Most common {n}-grams:")
        fig, ax = plt.subplots()
        ax.bar([x[0] for x in sorted_ngrams[:10]], [x[1] for x in sorted_ngrams[:10]])
        plt.xticks(rotation=90)
        st.pyplot(fig)
    else:
        st.write("Please enter some text to analyze.")
