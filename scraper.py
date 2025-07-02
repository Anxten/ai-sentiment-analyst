# scraper.py

from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_kompas_article(url: str):
    """
    Fungsi ini menerima sebuah URL artikel Kompas, melakukan scraping,
    dan mengembalikan judul serta isi teksnya.
    """
    print(f"Mencoba mengambil data dari: {url}")
    
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--log-level=3')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36')
    
    driver = None
    try:
        driver = webdriver.Chrome(options=options)
        driver.get(url)

        wait = WebDriverWait(driver, 20)
        title_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'read__title')))
        title = title_element.text
        
        content_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'read__content')))
        content_html = content_element.get_attribute('innerHTML')
        soup_content = BeautifulSoup(content_html, 'lxml')

        paragraphs = [p.get_text(strip=True) for p in soup_content.find_all('p') if not p.find('strong')]
        full_text = "\n".join(paragraphs)

        return title, full_text

    finally:
        if driver:
            driver.quit()