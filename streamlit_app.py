import streamlit as st
import feedparser

st.title("Get RSS entries from a feed")

url = st.text_input("Enter a RSS feed URL:")

entries = feedparser.parse(str(url)).entries

st.write(entries)
