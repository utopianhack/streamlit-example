import streamlit as st
import feedparser

st.title("Get RSS URL from a Website")

url = st.text_input("Enter a website URL")

if url:
    feed = feedparser.parse(url)
    if 'rss' in feed.version.lower():
        st.write("The RSS URL for the provided website is: ")
        st.write(feed.feed.link)
    else:
        st.write("No RSS feed found for the provided website.")
