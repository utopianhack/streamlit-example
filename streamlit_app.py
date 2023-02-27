import streamlit as st
from nvdlib.nvd import NVD
from pycvesearch import CVESearch

st.title("CVE Information App")

cve_id = st.text_input("Enter the CVE ID")

if cve_id:
    nvd = NVD()
    cve = nvd.cve(cve_id)
    if cve:
        st.write("### Description")
        st.write(cve.description)
        st.write("### CVSS Score")
        st.write(cve.cvss_score)
    else:
        st.write("CVE not found in NVD")

    cve_search = CVESearch()
    cve_info = cve_search.id(cve_id)
    if cve_info:
        st.write("### References")
        st.write(cve_info.get("references", ""))
    else:
        st.write("CVE not found in CVE Search")
