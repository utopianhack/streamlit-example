import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
from wordcloud import WordCloud

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

# Add date range selection to sidebar
start_date = st.sidebar.date_input('Start date', min_value=df['dateAdded'].min(), max_value=df['dateAdded'].max(), value=df['dateAdded'].min())
end_date = st.sidebar.date_input('End date', min_value=df['dateAdded'].min(), max_value=df['dateAdded'].max(), value=df['dateAdded'].max())

# Filter data by date range
filtered_data = df[(df['dateAdded'] >= start_date) & (df['dateAdded'] <= end_date)]


# Add a dropdown menu to select the plot type
plot_type = st.sidebar.selectbox(
    "Select a plot type",
    {
        "Bar Chart": px.bar,
        "Pie Chart": px.pie,
        "Line Chart": px.line,
        "Word Cloud": st.image,
    },
)

# Count the frequency of the selected column for the top 10 values
counts_10 = filtered_data[column].value_counts().head(10)
counts = filtered_data[column].value_counts()

# Create a chart based on the user's selection
if plot_type == "Line Chart":
    fig = px.line(x=counts.index, y=counts.values)
    
if plot_type == "Bar Chart":
    fig = px.bar(x=counts.index, y=counts.values)
    
if plot_type == "Pie Chart":
    fig = px.pie(names=counts_10.index, values=counts_10.values)
    
elif plot_type == "Word Cloud":
    # Create a wordcloud from the vulnerabilityName column
    text = " ".join(df[column].fillna(""))
    wordcloud = WordCloud(width=800, height=400).generate(text)
    # Display the wordcloud as an image
    st.image(wordcloud.to_array(), use_column_width=True)

# Count the number of CVEs on the list
num_cves = filtered_data.shape[0]

# Count the number of unique products
num_products = filtered_data["product"].nunique()

# Count the number of unique vendors
num_vendors = filtered_data["vendorProject"].nunique()

# Select the most recent dateAdded
most_recent = filtered_data["dateAdded"].max()

# Count the number of CVEs added on the date of most_recent
num_added_on_most_recent = filtered_data[filtered_data["dateAdded"] == most_recent].shape[0]

# Select the CVEs added on date of most_recent
most_recent_cves = filtered_data[filtered_data['dateAdded'] == most_recent]['cveID']

# Select the most frequent value in the product column
most_frequent_product = filtered_data["product"].value_counts().index[0]

# Select the frequency of the most frequent value
frequency = filtered_data["product"].value_counts().max()

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
st.dataframe(filtered_data)
