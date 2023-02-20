import streamlit as st
import requests
from bs4 import BeautifulSoup

def get_cves(url):
    # Make a GET request to the URL
    response = requests.get(url)

    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the CVE elements on the page
    cve_elements = soup.find_all('a', href=lambda href: href and 'cve.mitre.org/cgi-bin/cvename.cgi' in href)

    # Extract the CVE numbers from the elements
    cves = [cve.text for cve in cve_elements]

    return cves
# Define the Streamlit app
def app():
    # Add a sidebar to the app
    st.sidebar.title('Enter a URL')
    url = st.sidebar.text_input('')

    # Create a button to start the scraping process
    if st.sidebar.button('Get CVEs'):
        # Scrape the CVEs
        cves = get_cves(url)

        # Display the results in the main section
        st.write('CVEs found:')
        for cve in cves:
            st.write(f'- {cve}')
