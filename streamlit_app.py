import streamlit as st
import requests

st.title("CVE Lookup")

st.form("cve_lookup"):
cve_input = st.text_input("Enter CVE")
submit_button = st.form_submit_button(label="Lookup")

if submit_button:
    url = f"https://services.nvd.nist.gov/rest/json/cve/1.0/{cve_input}"
    response = requests.get(url)
    if response.status_code == 200:
        json_response = response.json()
        cvss_score = json_response["result"]["CVE_Items"][0]["impact"]["baseMetricV3"]["cvssV3"]["baseScore"]
        published_date = json_response["result"]["CVE_Items"][0]["publishedDate"]
        st.write(f"The CVSS score for {cve_input} is {cvss_score}")
        st.write(f"Published date: {published_date}")
    else:
        st.write(f"Error retrieving CVSS score for {cve_input}")
