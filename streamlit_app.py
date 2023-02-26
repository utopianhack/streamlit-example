import streamlit as st
import pandas as pd
import plotly.express as px

# Load the CSV file
df = pd.read_csv("https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv")

# Group the data by product and count the occurrences
product_counts = df.groupby("product").size().reset_index(name="Counts")

# Sort the products by counts in descending order
product_counts = product_counts.sort_values("Counts", ascending=False)

# Create a histogram using Plotly Express
fig = px.histogram(product_counts.head(10), x="product", y="counts", title="Most Frequent Products")

# Display the histogram using Streamlit
st.plotly_chart(fig)
