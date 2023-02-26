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

# Display the chart using Streamlit
st.plotly_chart(fig)
st.dataframe(df.[str(column)])
