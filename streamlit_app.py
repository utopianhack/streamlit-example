import streamlit as st
import pandas as pd

# Load CISA Known Exploited Vulnerabilities catalog as a dataframe
cisa_catalog = pd.read_csv('CISA_Known_Exploited_Vulnerabilities.csv')

# Get the date the catalog was last updated
last_updated = cisa_catalog['Date Last Updated'][0]

# Get the 5 most recently added CVEs
recent_cves = cisa_catalog[['CVE ID', 'Date Added']].sort_values(by=['Date Added'], ascending=False)[:5]

# Display the date the catalog was last updated
st.write("CISA Known Exploited Vulnerabilities catalog was last updated on ", last_updated)

# Display the 5 most recently added CVEs
st.write("The 5 most recently added CVEs are:")
for index, row in recent_cves.iterrows():
    st.write(row['CVE ID'], " (Added on ", row['Date Added'], ")")
