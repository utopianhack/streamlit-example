import streamlit as st

def word_char_count(text):
    words = len(text.split())
    chars = len(text)
    return words, chars

st.title("Word and Character Count App")
user_input = st.text_area("Enter text here:")
if st.button("Count!"):
    words, chars = word_char_count(user_input)
    st.write(f"Word Count: {words}")
    st.write(f"Character Count: {chars}")
