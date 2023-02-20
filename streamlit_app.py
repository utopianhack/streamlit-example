import streamlit as st
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder
import matplotlib.pyplot as plt

def get_ngrams(text, n=2, num=10):
    # tokenize the text
    tokens = word_tokenize(text)
    # calculate the frequency distribution of ngrams
    ngram_measures = BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(tokens)
    finder.apply_freq_filter(2)  # filter out ngrams that occur less than 2 times
    ngrams = finder.nbest(ngram_measures.raw_freq, num)
    freq_dist = finder.ngram_fd.items()
    # return the top n ngrams and their frequency
    return ngrams, freq_dist[:num]

st.title('Ngram Visualizer')

text = st.text_area('Enter text')

if st.button('Generate Ngrams'):
    ngrams, freq_dist = get_ngrams(text)
    # convert frequency distribution to a pandas dataframe
    freq_df = pd.DataFrame(freq_dist, columns=['ngram', 'frequency']).sort_values(by='frequency', ascending=False)
    # plot the most frequent ngrams
    plt.bar(freq_df['ngram'], freq_df['frequency'])
    plt.xticks(rotation=90)
    st.pyplot()

    
