import streamlit as st
import pandas as pd
import plotly.express as px

# Load the CSV file
df = pd.read_csv("https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv")

# Add a sidebar
st.sidebar.title("Select options")

# Add a dropdown menu to select the column
column = st.sidebar.selectbox("Select a column", df.columns)

# Add a dropdown menu to select the plot type
plot_type = st.sidebar.selectbox(
    "Select a plot type",
    {
        "Bar Chart": px.bar,
        "Pie Chart": px.pie,
        "DataFrame": st.write,
    },
)

# Count the frequency of the selected column
counts = df[column].value_counts()

# Create a chart based on the user's selection
if plot_type == "DataFrame":
    plot_type(counts)
else:
    fig = plot_type(x=counts.index, y=counts.values)
    st.plotly_chart(fig)
