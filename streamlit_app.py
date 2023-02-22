import streamlit as st
import requests
import hashlib
from PIL import Image
from io import BytesIO

def get_favicon_hash(url):
    try:
        # fetch the favicon
        response = requests.get(f"{url}/favicon.ico")
        img = Image.open(BytesIO(response.content))
        # calculate the MD5 hash value
        md5 = hashlib.md5()
        md5.update(response.content)
        return md5.hexdigest()
    except:
        st.write("Error: Could not fetch favicon from the provided URL")
        return None

st.title("Calculate Hash of Favicon")
url = st.text_input("Enter the URL")

if url:
    favicon_hash = get_favicon_hash(url)
    if favicon_hash:
        st.write(f"The MD5 hash value of the favicon at {url} is {favicon_hash}")
