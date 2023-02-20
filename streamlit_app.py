import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv')

# Group the data by vendor and count the occurrences
vendor_counts = df.groupby('Vendor').size().reset_index(name='Counts')

# Sort the data by counts
vendor_counts = vendor_counts.sort_values(by='Counts', ascending=False)

# Create the pie chart
fig, ax = plt.subplots()
ax.pie(vendor_counts['Counts'], labels=vendor_counts['Vendor'], autopct='%1.1f%%')
ax.set_title('Most Frequent Vendors on CISA Known Exploited Vulnerabilities Catalog')

# Display the pie chart in the Streamlit app
st.pyplot(fig)
