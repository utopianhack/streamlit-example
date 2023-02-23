import streamlit as st
import pandas as pd
import tldextract

def extract_tld(url):
    extracted = tldextract.extract(url)
    return extracted.suffix

def main():
    st.title("Most Frequent TLDs")
    st.write("Enter a list of URLs to see the most frequent TLDs.")

    # Get the list of URLs from the user
    input_urls = st.text_area("Enter URLs, one per line")

    # Convert the input URLs to a list
    urls = input_urls.split("\n")

    # Extract the TLDs from the URLs
    tlds = [extract_tld(url) for url in urls]

    # Count the frequencies of each TLD
    tld_counts = pd.Series(tlds).value_counts()

    # Display the histogram of the most frequent TLDs
    st.bar_chart(tld_counts.head(10))

if __name__ == "__main__":
    main()
