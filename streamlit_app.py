import streamlit as st
import re

def extract_domain(text):
    pattern = r"(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    domain_list = re.findall(pattern, text)
    return [domain[0] for domain in domain_list]

def main():
    st.title("Extract Domain Names from Text")
    input_text = st.text_input("Enter Text:")
    if input_text:
        domain_list = extract_domain(input_text)
        if domain_list:
            st.write("Domain Names:")
            for domain in domain_list:
                st.write(domain)
        else:
            st.write("No domain names found in the text")

if __name__ == '__main__':
    main()
