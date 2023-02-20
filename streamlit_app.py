import streamlit as st
import mmh3
import requests

def get_favicon_hash(url):
    # Retrieve the website's favicon using a GET request to the URL + "/favicon.ico".
    icon = requests.get(url + "/favicon.ico").content
    # Calculate the hash of the favicon using the mmh3 library.
    hash_value = mmh3.hash(icon)
    return hash_value

def app():
    st.title("Calculate Favicon Hash")
    url = st.text_input("Enter a URL:")
    if st.button("Calculate"):
        hash_value = get_favicon_hash(url)
        st.success(f"The favicon hash value is {hash_value}.")
