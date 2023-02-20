import streamlit as st
from pyvuln.nvd import NVD

def get_cve_info(cve):
    nvd = NVD.from_feeds()
    cve_item = nvd.get_by_cve_id(cve)
    if cve_item:
        return cve_item['description'], cve_item['published_date']
    else:
        return None, None

    # App title
st.title('CVE Information App')

# CVE input field
cve = st.text_input('Enter CVE')

# Button to get CVE info
if st.button('Get CVE Info'):
    description, published_date = get_cve_info(cve)
    if description and published_date:
        st.write('Description:', description)
        st.write('Published date:', published_date)
    else:
        st.write('CVE not found')
