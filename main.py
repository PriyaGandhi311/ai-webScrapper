import streamlit as st
from scrape import scrape_website, extract_body_content, clean_body_content, split_content_into_chunks

from bs4 import BeautifulSoup

st.title("AI Web Scrapper")

url = st.text_input("Enter the URL to scrape:")

if st.button("Scrape Site"):
    st.write("Scraping the website...")
    result = scrape_website(url)
    dom_content = extract_body_content(result)
    cleaned_content = clean_body_content(dom_content)
    # chunks = split_content_into_chunks(content, max_length=6000)
    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("Dom Content", cleaned_content, height=300)
