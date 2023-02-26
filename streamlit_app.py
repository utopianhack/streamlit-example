import streamlit as st
import pandas as pd
import plotly.express as px

# Load the CSV file
df = pd.read_csv("https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv")

# Add a sidebar
st.sidebar.title("Select Plot Type")

# Add a dropdown menu to select the column
column = st.sidebar.selectbox("Select Column", df.columns)

# Add a dropdown menu to select the plot type
plot_type = st.sidebar.selectbox("Select Plot Type", ["Bar Chart", "Pie Chart"])

# Count the frequency of the selected column
counts = df[column].value_counts()

# Create a chart based on the user's selection
if plot_type == "Bar Chart":
    fig = px.bar(x=counts.index, y=counts.values)
else:
    fig = px.pie(names=counts.index, values=counts.values)

# Count the number of CVEs on the list
num_cves = df.shape[0]

# Select the most recent dateAdded
most_recent = df["dateAdded"].max()

# Select the most frequent value in the product column
most_frequent_product = df["product"].value_counts().index[0]

# Select the frequency of the most frequent value
frequency = df["product"].value_counts().max()

# Divide the app into three equal-width columns
col1, col2, col3 = st.columns(3)

# Display the metrics in separate columns
with col1:
    st.metric("Number of CVEs", num_cves)

with col2:
    st.metric("Last Update", most_recent)

with col3:
    st.metric("Product With Most CISA KEV CVEs", most_frequent_product, f"{frequency} occurrences")

# Display the chart using Streamlit
st.plotly_chart(fig)
st.dataframe(df)
