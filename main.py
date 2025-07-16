import streamlit as st
from scrape import scrape_website, extract_body_content, clean_body_content, split_content_into_chunks
from parse import parse_content
from bs4 import BeautifulSoup

st.title("AI Web Scrapper")

url = st.text_input("Enter the URL to scrape:")

if st.button("Scrape Site"):
    st.write("Scraping the website...")
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("Dom Content", cleaned_content, height=300) 

if 'dom_content' in st.session_state:
    parse_description = st.text_input("Describe what you want to parse:")
    if st.button("Parse Content"):
        if parse_description:
            status_text = st.empty()
            status_text.write("Parsing content...")
            dom_chunks = split_content_into_chunks(st.session_state.dom_content, 6000)
            result = parse_content(dom_chunks, parse_description)
            status_text.write("Done!")
            st.write(result)

