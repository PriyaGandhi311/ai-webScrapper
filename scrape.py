import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def scrape_website(website_url):
    chrome_driver_path = "./chromedriver.exe"
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

    try:
        driver.get(website_url)
        html = driver.page_source
        return html
    finally:
        driver.quit()

def extract_body_content(content):
    soup = BeautifulSoup(content, 'html.parser')
    body_content = soup.find('body')
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup =  BeautifulSoup(body_content, 'html.parser')
    for script_or_style in soup(['script', 'style']):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator='\n')
    cleaned_content = "/n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
    return cleaned_content

def split_content_into_chunks(content, max_length):
    return [content[i:i + max_length] for i in range(0, len(content), max_length)]
