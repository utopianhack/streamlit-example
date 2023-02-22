import streamlit as st
import pandas as pd
import re
from collections import Counter

# Step 1: File upload widget
csv_file = st.file_uploader("Upload CSV", type=["csv"])

if csv_file is not None:
    # Step 2: Read CSV into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Step 3: Extract URLs from DataFrame
    pattern = r"(?P<url>https?://[^\s]+)"
    urls = df["text"].str.extractall(pattern)["url"].tolist()

    # Step 4: Count TLD occurrences
    tlds = [re.search(r"(?<=\.)\w+$", url).group(0) for url in urls]
    tld_counts = Counter(tlds)

    # Step 5: Display URLs in a Streamlit DataFrame
    st.write("Extracted URLs:")
    st.dataframe(pd.DataFrame(urls, columns=["URL"]))

    # Step 6: Display histogram of most common TLDs
    st.write("Most common TLDs:")
    tld_counts_df = pd.DataFrame.from_dict(tld_counts, orient="index", columns=["count"])
    st.bar_chart(tld_counts_df.sort_values(by="count", ascending=False).head(10))
