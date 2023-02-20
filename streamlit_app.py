import requests
from bs4 import BeautifulSoup
import re

def get_cves_from_url(url):
    # send a GET request to the URL
    response = requests.get(url)

    # check if the response was successful
    if response.status_code != 200:
        return []

    # parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # find all the text in the page
    text = soup.get_text()

    # use regular expressions to extract CVEs from the text
    cve_pattern = r"CVE-\d{4}-\d+"
    cves = re.findall(cve_pattern, text)

    return cves

import streamlit as st

# import the get_cves_from_url function from the previous step
from get_cves_from_url import get_cves_from_url

# set the title of the app
st.title("CVE Extractor")

# create a text input for the user to enter a URL
url = st.text_input("Enter a URL to extract CVEs from:")

# if the user enters a URL and clicks the "Extract" button,
# extract the CVEs from the URL and display them
if st.button("Extract"):
    cves = get_cves_from_url(url)
    if not cves:
        st.write("No CVEs found in the URL.")
    else:
        st.write("CVEs found in the URL:")
        for cve in cves:
            st.write(cve)
