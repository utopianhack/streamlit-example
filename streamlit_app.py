import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('path/to/known_exploits.csv')

# Group the data by product and count the number of vulnerabilities
product_counts = data.groupby('Product').count()['ID'].sort_values(ascending=False)

# Generate the wordcloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(product_counts)

# Define the Streamlit app
st.title("CISA's Known Exploited Vulnerabilities - Most Frequent Products")
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(plt.figure(figsize=(20,10)))
