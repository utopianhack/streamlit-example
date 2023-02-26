import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# Load the CSV file
df = pd.read_csv("https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv")

st.set_page_config(layout="wide")

# Add a sidebar
st.sidebar.title("Select Plot Type")

col1, col2 = st.columns(2)

# Display the metrics in separate columns
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/1/1f/CISA_Logo.png", width=200)  
with col2:
    st.title("CISA KEV Explorer")
    
# Add a dropdown menu to select the column
column = st.sidebar.selectbox("Select Column", df.columns)

# Add a dropdown menu to select the plot type
plot_type = st.sidebar.selectbox(
    "Select a plot type",
    {
        "Bar Chart": px.bar,
        "Pie Chart": px.pie,
        "DataFrame": st.write,
        "Word Cloud": st.image,
    },
)

# Count the frequency of the selected column for the top 10 values
counts = df[column].value_counts().head(10)

# Create a chart based on the user's selection
if plot_type == "DataFrame":
    plot_type(counts)
elif plot_type == "Word Cloud":
    # Create a wordcloud from the vulnerabilityName column
    text = " ".join(df["vulnerabilityName"].fillna(""))
    wordcloud = WordCloud(width=800, height=400).generate(text)
    # Display the wordcloud as an image
    st.image(wordcloud.to_array(), use_column_width=True)
else:
    fig = plot_type(x=counts.index, y=counts.values)
    st.plotly_chart(fig)

# Count the number of CVEs on the list
num_cves = df.shape[0]

# Count the number of unique products
num_products = df["product"].nunique()

# Count the number of unique vendors
num_vendors = df["vendorProject"].nunique()

# Select the most recent dateAdded
most_recent = df["dateAdded"].max()

# Count the number of CVEs added on the date of most_recent
num_added_on_most_recent = df[df["dateAdded"] == most_recent].shape[0]

# Select the most frequent value in the product column
most_frequent_product = df["product"].value_counts().index[0]

# Select the frequency of the most frequent value
frequency = df["product"].value_counts().max()

# Divide the app into three equal-width columns
col1, col2, col3, col4 = st.columns(4)

# Display the metrics in separate columns
with col1:
    st.metric("Last Update", most_recent, f"{num_added_on_most_recent} CVEs Added")

with col2:
    st.metric("Product With Most CISA KEV CVEs", most_frequent_product, f"{frequency} CVEs")

with col3:
    st.metric("Number of Products", num_products, f"From {num_vendors} Vendors")    
    
with col4:
    st.metric("Number of CVEs", num_cves)

# Display the chart using Streamlit
st.plotly_chart(fig)
st.dataframe(df)
